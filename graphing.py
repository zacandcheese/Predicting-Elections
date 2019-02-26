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

def Graph(xdata, ydata):
	plt.plot(xdata, ydata, color='blue')
	plt.ylabel(xname)
	plt.xlabel(yname)
	plt.title(title)
	plt.show()
	return None;