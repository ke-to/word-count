# -*- coding: utf-8 -*- 

import os
import requests
from collections import Counter
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

fileName = raw_input("Input CSV file name write now! > ")

result = open(fileName, 'w')
result.write('')

container=u""
f = open('/Users/kojimakeito/Desktop/result2.txt','r')
for line in f:
	container += line.decode('utf-8')
	print line
	
print "container in contents"

counter = Counter(container)
for word, cnt in counter.most_common():
	#print type(word)
	text = word
	result.writelines(text)
	print text
	
result.close

print "COMPLATE"