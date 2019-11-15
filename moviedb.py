#!/usr/bin/python
import json
import argparse
import re #Regex

actor = {}

with open('moviedb_small.json', 'r') as file:
	for line in file:
		movie = json.loads(line)
		for name in movie['cast']:
			actor[name] = [movie['title'], movie['year']]

f = open('test.json', 'w')
f.write(actor)
f.close()