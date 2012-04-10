#!/usr/bin/python
# -*- coding: utf-8 -*- #

import os,sys
from lab1 import biN, singleN
import operator
import codecs
import math
import random
#-7 4 -4 3 our
#-4 6 -3 3 and

file_in = ""
file_out = ""
rus_text = "TEXT1"
temp = "temp"
if len(sys.argv) == 3:
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    #print "file name is %s " % fn
else:
    print "usage script.py <input file name> <output file name>"

most_use = [u'ст',u'но',u'то',u'на',u'ен']
m = 31
alphabet = {u'а':0,u'б':1,u'в':2,u'г':3,u'д':4,u'е':5,u'ж':6,u'з':7,u'и':8,u'й':9,u'к':10,u'л':11,u'м':12,u'н':13,u'о':14,u'п':15,u'р':16,u'с':17,u'т':18,u'у':19,u'ф':20,u'х':21,u'ц':22,u'ч':23,u'ш':24,u'щ':25,u'ы':26,u'ь':27,u'э':28,u'ю':29,u'я':30}

x = biN(file_in)
most_biN_find = sorted(x.iteritems(), key=operator.itemgetter(1))[-9:]
less_voc = sorted(biN(rus_text).iteritems(), key = operator.itemgetter(1))[:15]

def readable(filename):
    desh_freq = sorted(biN(filename).iteritems(), key = operator.itemgetter(1))[-3:]
    it = 2
    for i in range(0,len(desh_freq)):
	for j in range(0,len(most_use)):
	    if most_use[j] == desh_freq[i][0]:
		it -= 1
    if it <= 0 : return True
    return False
    
def readable_neg(filename):
    less_voc_desh = sorted(biN(filename).iteritems(), key = operator.itemgetter(1))[:10]
    it = 0
    for i in range(0,len(less_voc_desh)):
	for j in range(0,len(less_voc)):
	    if less_voc[j][0] == less_voc_desh[i][0]:
		it -= 1
    if it <= 0:
	return True
    return False
    
def get_alp_key(val):
    return [key for key, value in alphabet.iteritems() if value == val][0]

def a_key(x1,x2,y1,y2):
    a = []
    x1,x2,y1,y2 = map(get_code,[x1,x2,y1,y2])
    xx = (x1 - x2) % (m*m)
    yy = (y1 - y2) % (m*m)
    #print "X1 = %s, X2 = %s, Y1 = %s, Y2 = %s xx = %s yy = %s" % (x1,x2,y1,y2,xx, yy)
    d = extended_euclid(xx,m*m)[0]
    #print d
    if d == 1:
	#print "D=1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        a.append(extended_euclid(m*m,xx)[2]*(yy) % (m*m))
        #print "xx =  %s, yy = %s a1 = %s" % (xx,yy,a[0])
        #print a
        return a
    if (yy) % d != 0 or d == m*m:
        return []
    if (yy) % d == 0 :
        a.append(extended_euclid(m*m/d,(xx)/d)[2]*(yy)/d % (m*m)/d)
        #print "X1 = %s, X2 = %s, Y1 = %s, Y2 = %s a1 = %s" % (x1,x2,y1,y2,a[0])
        for i in range(1,d):
	    a.append(a[i-1] + (m*m)/d)
	#print a
        return a

def b_key(x1,y1,a):
    x1,y1 = map(get_code,[x1,y1])
    b = (y1 - a*x1) % (m*m)
    return b

def de_code_text(filename,a,b):
    text = codecs.open(filename, "r", "utf-8" )
    f = codecs.open(temp, 'w', 'utf-8')
    for line in text.readlines():
        for i in range(0,len(line.strip())-1):
	    if i % 2 == 0 :
	        Y = get_code(line[i]+line[i+1])
	        X = extended_euclid(m*m,a)[2]*(Y-b) % (m*m)
	        f.write(de_code(X))
    f.close()

def get_code(bi):
    return (alphabet[bi[0]])*m+alphabet[bi[1]]

def de_code(code):
    return get_alp_key(code / 31 ) + get_alp_key(code % 31)

def extended_euclid(a, b):
    if (b==0):
        return a, 1, 0
    d, x, y = extended_euclid(b, a % b)
    return d, y, x - a/b*y
def execute():
    ir = 0
    for X in range(0,len(most_use)):
	for XX in range(1,len(most_use)):
	    for Y in range(0, len(most_biN_find)):
		for YY in range(1, len(most_biN_find)):
		    a_array = a_key(most_use[X],most_use[XX],most_biN_find[Y][0],most_biN_find[YY][0])
		    for a in a_array:
			b = b_key(most_use[X],most_biN_find[Y][0],a)
			if a % m != 0:
			    de_code_text(file_in,a,b)
			    if readable(temp) and readable_neg(temp):
				#os.rename(temp,file_out)
				print codecs.open(temp, 'r', 'utf-8').readlines()[0][:20]
				ir+=1
				#return True
    print ir
execute()