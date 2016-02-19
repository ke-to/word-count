# -*- coding: utf-8 -*-

import os
from collections import Counter
import sys, codecs
import csv

fileName = input("Output CSV file name write now! > ")

result = open(fileName, 'w', newline='')
csvWriter = csv.writer(result)
csvWriter.writerow(["count","word"]) 

fileName2 = input("Input TXT file name write now! > ")

container=u""
f = open(fileName2,'r')
for line in f:
	container += line
	#print line
	
print("container in contents.")
Clist = container.split(",")
print("container split is finished.")

counter = Counter(Clist)
for word, cnt in counter.most_common():
	print(type(cnt))
	text = [cnt,word]
	csvWriter.writerow(text) 
	print(text)
	
result.close

print ("COMPLATE")