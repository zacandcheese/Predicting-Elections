#cmd /K "$(FULL_CURRENT_PATH)"
# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

"""
Author: Zachary Nowak and Ethan Saari
Date: 01/03/2019

Program Description: This uses the
dataset to calculate a score.
"""
import sentiment
import sys, os, json, numpy
from datetime import date
import calendar
abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

#ADDED 3/14
import codecs, json

#def Score(dataset1):		
#file = open('C:/Users/nogos/Documents/GitHub/Predicting-Elections/Test.txt', 'r+')
#sentiment.Sentiment(file)
#return 

def ConvertTweets(name_of_file):
	with open(name_of_file, 'r') as fp:
		collection_of_tweets = json.load(fp)
	compiled = {}
	for canidate in collection_of_tweets.keys():
		try:
			currentDay = collection_of_tweets[canidate][0][0]
		except IndexError:
			currentDay = "1 Nov 2018"
		listPerDay = []
		listDayBefore = [0,0,0,0,0]
		listOfSummaries = []
		print(canidate)#, currentDay, listPerDay, listDayBefore)
		for tweet in collection_of_tweets[canidate]:
			#print(tweet)
			try:
				if(tweet[0] == currentDay): #Is the tweet on the same day
					listPerDay.append(tweet)#If it is still the same day
				else:
					#NewDay!
					currentDay = tweet[0] #FIXME Current day wasn't updating right
					#SUMMARY of the old list
					date1 = 0
					avglikes = 0
					avgretweets = 0
					toplikes = 0;
					topretweets = 0;
					spos = 0;
					sneg = 0;
					sneu = 0;
					dayArray = []
					if(len(listPerDay)>0):
						for day in listPerDay:
							
							try:
								if(float(day[2]) > toplikes):
									toplikes = float(day[2])
								if(float(day[3]) > topretweets):
									topretweets = float(day[3])
								
								avglikes += float(day[2])/len(listPerDay)
								avgretweets += float(day[3])/len(listPerDay)
								date1 = day[0]
								
								
								year = int(date1.split(" ")[2])
								month = ((date1.split(" ")[1]))
								month = (abbr_to_num[month])
								newday = int(date1.split(" ")[0])
								new_date = date(year, month, newday)
								
								yday = (new_date - date(2018, 1, 1)).days
								date1 = yday
								#sneg, sneu, spos = sentiment.Sentiment(day[1]) FIXME
							except ValueError:
								avglikes = 0
								avgretweets = 0
								toplikes = 0;
								topretweets = 0;
								spos = 0;
								sneg = 0;
								sneu = 0;
								yday = 0;
								
						
						dayArray = [date1, int(avglikes), int(avgretweets), int(toplikes), int(topretweets)]
						
						arr1 = numpy.array(dayArray)
						arr2 = numpy.array(listDayBefore)
						#print(arr1, arr2)
						sum = (arr1 - arr2)
						sum[0] = date1
						print("SUMMARY---------------------", sum)
						#listOfSummaries.append(dayArray)#TEMPORARY 
						#listOfSummaries.append(sum)#FIXME
						listOfSummaries.append(sum.tolist())#FIXME
						
						listDayBefore = dayArray
					
					#Update to set up for new day
					listPerDay.clear()
					listPerDay.append(tweet)
					
				
					
			except IndexError:
				pass
		
		print("FINISHED A CANIDATE")
		compiled[canidate] = listOfSummaries
		listPerDay.clear()
		listDayBefore.clear()
		#Dont clear a list you eventually want to return it destroys the memory idiot.
	print("DONE")
	
	with open(name_of_file + " compiled.txt", 'w') as fout:
		print(compiled)
		json.dump(compiled, fout)
	
	return(compiled)
	
	#print(compiled)
				#-------------------------------------#
		# for each day I need to get the average likes and retweets #
		# senitment and the difference from the day before, iterate #
		# through each day ... #
		
	
def Scoring(collection_of_tweets, end):
	pass
	

	
if __name__ == '__main__':
	#name_of_file = "Comstock Wexton tweets.txt"
	#name_of_file = "Kaine Stewart tweets.txt"
	name_of_file = "Brat Spanberger tweets.txt"
	"""with open(name_of_file, 'r') as fp:
		collection_of_tweets = json.load(fp)
	for canidate in collection_of_tweets.keys():
		print(collection_of_tweets[canidate], "\n")"""
	dict = ConvertTweets(name_of_file)
	with open(name_of_file + " compiled.txt", 'r') as fin:
		b = json.load(fin)
		for canidate in b.keys():
			print(canidate)
			sum = 0;
			for entry in b[canidate]:
				a = numpy.array(entry)
				sum += a[1]
			print(sum)