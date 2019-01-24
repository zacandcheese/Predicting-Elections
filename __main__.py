#cmd /K "$(FULL_CURRENT_PATH)"
# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

"""
Author: Zachary Nowak and Ethan Saari
Date: 01/03/2019

Program Description: This code can
determine elections based off of 
the two canidates social media trends
"""
VERSION = '1.1'
__author__ = 'Zachary Nowak, Ethan Saari'

"""STANDARD LIBRARY IMPORTS"""
import json
import platform
import os
import datetime

"""LOCAL LIBRARY IMPORTS"""
import collecting
import scoring
import graphing

"""FOLDER IMPORTS"""


"""MAIN"""
def main():
	
	start = datetime.datetime(2010, 1, 1)  # year, month, day
	end = datetime.datetime(2016, 12, 7)  # year, month, day
	
	"""
	collection_of_tweets follows this file format
	canidate, date, tweet, likes, replies, sentitment
	"""
	collection_of_tweets = open("tweets.txt","w+")# open a file for writing and create it if it doesn't exist
	"""
	collection_of_polls follows this file format
	date, canidate, score
	"""
	collection_of_polls = open("polls.txt","w+")
	"""
	x = date
	y = score
	"""
	coordinates_of_tweets = {}#comprised of [x,y] scores
	coordinates_of_polls = {}#comprised of [x,y] scores
	
	#Collecting Canidates Name
	list_of_canidates = []
	
	#Collecting Handles
	for canidate in list_of_canidates:
		canidates_handle = collecting.Handle(canidate)
		collection_of_tweets.write(collecting.Collect(canidates_handle))
		
	#Collecting Poll Data
	collection_of_polls.append(collecting.CollectPoll("election_name")#date, canidate, score
	
	#Coordinates of Poll
	for line in coordinates_of_polls:
		line = line.delimited(",")
		coordinates_of_polls[line[0],line[1] + " " + line[2]]#date, canidate+score
	
	#Scoring Sentiment
	#Adds a sentiment score to each line of tweets
	sentiment.Sentiment(collection_of_tweets)
	
	#Scoring Everything
	for date in coordinates_of_polls.keys():
		end = date
		start = date - datetime.timedelta(7)
		coordinates_of_tweets[date] = score.Scoring(collection_of_tweets, start, end)
	
	
	collection_of_polls.close()
	collection_of_tweets.close()
	
	graphing.Graph(coordinates_of_polls, coordinates_of_tweets)
	
if __name__ == '__main__':
	main()