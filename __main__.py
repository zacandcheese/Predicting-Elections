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
VERSION = '1.0'
__author__ = 'Zachary Nowak, Ethan Saari'

"""STANDARD LIBRARY IMPORTS"""
import json
import platform
import os

"""LOCAL LIBRARY IMPORTS"""
import collecting
import scoring
import graphing

"""FOLDER IMPORTS"""


"""MAIN"""
def main():

	# Example 1 - Use canidate's tweets
	dataset1 = collecting.Collect("Canidate 1")#"Canidate 1" should be a handle
	dataset2 = collecting.Collect("Canidate 2")#"Canidate 2" should be a handle
	
	score1, score2 = scoring.Score(dataset1, dataset2)
	graphing.Graph(score1, score2)
	
if __name__ == '__main__':
	main()