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
the two candidates social media trends
"""
VERSION = '1.2'

"""STANDARD LIBRARY IMPORTS"""
import json
import platform
import os
import sys
import datetime
from datetime import timedelta
import numpy

"""LOCAL LIBRARY IMPORTS"""
import collecting
import scoring
import graphing

"""FOLDER IMPORTS"""


"""MAIN"""
def main(election_search = None):
												#INTRO#
	#------------------------------------------------------------------------------------------------#
	#The convention is alphbetical#
	if(election_search == None):
		if(platform.system() == "Darwin"):#MAC
			election_search = raw_input("What election: ")#The two last names of the candidates i.e. Comstock Wexton
	   
		if(platform.system() == "Windows"):#WINDOWS
			election_search = input("What election: ")#The two last names of the candidates i.e. Comstock Wexton
	else:
		pass
	"""
	collection_of_tweets follows this file format
	candidate, date, tweet, likes, replies, sentitment
	"""
	collection_of_tweets = {}
	"""
	collection_of_polls follows this file format
	date, candidate, score
	"""
	collection_of_polls = {}
	"""
	x = date
	y = score
	"""
	coordinates_of_tweets = {}#comprised of [x,y] scores
	coordinates_of_polls = {}#comprised of [x,y] scores
	
	"""twitter handles for candidates"""
	#Collecting candidates Name
	list_of_candidates = []
	list_of_names = election_search.split(" ")
	for i in range(int(len(list_of_names)/2)):
		list_of_candidates.append(list_of_names[(2*i)] + " " + list_of_names[(2*i+1)])
	
	print(list_of_candidates)
	candidates_handle = {}
	for candidate in list_of_candidates:
		candidates_handle[candidate] = collecting.Handle(candidate)
		
											#Collecting Poll Data#
	#------------------------------------------------------------------------------------------------#
	if(os.path.isfile('DATA-POLL ' + election_search + '.txt')):
		with open('DATA-POLL ' + election_search + '.txt', 'r') as fp:
			collection_of_polls = json.load(fp)
	else:
		collection_of_polls = collecting.CollectPoll(election_search)#collection_of_polls[date] = score name
	
	"""Iterate through the dates in the dict of polls and find the corresponding tweets from that week."""
	if(os.path.isfile('DATA-TWEETS ' + election_search + '.txt')):
		with open('DATA-TWEETS ' + election_search + '.txt','r') as fp:
			collection_of_tweets = json.load(fp)

	else:
										#Collecting Over The Whole Election#
	#-----------------------------------------------------------------------------------------------#
		poll_list = []
		for date in collection_of_polls:
			poll_list.append(date)
		
		print(poll_list)
		StartDate = poll_list[-1]
		month = int(StartDate.split("/")[0])
		day = int(StartDate.split("/")[1])
		#start = datetime.datetime(2018, month, day)#FIXME
		start = datetime.datetime(2018, 10, 1)
		
		EndDate = poll_list[0]
		month = int(EndDate.split("/")[0])
		day = int(EndDate.split("/")[0])
		#end = datetime.datetime(2018, month, day)#FIXME
		end = datetime.datetime(2018, 11, 6)	
			
											#Collecting Tweets#
	#-----------------------------------------------------------------------------------------------#
		#ASCII for the letter A
		for candidate in list_of_candidates:
			collection_of_tweets[str(candidate)] = collecting.Collect(candidates_handle[candidate], start, end)

		with open('DATA-TWEETS ' + election_search + '.txt', 'w') as outfile:
			json.dump(collection_of_tweets, outfile)

											#Scoring Everything#
	#-----------------------------------------------------------------------------------------------#
	"""
	compDict = scoring.ConvertTweets('DATA-TWEETS ' + election_search + '.txt')
	
	print(collection_of_polls['11/6'])
	results = scoring.GetResults(list_of_candidates, collection_of_polls['11/6'])
	print(results)
	listArr = [];
	for candidate in collection_of_tweets.keys():
		sumarr = [];
		for entry in compDict[candidate]:
			a = numpy.array(entry)
			sumarr.append(a)
		listArr.append(sumarr)
	
	final_resultsA, final_resultsB = scoring.Scoring("BLANK_FILE.txt", listArr, results)
	print("RESULTS: " , final_resultsA[2])
	"""
	result, final_resultsX, final_resultsY = scoring.main_scoring(election_search)
	print("RESULTS: ", result)
	print("Y", final_resultsY)
												#Graphing#
	#------------------------------------------------------------------------------------------------#
	graphing.MakeGraphs('DATA-TWEETS ' + election_search + '.txt')
	graphing.Graph(final_resultsX, final_resultsY,"time", "Comparing")
	
if __name__ == '__main__':
	import testingTheGui
	testingTheGui.MAINApp().run()