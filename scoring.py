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
import time
import sys, os, json, numpy
from datetime import date
import calendar
import scoringMatrix

abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

#ADDED 3/14
import codecs, json

#def Score(dataset1):		
#file = open('C:/Users/nogos/Documents/GitHub/Predicting-Elections/Test.txt', 'r+')
#sentiment.Sentiment(file)
#return
def makeDay(date1):
	#WHAT IS THE DAY?
	year = int(date1.split(" ")[2])
	month = ((date1.split(" ")[1]))
	month = (abbr_to_num[month])
	newday = int(date1.split(" ")[0])
	new_date = date(year, month, newday)
	yday = (new_date - date(2018, 1, 1)).days
	date1 = yday
	return (int(yday))
	
def doNothing(x=None, x2=None, x3=None,x4 = None):
	pass
def convert(block):
	block = str(block)
	try:
		if block == "Like" or block == "Retweet": return 1
		new = (float(block))
	except ValueError:
		new = 0
		if 'K' in block:
			num = float(block[:-1])*1000			
		if 'M' in block:
			num = float(block[:-1])*1000000
		new = (num)
	return(new)

def GetResults(list_of_candidates, result):
	name = result.split('+')[0]
	value = float(result.split('+')[1])
	final_list = []
	for candidate in list_of_candidates:
		if name in candidate:
			final_list.append(50+value/2)
		else:
			final_list.append(50-value/2)
	return(final_list)
	
def ConvertTweets(name_of_file, method=doNothing):
	with open(name_of_file, 'r') as fp:
		collection_of_tweets = json.load(fp)
	
	compiled = {}
	
	for candidate in collection_of_tweets.keys():
		#try:
		#	currentDay = collection_of_tweets[candidate][0][0]
		#except IndexError:
		#	currentDay = "3 Oct 2018"
		
		currentDay = 275
		listPerDay = []
		listDayBefore = [275,0,0,0,0]#DAY 1
		listOfSummaries = []
		method("NAME: " + candidate + "\n")
		
		#TWEETS ARE NOT IN THE CORRECT ORDER
		#I NEED TO FIX THIS
		
		sorted_list = []
		for i in range(275,309):
			flag = True
			for tweet in collection_of_tweets[candidate]:

				if tweet:
					if (makeDay(tweet[0]) == i):
						sorted_list.append(tweet)
						flag = False
				else:
					pass
			if flag:
				sorted_list.append([])
		
		#START SORTING THE TWEETS
		for tweet in sorted_list:
			#print(tweet)
			
			#----------------------------------------CASE 1: NO TWEETS WERE POSTED-------------------------------#
			if not tweet and not listPerDay:
				method("\tCASE 1: THE DAY IS " + str(currentDay))
				dayArray = [currentDay,0,0,0,0]				
				
				arr1 = numpy.array(dayArray)
				arr2 = numpy.array(listDayBefore)
				#print(arr1, arr2)
				sum = (arr1 - arr2)
				sum[0] = currentDay
				
				method("SUMMARY---------------------", sum, "\n")
				listOfSummaries.append(sum.tolist())
				listDayBefore = dayArray
				currentDay += 1
				
			
			elif not tweet:
				#-----------------------------------CASE 2: DAY SWITCHED TO AN EMPTY DAY--------------------------#
				#FIRST APPEND YESTERDAY, THEN APPEND TODAY, THEN CLEAR LIST, INCREMENT DAY
				method("\tCASE 2: THE DAY IS " + str(currentDay))
				avglikes = 0
				avgretweets = 0
				toplikes = 0;
				topretweets = 0;
				spos = 0;
				sneg = 0;
				sneu = 0;
				dayArray = []

				for day in listPerDay:
					if(convert(day[2]) > toplikes):
						toplikes = convert(day[2])
					if(convert(day[3]) > topretweets):
						topretweets = convert(day[3])
					
					avglikes += convert(day[2])/float(len(listPerDay))
					avgretweets += convert(day[3])/float(len(listPerDay))
					#sneg, sneu, spos = sentiment.Sentiment(day[1]) FIXME
								
						
				dayArray = [day_of_tweet, int(avglikes), int(avgretweets), int(toplikes), int(topretweets)]
				
				arr1 = numpy.array(dayArray)
				arr2 = numpy.array(listDayBefore)
				sum = (arr1 - arr2)
				sum[0] = currentDay
				method("SUMMARY---------------------", sum, "\n")
				listOfSummaries.append(sum.tolist())		
				listDayBefore = dayArray		
				currentDay += 1
				
				
				dayArray = [currentDay, 0,0,0,0]
				arr1 = numpy.array(dayArray)
				arr2 = numpy.array(listDayBefore)
				sum = (arr1 - arr2)
				sum[0] = currentDay
				method("SUMMARY---------------------", sum, "\n")
				listOfSummaries.append(sum.tolist())		
				listDayBefore = dayArray		
				currentDay += 1
				
				listPerDay.clear()
			else:	
				#--------------------------------------CASE 3: ONE OR MORE TWEETS WERE POSTED------------------------------------#
				#WHAT IS THE DAY?
				date1 = tweet[0]
				year = int(date1.split(" ")[2])
				month = ((date1.split(" ")[1]))
				month = (abbr_to_num[month])
				newday = int(date1.split(" ")[0])
				new_date = date(year, month, newday)
				yday = (new_date - date(2018, 1, 1)).days
				date1 = yday
				
				method("THIS IS THE DATE ", yday, tweet[0], currentDay)	
				day_of_tweet = yday
				
				
				if(day_of_tweet == currentDay):
					method("ADDING")
					listPerDay.append(tweet)
				else:
					#NEW DAY
					method("----------------------NEW DAY--------------------")
					method("\tCASE 3: THE DAY IS " + str(currentDay))
					#SUMMARY of the old list
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
							if(convert(day[2]) > toplikes):
								toplikes = convert(day[2])
							if(convert(day[3]) > topretweets):
								topretweets = convert(day[3])
							
							avglikes += convert(day[2])/len(listPerDay)
							avgretweets += convert(day[3])/len(listPerDay)
							#sneg, sneu, spos = sentiment.Sentiment(day[1]) FIXME
								
						
						dayArray = [day_of_tweet, int(avglikes), int(avgretweets), int(toplikes), int(topretweets)]
						
						arr1 = numpy.array(dayArray)
						arr2 = numpy.array(listDayBefore)
						#print(arr1, arr2)
						sum = (arr1 - arr2)
						sum[0] = date1-1
						method("SUMMARY---------------------", sum, "\n")
						
						
						currentDay += 1
						listOfSummaries.append(sum.tolist())
						
						listDayBefore = dayArray
						currentDay = day_of_tweet
					
					
					#Update to set up for new day
					listPerDay.clear()
					listPerDay.append(tweet)
				#time.sleep(2)
		print("Finished Candidate's Tweets")
		compiled[candidate] = listOfSummaries
		listPerDay.clear()
		listDayBefore.clear()
		#Dont clear a list you eventually want to return it destroys the memory idiot.
	print("DONE")
	
	with open(name_of_file + " compiled.txt", 'w') as fout:
		print(compiled)
		json.dump(compiled, fout)
	
	return(compiled)

def loadMatrix(name_of_file):
	with open(name_of_file, 'r') as file:
		b = json.load(file)
		"""
		for matrix in b:
			print(numpy.array(matrix))
		"""
		arr1 = numpy.array(b[0])
		arr2 = numpy.array(b[1])
		return arr1, arr2
					
def Scoring(name_of_file, list_of_collection_of_tweets, final_result):
	n = 601
	size = (len(list_of_collection_of_tweets[0][0]))#[][]
	matrix = scoringMatrix.scoringMatrixOverTime(num_of_factors = size, num_of_weights = 2, learning_rate = 0.4, method = doNothing)#CONSTRUCTOR
	for i in range(n):
		#matrix.train(list_of_collection_of_tweets[i%2],final_result[i%2], 50)
		if(matrix.train(list_of_collection_of_tweets[i%2],final_result[i%2])):
			break
		if(i%100 == 0):
			print(i)
						#upload matrix#
	#-------------------------------------------------------------#
	with open(name_of_file, 'w') as file:
		json.dump([(matrix.getMatrix()[0]).tolist(),(matrix.getMatrix()[1]).tolist()], file)

	print(matrix.getMatrix())
	
	print("First Run", matrix.run(list_of_collection_of_tweets[0]), "\nSecond Run", matrix.run(list_of_collection_of_tweets[1]))
	return(matrix.run(list_of_collection_of_tweets[0]), matrix.run(list_of_collection_of_tweets[1]))

	
if __name__ == '__main__':
	name_of_file = "DATA-TWEETS Tim Kaine Corey Stewart.txt"
	final_result_file = "Comstock Wexton poll.txt"
	final_result = 0
	
	with open(final_result_file, 'r') as file:
		dict = json.load(file)
		final_result = dict['11/6']
		final_result = (float(final_result.split('+')[1]))
		result_list = []
		final_result_a = 50-final_result/2
		result_list.append(final_result_a)
		final_result_b = 50+final_result/2
		result_list.append(final_result_b)

	dict = ConvertTweets(name_of_file,print)
	with open(name_of_file + " compiled.txt", 'r') as fin:
		b = json.load(fin)
		listArr = []
		
		for candidate in b.keys():
			print(candidate)
			sumarr = [];
			
			for entry in b[candidate]:
				a = numpy.array(entry)
				sumarr.append(a)
			listArr.append(sumarr)
		
			#Scoring("Comstock Wexton Matrix.txt", listArr, result_list)
		Scoring("Comstock Matrix.txt", listArr, result_list)
		#print(sumarr)"""
		

