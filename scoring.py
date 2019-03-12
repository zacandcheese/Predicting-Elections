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
import sentiment, sys, os, json, numpy

#def Score(dataset1):		
#file = open('C:/Users/nogos/Documents/GitHub/Predicting-Elections/Test.txt', 'r+')
#sentiment.Sentiment(file)
#return 

def ConvertTweets(name_of_file):
	with open(name_of_file, 'r') as fp:
		collection_of_tweets = json.load(fp)
	compiled = {}
	for canidate in collection_of_tweets.keys():

		currentDay = collection_of_tweets[canidate][0][0]
		listPerDay = []
		listDayBefore = ['',0,0,0,0]
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
					date = ""
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
								date = day[0]
								#sneg, sneu, spos = sentiment.Sentiment(day[1]) FIXME
							except ValueError:
								date = ""
								avglikes = 0
								avgretweets = 0
								toplikes = 0;
								topretweets = 0;
								spos = 0;
								sneg = 0;
								sneu = 0;
						dayArray = [date, int(avglikes), int(avgretweets), int(toplikes), int(topretweets)]
						
						arr1 = numpy.array(dayArray[1:])
						arr2 = numpy.array(listDayBefore[1:])
						#print(arr1, arr2)
						print("SUMMARY---------------------", arr1 - arr2)
						#listOfSummaries.append(dayArray)#TEMPORARY 
						listOfSummaries.append(arr1 - arr2)#FIXME
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
	return(compiled)
	#print(compiled)
				#-------------------------------------#
		# for each day I need to get the average likes and retweets #
		# senitment and the difference from the day before, iterate #
		# through each day ... #
		
	
def Scoring(collection_of_tweets, end):
	"""
	print("\nNEW LINE\n"+ end)
	try:
		print((collection_of_tweets[end][1]))
		print("\n")
		#Create features
		tweet = collection_of_tweets[end][1]
		negative, neutral, positive = sentiment.Sentiment(tweet[1])
		print("size", len(tweet[1]), "negative: ", negative, "neutral:", neutral,"positive:", positive, "likes", tweet[2],"retweets", tweet[3])
	except IndexError:
		pass
	"""
	pass
	

	
if __name__ == '__main__':
	name_of_file = "Comstock Wexton tweets.txt"
	"""with open(name_of_file, 'r') as fp:
		collection_of_tweets = json.load(fp)
	for canidate in collection_of_tweets.keys():
		print(collection_of_tweets[canidate], "\n")"""
	dict = ConvertTweets(name_of_file)
	for canidate in dict.keys():
		sum = 0
		for entry in dict[canidate]:
			try:
				sum += entry[2]
			except IndexError:
				pass
		print(sum)
	"""
	list_of_canidates = ["Comstock","Wexton"]
	import json
		

	with open(,'r') as fp:
		collection_of_tweets = json.load(fp)
	
	coordinates_of_tweets = {}
	print(len(collection_of_tweets.keys()))
	
	#[date,body, likes, retweets]
	for date in collection_of_tweets.keys():
		coordinates_of_tweets[date] = Scoring(collection_of_tweets, date)
	"""	
		
