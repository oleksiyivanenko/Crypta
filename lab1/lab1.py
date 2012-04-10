#!/usr/bin/python

import codecs

def readFile():
	f = codecs.open('text','r','utf-8')
	text = f.read()
	f.close()
	return text

def countLeters(text):
	letters = {}
	for items in text:
		letters[items] = 0
		print letters[items]
#		if letters[items] != false:
#			letters[items] +=1
#		else:
#			letters[items] = 1
	print letters
	#a_count = []
	#alpha_count = 0
	#for items in text:
	#	if items.isalpha():
	#		my_ord = ord(items)
	#		k = a_count

def main():
	text = readFile()
	countLeters(text)

if __name__ == '__main__':
	main()