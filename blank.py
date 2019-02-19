"""import os, urllib, sys
filename = 'http://www.google.com/search?' + urllib.urlencode({'q': ' '.join(sys.argv[1:]) })
cmd = os.popen("lynx -dump %s" % filename)
output = cmd.read()
cmd.close()
print(output)"""

def Scoring(collection_of_tweets, end):
	print("\nNEW LINE\n"+ end)
	try:
		print(collection_of_tweets[end])
	except IndexError:
		pass

list_of_canidates = ["Comstock","Wexton"]
import json
	

with open("Comstock Wexton poll.txt",'r') as fp:
	collection_of_tweets = json.load(fp)
	
print(collection_of_tweets)	
coordinates_of_tweets = {}
print(len(collection_of_tweets.keys()))
for date in collection_of_tweets.keys():
	coordinates_of_tweets[date] = Scoring(collection_of_tweets, date)