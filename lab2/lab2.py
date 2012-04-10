#!/usr/bin/python
# -*- coding: utf-8 -*- #

import os,sys
import codecs
import operator
import math

def bigrams(filename):
	bigrams = {}
	text = codecs.open(filename, "r", "utf-8")
	for line in text.readlines():
		line ="%s " % line.strip()
		#print line
		for i in range(0,len(line)-1):
			bi = line[i]+line[i+1]
			if bigrams.has_key(bi): bigrams[bi]+=1
			else: bigrams[bi] = 1
	text.close()
	return bigrams

file_in = ""
file_out = ""
rus_btext = "TEXT1"
temp = "temp.txt"

if len(sys.argv)==3:
	file_in = sys.argv[1]
	file_out = sys.argv[2]
else:
	print "usage "+ sys.argv[0] +" <input file name> <output file name>"

most_used = [u'ст',u'но',u'то',u'на',u'ен']
m = 31
alph = {u'а':0,u'б':1,u'в':2,u'г':3,u'д':4,u'е':5,u'ж':6,u'з':7,u'и':8,u'й':9,u'к':10,u'л':11,u'м':12,u'н':13,u'о':14,u'п':15,u'р':16,u'с':17,u'т':18,u'у':19,u'ф':20,u'х':21,u'ц':22,u'ч':23,u'ш':24,u'щ':25,u'ы':26,u'ь':27,u'э':28,u'ю':29,u'я':30}

bigrams(file_in)
