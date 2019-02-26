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
VERSION = '1.2'
__author__ = 'Zachary Nowak, Ethan Saari'

"""STANDARD LIBRARY IMPORTS"""
import json
import platform
import os
import sys
import datetime
from datetime import timedelta

"""LOCAL LIBRARY IMPORTS"""
import collecting
import scoring
import graphing

"""FOLDER IMPORTS"""


"""MAIN"""
def main():
												#INTRO#
	#------------------------------------------------------------------------------------------------#
	#The convention is alphbetical#
	if(platform.system() == "Darwin"):#MAC
		election_search = raw_input("What election: ")#The two last names of the canidates i.e. Comstock Wexton
   
	if(platform.system() == "Windows"):#WINDOWS
		election_search = input("What election: ")#The two last names of the canidates i.e. Comstock Wexton
		
	"""
	collection_of_tweets follows this file format
	canidate, date, tweet, likes, replies, sentitment
	"""
	collection_of_tweets = {}
	"""
	collection_of_polls follows this file format
	date, canidate, score
	"""
	collection_of_polls = {}
	"""
	x = date
	y = score
	"""
	coordinates_of_tweets = {}#comprised of [x,y] scores
	coordinates_of_polls = {}#comprised of [x,y] scores
	
	"""twitter handles for canidates"""
	#Collecting Canidates Name
	list_of_canidates = election_search.split(" ")
	canidates_handle = {}
	for canidate in list_of_canidates:
		canidates_handle[canidate] = collecting.Handle(canidate)
		
											#Collecting Poll Data#
	#------------------------------------------------------------------------------------------------#

	if(os.path.isfile(election_search + " poll.txt")):
		with open(election_search + " poll.txt", 'r') as fp:
			collection_of_polls = json.load(fp)
	else:
		collection_of_polls = collecting.CollectPoll(election_search)#collection_of_polls[date] = score name
	
	"""Iterate through the dates in the dict of polls and find the corresponding tweets from that week."""
	if(os.path.isfile(election_search + " tweets.txt")):
		with open(election_search + " tweets.txt",'r') as fp:
			collection_of_tweets = json.load(fp)

	else:		
		for date in collection_of_polls:
			date_list = date.split("/")
			month = int(date_list[0])
			day = int(date_list[1])
			end = datetime.datetime(2018, month, day)# year, month, day
			start = end - timedelta(days=7)# a week back from the end
			print('\n\n'+ str(start) + " " + str(end) + '\n\n')
			
											#Collecting Tweets#
	#-------------------------------------------------------------------------------------------------#
			i = 65 #ASCII for the letter A
			for canidate in list_of_canidates:
				collection_of_tweets[(str(end)+chr(i))] = collecting.Collect(canidates_handle[canidate], start, end)
				i += 1

		with open(election_search + " tweets.txt", 'w') as outfile:
			#with open(os.path.join(sys.path[0],"tweets"), 'w') as outfile:
			json.dump(collection_of_tweets, outfile)

											#Scoring Everything#
	#-----------------------------------------------------------------------------------------------#
	for date in collection_of_tweets.keys():
		for j in range(len(list_of_canidates)):
			coordinates_of_tweets[date+chr(j+65)] = scoring.Scoring(collection_of_tweets, date)
	
	"""FIXME"""
	#Coordinates of polls needs to be tuned#
	
	graphing.Graph(coordinates_of_polls, coordinates_of_tweets)
	
if __name__ == '__main__':
	main()