#cmd /K "$(FULL_CURRENT_PATH)"
# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

"""
Author: Zachary Nowak and Ethan Saari
Date: 01/03/2019

Program Description: Graph the set
over the specific time stamp 
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json

def MakeGraphs():
	with open("Comstock Wexton tweets.txt",'r') as fp:
		collection_of_tweets = json.load(fp)
	
	coordinates_of_tweets = {}
		
	for date in collection_of_tweets.keys():
		stuff = collection_of_tweets[date]
		try: 
			plt.plot(3, stuff[0][2], 'bo')
		except IndexError:
			pass
	plt.show()
	
def Graph(xdata, ydata, xname, title):
	plt.plot(xdata, ydata, color='blue')
	plt.ylabel("Dates")
	plt.xlabel(xname)
	plt.title(title)
	plt.show()
	return None;
	
if __name__=="__main__":
	MakeGraphs()