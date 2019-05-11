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
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import calendar
abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

def value_to_float(x):
	if type(x) == float or type(x) == int:
		return x
	if 'K' in x:
		if len(x) > 1:
			return float(x.replace('K', '')) * 1000
		return 1000.0
	if 'M' in x:
		if len(x) > 1:
			return float(x.replace('M', '')) * 1000000
		return 1000000.0
	if 'Like' in x or 'Retweet' in x:
		return 10
	else:
		return float(x)

def MakeGraphs(name_of_file):
	with open(name_of_file,'r') as fp:
		collection_of_tweets = json.load(fp)
	
	coordinates_of_tweets = {}
	x_axis_A = []
	y_axis_A = []	
	
	x_axis_B = []
	y_axis_B = []
	
	candidate = name_of_file.split(" ")
	A_name = candidate[-2]+" "+candidate[-1].split(".")[0]
	B_name = candidate[-4]+" "+candidate[-3]
	for date in collection_of_tweets.keys():
		stuff = collection_of_tweets[date]
		for tweet in stuff:
			try:
				tweet = tweet[0]
			
				year = int(tweet[0].split(" ")[2])
				month = ((tweet[0].split(" ")[1]))
				month = (abbr_to_num[month])
				day = int(tweet[0].split(" ")[0])
				new_date = datetime.date(year, month, day)
				
				num_of_like = value_to_float(tweet[3])
				if(date == A_name):
					y_axis_A.append(float(num_of_like))
					x_axis_A.append(new_date)
				else:
					y_axis_B.append(float(num_of_like))
					x_axis_B.append(new_date)
				
			except IndexError:
				pass
				
	plt.ylabel('Number of Retweets')
	plt.title('Number of Retweets Per Tweet')
	plt.plot_date(x_axis_A, y_axis_A, 'ro', xdate = True, label = A_name)
	plt.plot_date(x_axis_B,y_axis_B, 'bo', xdate = True, label = B_name)
	plt.legend()
	plt.gcf().autofmt_xdate()
	plt.show()
def meth(start, stop, step):
	l = []
	i = start
	while i <= stop:
		l.append(i)
		i += step
	return l
def Graph(xdata, ydata, xname, title):
	l = meth(0, 50, 50/(len(xdata)-1))
	print(l)
	plt.plot( xdata, l , color='black')
	plt.plot(xdata, (ydata), color='Blue', label = "Donnelly's Favorability with Respect to Braun")
	plt.ylabel("Percent Favorability")
	plt.xlabel(xname)
	plt.title(title)
	plt.legend()
	plt.show()
	return None;

def GraphPolls(name_of_file):
	with open( name_of_file, 'r') as fp:
		collection_of_polls = json.load(fp)
		print(collection_of_polls)
	coordinates_of_polls = {}
	x_axis_A = []
	y_axis_A = []	
	
	x_axis_B = []
	y_axis_B = []
	
	x_axis_C = []
	y_axis_C = []
	#Make Dates
	
	#Candidate A is positive
	candidates = (name_of_file.split(" "))
	candidateA = name_of_file.split(" ")[2]
	candidateB = name_of_file.split(" ")[-1].split(".")[0]
	
	
	for date in collection_of_polls.keys():
		stuff = collection_of_polls[date]
		value = (float(stuff.split("+")[1]))
		name = stuff.split("+")[0]
		
		print(date.split("/")[0])#month
		
		year = 2019
		month = int(date.split("/")[0])
		day = int(date.split("/")[1])
		new_date = datetime.date(year, month, day)
		
		if candidateA in name:
			value = value/2
			x_axis_A.append(new_date)
			y_axis_A.append(50+value)
		else:
			value = -1*value/2
			x_axis_B.append(new_date)
			y_axis_B.append(50+value)
		
		x_axis_C.append(new_date)
		y_axis_C.append(50)
		
	plt.ylabel('Percentage of People')
	plt.title('Poll Prediction of the Election')
	plt.plot_date(x_axis_A, y_axis_A, 'bo', xdate = True, label = candidateA)
	plt.plot_date(x_axis_B, y_axis_B, 'ro', xdate = True, label = candidateB)
	plt.plot_date(x_axis_C,y_axis_C, 'k-', xdate = True)
	plt.legend()
	plt.gcf().autofmt_xdate()
	plt.show()
	
def GraphCompiled(xArr1, yArr1, xArr2, yArr2):
	#assume it is every day
	plt.ylabel("Favorability Index")
	plt.xlabel("Days")
	plt.title("candidate Favorability")
	plt.plot(xArr1, yArr1, color='red')
	plt.plot(xArr2, yArr2, color='blue')
	plt.show()
	
if __name__=="__main__":
	#Graph([12,13,14],[1,2,3],"a","b")
	MakeGraphs("DATA-TWEETS Joe Donnelly Mike Braun.txt")
	GraphPolls("DATA-POLL Joe Donnelly Mike Braun.txt")