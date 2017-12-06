"""
A dumb script which gives a sorted list of items at element zero of a large text file 
"""

import sys 
import os

#open the file with the raw list of access points
f = open(os.path.join('\MyDocuments\Python Scripts','list of access points'), "r")
#opens a blank document - will write to it later. 
f2 = open(os.path.join('\MyDocuments\Python Scripts','fixed list'), "w")
#opens a blank document - will write to it later. 
f3 = open(os.path.join('\MyDocuments\Python Scripts','fresh-list'), "w")
"""
creates two empty lists, just use these to tempoarily store data later in the program.
"""
list_p1 = []
list_p2 = []

"""
iterates through each line in the file 'f', for each iteration, append that line
to the list. 
what you end up is a list where each element is an individual line from the text doc. 
"""
for x in f:
    list_p1.append(x)

""" again - iterates through each element in the list_p1. And then split each 
line, so then each word is it's own element in a list. 
Only write element zero to the text file f2 and then put a new line after each write. 
"""
for x in list_p1: 
	 #list_p2.append(x.split(" ")[0])
	 f2.write(x.split(" ")[0]+ " \n")

#close these text files 
f.close()
f2.close() 

"""
This is some code I stole from stackoverflow. 
It sorts the data that was in "fixed list" and writes the sorted 
lines to another text file called "fresh-list".
"""
with open(os.path.join('\MyDocuments\Python Scripts','fixed list'), "r+") as r:
    for line in sorted(r):
        print(line, end='', file = f3)

#closes the f3 file. 
f3.close()