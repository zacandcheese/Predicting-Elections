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
"""
from paralleldots import set_api_key, get_api_key

def Sentiment(data)
	set_api_key("VIJL2MNSIraV6xzz2fNepEPdGX86Rxd7s0JvCqwqAEI")
	print(get_api_key())
	from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
	return(sentiment(data)) 