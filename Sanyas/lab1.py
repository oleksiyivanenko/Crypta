#!/usr/bin/python
# -*- coding: utf-8 -*- #
import sys
import codecs
import math
"""
if len(sys.argv) == 2:
    fn = sys.argv[1]
    #print "file name is %s " % fn
else:
    print "Starting"
"""
    
    
def singleN(filename):
    alphabet = {}
    text = codecs.open(filename, "r", "utf-8" ) 
    length = 0
    for line in text.readlines():
	for char in line.strip():
	    length += 1
	    if alphabet.has_key(char) : alphabet[char] += 1
	    else : alphabet[char] = 1
    entropia = 0.0
    for key in alphabet:
	p = (alphabet[key]*1.0)/length
	per = 100 * (alphabet[key]*1.0)/length
	entropia += math.log(1.0/p,2)*p
    entropia = entropia
    return alphabet

def biN(filename):
    entropia = 0.0
    length = 0
    bigrams = {}
    text = codecs.open(filename, "r", "utf-8" )
    for line in text.readlines():
	line =" %s " % line.strip()
	for i in range(0,len(line)-1):
	    length += 1
	    #print char
	    bi = line[i]+line[i+1]
	    if bigrams.has_key(bi) : bigrams[bi] += 1
	    else : bigrams[bi] = 1
	length += 1
    sums = 0
    for key in bigrams:
	sums += bigrams[key]
	p = (bigrams[key]*1.0)/length
	per = 100 * (bigrams[key]*1.0)/length
	#print "symbol %s, n=%s, frec=%s, persent=%s " % (key,bigrams[key],round(p,3),round(per,2))
	entropia += math.log(1.0/p,2)*p
    entropia = entropia/2
    return bigrams

def voc_print(voc):
    for key in voc:
	print "key = %s, value =%s" % (key,voc[key])

#voc_print(biN(fn))