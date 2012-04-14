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
rus_text = "TEXT1"
temp = "temp.txt"

if len(sys.argv)==3:
	file_in = sys.argv[1]
	file_out = sys.argv[2]
else:
	print "usage "+ sys.argv[0] +" <input file name> <output file name>"

most_used = [u'ст',u'но',u'то',u'на',u'ен']
m = 31
alph = {u'а':0,u'б':1,u'в':2,u'г':3,u'д':4,u'е':5,u'ж':6,u'з':7,u'и':8,u'й':9,u'к':10,u'л':11,u'м':12,u'н':13,u'о':14,u'п':15,u'р':16,u'с':17,u'т':18,u'у':19,u'ф':20,u'х':21,u'ц':22,u'ч':23,u'ш':24,u'щ':25,u'ь':26,u'ы':27,u'э':28,u'ю':29,u'я':30}

cypher_bi = bigrams(file_in)
most_frequed_bi = sorted(cypher_bi.iteritems(), key = operator.itemgetter(1))[-9:]
least_bi = sorted(bigrams(rus_text).iteritems(), key = operator.itemgetter(1))[:15]

def readable(filename):
    desh_freq = sorted(bigrams(filename).iteritems(), key = operator.itemgetter(1))[-3:]
    it = 2
    for i in range(0,len(desh_freq)):
	for j in range(0,len(most_used)):
	    if most_used[j] == desh_freq[i][0]:
		it -= 1
    if it <= 0 : return True
    return False
    
def readable_neg(filename):
    less_voc_desh = sorted(bigrams(filename).iteritems(), key = operator.itemgetter(1))[:10]
    it = 0
    for i in range(0,len(less_voc_desh)):
	for j in range(0,len(least_bi)):
	    if least_bi[j][0] == less_voc_desh[i][0]:
		it -= 1
    if it <= 0:
	return True
    return False

def a_key(x1,x2,y1,y2):
	a=[]
	x1,x2,y1,y2 = map(get_code,[x1,x2,y1,y2])
	#print x1,x2,y1,y2
	xx = (x1-x2) % (m*m)
	yy = (y1-y2) % (m*m)
	#print xx, yy
	d = euclid(xx,m*m)[0]
	#print d
	if d == 1:
		a.append(euclid(m*m,xx)[2]*yy % (m*m))
		return a
	if yy % d != 0 or d == m*m:
		return []
	if yy % d == 0:
		a.append(euclid(m*m/d,(xx)/d)[2]*(yy)/d % (m*m)/d)
        for i in range(1,d-1):
	    	a.append(a[i-1] + (m*m)/d)
        return a
def b_key(x1,y1,a):
	x1, y1 = map(get_code,[x1,y1])
	return (y1-(a*x1)) % (m*m)

def euclid(a, b):
	if (b==0):
		return a, 1, 0
	d, x, y = euclid(b,a%b)
	return d, y, x - a/b*y

def get_code(bi):
	return (alph[bi[0]])*m + alph[bi[1]]

def decodeChar(code):
	return get_alp_key(code / m) + get_alp_key(code % m)

def get_alp_key(val):
    return [key for key, value in alph.iteritems() if value == val][0]

def decode(filename,a,b):
	text = codecs.open(filename,'r','utf-8')
	f = codecs.open(temp, 'w','utf-8')
	for line in text.readlines():
		for i in range(0,len(line.strip())-1):
			if i % 2 == 0:
				Y = get_code(line[i]+line[i+1])
				X = euclid(m*m,a)[2]*(Y-b) % (m*m)
				f.write(decodeChar(X))
	f.close()
	text.close()

def run():
	for X in range(0,len(most_used)):
		for XX in range(X+1,len(most_used)):
			for Y in range(0,len(most_frequed_bi)):
				for YY in range(0,len(most_frequed_bi)):
					 if Y!=YY : 
					     a_array = a_key(most_used[X],most_used[XX],most_frequed_bi[Y][0],most_frequed_bi[YY][0])
					     for a in a_array:
					 	    b = b_key(most_used[X],most_frequed_bi[Y][0],a)
					     if a % m != 0:
					 	    decode(file_in,a,b)
					 	    if readable(temp) and readable_neg(temp):
					 		    print "%s a = %s b = %s" % (codecs.open(temp, 'r', 'utf-8').readlines()[0][:30], a, b)


run()