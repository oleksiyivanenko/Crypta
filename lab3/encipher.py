#!/usr/bin/python
# -*- coding: utf-8 -*- #

import sys,os
import codecs
import alph

#Read text from source file
def fileRead(filename):
    f = codecs.open(filename,'r','utf-8')
    text = f.read()
    f.close()
    return text

#Clear text from punctuation and convert to lover case
def clearText(text):
    text = text.lower()
    clean = ''
    for i in text:
        if i.isalpha():
            if i == u'ё':
                clean += u'е'
            elif i == u'ъ':
                clean += u'ь'
            else:
                clean += i
    return clean

#Encipher text
def encipherText(text,key):
    r = len(key)
    lst = []
    for i in range(len(text)):
        lst.append((alph.alphToCode(text[i])+alph.alphToCode(key[i%r]))%alph.m)
    enciphered = ''
    for i in lst:
        enciphered += alph.codeToAlph(i)
    return enciphered

#Save ensiphered text to file
def writeToFile(text,filename):
    f = codecs.open(filename,'w','utf-8')
    f.write(text)
    f.close()

def main():
    input_file = ''
    enciphered_file = ''
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        enciphered_file = sys.argv[2]
    else:
        print "Usage: %s <input filename> <enciphered filename>" % sys.argv[0]
        sys.exit(0)
    print 'Please enter key word:'
    key = unicode(sys.stdin.readline(), 'utf-8')
    key = key.strip()
    text = fileRead(input_file)
    clean = clearText(text)
    enc = encipherText(clean,key)
    writeToFile(enc,enciphered_file)

if __name__ == "__main__":
    main()