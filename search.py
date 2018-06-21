#!/bin/python
#this program will request a directory to search and a file extension type to search for
#will then walk the directory and its subdirectories and list all files that have the same size, side by side.

import os

dictionary = {}

path = raw_input("Please enter the full path name of the directory you would like to search: ")
extension = raw_input("Please enter file format you would like to search for: ")

for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith(extension):
			size = os.path.getsize(os.path.join(root,file))	
			if size not in dictionary:
				dictionary[size] = [os.path.join(root,file)]
			else: 
				dictionary[size].append(os.path.join(root,file))
for i in dictionary:
	if len(dictionary[i])>1:
		for x in dictionary[i]:
			print x,
