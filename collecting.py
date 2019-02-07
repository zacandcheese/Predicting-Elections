#cmd /K "$(FULL_CURRENT_PATH)"
# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

"""
Author: Zachary Nowak and Ethan Saari
Date: 01/03/2019

Program Description: Returns a set of all tweets
from handle for a certain time stamp
"""
def Collect(user, start, end):
	#https://github.com/bpb27/twitter_scraping/blob/master/scrape.py
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
	from time import sleep
	import json
	import datetime

	"""
	# edit these three variables
	user = 'realdonaldtrump'
	start = datetime.datetime(2010, 2, 10)  # year, month, day
	end = datetime.datetime(2016, 12, 7)  # year, month, day
	"""
	
	# only edit these if you're having problems
	delay = 1  # time to wait on each page load before reading the page
	driver = webdriver.Chrome()  # options are Chrome() Firefox() Safari()

	#main list is made up of date lists
	main_list = []
	
	#date list
	date_list = []
	# don't mess with this stuff
	twitter_ids_filename = 'all_ids.json'
	days = (end - start).days + 1
	id_selector = '.time a.tweet-timestamp'
	tweet_selector = 'li.js-stream-item'
	user = user.lower()

	def format_day(date):
		day = '0' + str(date.day) if len(str(date.day)) == 1 else str(date.day)
		month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
		year = str(date.year)
		return '-'.join([year, month, day])

	def form_url(since, until):
		p1 = 'https://twitter.com/search?f=tweets&vertical=default&q=from%3A'
		p2 =  user + '%20since%3A' + since + '%20until%3A' + until + 'include%3Aretweets&src=typd'
		return p1 + p2

	def increment_day(date, i):
		return date + datetime.timedelta(days=i)

	for day in range(days):
		date_list.clear()#ADDED
		
		d1 = format_day(increment_day(start, 0))
		d2 = format_day(increment_day(start, 1))
		url = form_url(d1, d2)
		driver.get(url)
		sleep(delay)

		try:
			found_tweets = driver.find_elements_by_css_selector(tweet_selector)
			increment = 10

			while len(found_tweets) >= increment:
				print('scrolling down to load more tweets')
				driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
				sleep(delay)
				found_tweets = driver.find_elements_by_css_selector(tweet_selector)
				increment += 10

			#print('{} tweets found, {} total'.format(len(found_tweets), len(ids)))

			for tweet in found_tweets:
				try:
					id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
					date = (tweet.find_element_by_css_selector(id_selector).text)
					tweet_body = tweet.find_element_by_css_selector("p.TweetTextSize").text#WORKS YAYYYY!
					likes = tweet.find_element_by_css_selector("div[class = 'ProfileTweet-action ProfileTweet-action--favorite js-toggleState'").text#like button
					retweets = tweet.find_element_by_css_selector("div[class = 'ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt'").text#Retweet button
					
					print("USUALY A DATE: " + date)
					print("TWEET: " + tweet_body)
					print("LIKES: "+ likes.replace("Like\n",""))
					print("RETWEETS: "+ retweets.replace("Retweet\n",""))
					
					date_list.extend((date,tweet_body,likes.replace("Like\n",""),retweets.replace("Retweet\n","")))
					main_list.append(date_list)
					
					
				except StaleElementReferenceException as e:
					print('lost element reference', tweet)

		except NoSuchElementException:
			pass

		start = increment_day(start, 1)

	print('all done here')
	driver.close()
	print(main_list)
	return main_list
	
def CollectPoll(election_search):
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from googlesearch import search
	import json
												#search for the poll html file#
	url = []
	for url2 in search('Poll Data ' + election_search, stop=1):
		url.append(url2)

	html_file = url[0]	

										   #get the html file and search for the poll#
	driver = webdriver.Chrome()
	driver.get(html_file)

	xpath = ("/html/body[@class='polls']/div[@id='container']/div[@class='alpha-container ']/div[@class='alpha']/div[@id='polling-data-full']/table[@class='data large ']/tbody")
	table_id = driver.find_element(By.XPATH, xpath)
	rows = table_id.find_elements(By.TAG_NAME, "tr")#get all of the rows in the table
	poll_dict = {}


	for row in rows:
		line = row.text.split(" ")#seperate the string line to format more like a table
		try:
			if('/' in line[-10]): #Checks to see if that spot is a date
				#Date, Name of Canidate in Favor, Score
				print(line[-10] + " score: " + line[-2] + line[-1])
				#Set the key to be the range of dates
				poll_dict[line[-10]] = line[-2] + line[-1]
		except IndexError:
			pass
		except:
			print("Something went wrong. Please refer to our error documents for trouble shooting")
		
		
	print(poll_dict)
												#dump the dictionary to a seperate file for future use#
	with open(election_search + " poll.txt", 'w') as fout:
		json.dump(poll_dict, fout)
		
		
	assert "No results found." not in driver.page_source
	driver.close()
	return(poll_dict)

def Handle(name):
	if(name == "Wexton"):
		return("JenniferWexton")
	elif(name == "Comstock"):
		return("RepComstock")
		
if __name__ == "__main__":
	CollectPoll("Wexton_Comstock")
	

