# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT
import re
from setuptools import setup, find_packages

def parse_version(str_):
    """
    Parses the program's version from a python variable declaration.
    """
    v = re.findall(r"\d+.\d+.\d+", str_)
    if v:
        return v[0]
    else:
        print("cannot parse string {}".format(str_))
        raise KeyError

# Our version is stored here.
with open("__main__.py") as f:
    _version_line = [line for line in f.readlines()
                     if line.startswith("VERSION")][0].strip()
    VERSION = parse_version(_version_line)

setup(name='searchtweets',
      description="Determining Elections based off of Social Media Trends",
      url='https://github.com/zacandcheese/Predicting-Elections',
      author='Zachary Nowak, Ethan Saari',
      long_description=open('README.md', 'r', encoding="utf-8").read(),
      author_email='zacandcheese@icloud.com',
      license='MIT',
      version=VERSION,
      python_requires='>=3.1',
      install_requires=["platform", "os"],
      packages=find_packages(),
     )