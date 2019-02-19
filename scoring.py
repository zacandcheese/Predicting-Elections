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
import sentiment, sys, os

#def Score(dataset1):		
#file = open('C:/Users/nogos/Documents/GitHub/Predicting-Elections/Test.txt', 'r+')
#sentiment.Sentiment(file)
#return 

def Scoring(collection_of_tweets, end):
	print("\nNEW LINE\n"+ end)
	try:
		print(collection_of_tweets[end][1])
	except IndexError:
		pass
		
if __name__ == '__main__':
	list_of_canidates = ["Comstock","Wexton"]
	import json
		

	with open("Comstock Wexton tweets.txt",'r') as fp:
		collection_of_tweets = json.load(fp)
	
	coordinates_of_tweets = {}
	print(len(collection_of_tweets.keys()))
	
	#[date,body, likes, retweets]
	for date in collection_of_tweets.keys():
		coordinates_of_tweets[date] = Scoring(collection_of_tweets, date)
		
		
		
