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

#def Score(dataset1):		
#file = open('C:/Users/nogos/Documents/GitHub/Predicting-Elections/Test.txt', 'r+')
#sentiment.Sentiment(file)
#return 
def Scoring(collection_of_tweets, end):
	print("\nNEW LINE\n"+ end)
	print(collection_of_tweets[end][0])
			
if __name__ == '__main__':
	list_of_canidates = ["Wexton","Comstock"]
	import json
		
	with open("tweets",'r') as fp:
		collection_of_tweets = json.load(fp)
	
	coordinates_of_tweets = {}
	for date in collection_of_tweets.keys():
		for j in range(len(list_of_canidates)):
			coordinates_of_tweets[date+chr(j+65)] = Scoring(collection_of_tweets, date)