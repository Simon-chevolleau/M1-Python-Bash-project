#!/usr/bin/env python3
# encoding=utf8
import json
import argparse
import re #Regex
import sys

actor = {}
director = {}

with open('moviedb_small.json', 'r') as file:
	for line in file:
		movie = json.loads(line)
		if "directors" and "year" in movie:
			for name in movie['cast']:
				if name in actor:
					actor[name].append((movie['title'], movie['year']))
				else:
					actor[name] = [movie['title'], movie['year']]

		if "directors" and "year" in movie:
			for name in movie['directors']:
				if name in director:
					director[name].append((movie['title'], movie['year']))
				else:
					director[name] = [movie['title'], movie['year']]

with open('actors.json', 'w') as data_actor:
	for name in actor:
		data_actor.write("{}{}\n".format(name, actor[name]))

with open('directors.json', 'w') as data_director:
	for name in director:
		data_director.write("{}{}\n".format(name, director[name]))

#Argument section
parser = argparse.ArgumentParser()
args, unknown = parser.parse_known_args(["sys.argv[2]", "sys.argv[3]"])
parser.add_argument('-c','--create-from-db', dest='createfromdb', action='store_true', help="prend en entrée le fichier JSON passé en paramètre à cette option et crée à partir de la base qu'il contient une base de données d'acteurs et de réalisateurs")

parser.add_argument('-a','--actor', dest='actor', action='store_true', help="Créer une liste au format CSV recensant le nombre de films tournés par les acteurs")

parser.add_argument('-d','--director', dest='director', action='store_true',help="Créer une liste au format CSV recensant le nombre de films tournés par les réalisateurs ")
args = parser.parse_args()

#Paramètre -c ou --create-from-db
if args.createfromdb:
	print("1")

#Paramètre -a ou --actor 
if args.actor:
	print("2")

#Paramètre -d ou --director
if args.director:
	print("3")

