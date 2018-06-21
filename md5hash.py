#!/bin/python
#this program will request a directory to search and a file extension type to search for
#will then walk the directory and its subdirectories and list all files that have the same MD5 hash, side by side.

import os
import hashlib

dictionary = {}

path = raw_input("\nPlease enter the full path name of the directory you would like to search:	")
extension = raw_input("\nPlease enter file format you would like to search for:	")

for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith(extension):
			infile = open(os.path.join(root,file), "r")
			data = infile.read()
			hash = hashlib.md5(data).hexdigest()			
			if hash in dictionary:
				dictionary[hash].append(file)
			else:
				
				dictionary[hash] = [file]
for i in dictionary:
	if len(dictionary[i])>1:
		print "\nThe following files have matching MD5 Hashes:\n"
		for x in dictionary[i]:
			print x,
		print "\n"
