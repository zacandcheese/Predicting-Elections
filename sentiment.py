#cmd /K "$(FULL_CURRENT_PATH)"
# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

"""
Author: Zachary Nowak and Ethan Saari
Date: 01/03/2019

Program Description: Analyze the given
data for sentiment and return value

canidate, date, tweet, likes, replies, sentiment
"""
from paralleldots import set_api_key, similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
import json

def Sentiment(tweet):
	set_api_key("VIJL2MNSIraV6xzz2fNepEPdGX86Rxd7s0JvCqwqAEI")
	score = sentiment(tweet)
	data = json.dumps(score)
	#print(score)
	result = data.split('{')[2]
	finalResult = result.split('}')[0]
	negative = score['probabilities']['negative']
	neutral = score['probabilities']['neutral']
	positive = score['probabilities']['positive']
	
	#print(negative, neutral, positive)
	return(negative, neutral, positive)
	
if __name__== '__main__':
	Sentiment("hi zach")