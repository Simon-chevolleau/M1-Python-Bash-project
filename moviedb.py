#!/usr/bin/python3
import json
import argparse
import re #Regex

# actor = {}

# with open('moviedb_small.json', 'r') as file:
# 	for line in file:
# 		movie = json.loads(line)
# 		for name in movie['cast']:
# 			actor[name] = [movie['title'], movie['year']]

# f = open('test.json', 'w')
# f.write(actor)
# f.close()

#Argument section
parser = argparse.ArgumentParser()
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

