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
file = open('C:/Users/nogos/Documents/GitHub/Predicting-Elections/Test.txt', 'r+')
sentiment.Sentiment(file)
	#return 