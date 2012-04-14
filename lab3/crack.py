#!/usr/bin/python
# -*- coding: utf-8 -*- #

import os,sys
import codecs
import operator
import alph

#Read text from source file
def fileRead(filename):
    f = codecs.open(filename,'r','utf-8')
    text = f.read()
    f.close()
    return text

#Kronecker delta
def kronecker(a,b):
    if a==b:
        return 1
    else:
        return 0

#counts Dj
def calcD(text,j,n):
    d = 0
    for i in range(n):
        d += kronecker(alph.alphToCode(text[i]),alph.alphToCode(text[(i+j)%n]))
    if d > 300:
        print "j = %d D = %d ||" % (j,d)

#make blocks of text
def makeBlocks(text,n,r):
    blocks = []
    for i in range(r):
        blocks.append([])
    for i in range(n):
        blocks[i%r].append(text[i])
    return blocks

# Find k
def findK(x,y):
    return (y-x) % alph.m

def decryptBlock(block):
    letters = {}
    for i in block:
        if letters.has_key(i):
            letters[i] +=1
        else:
            letters[i] = 1
    y = alph.alphToCode(sorted(letters.items(), key = operator.itemgetter(1))[-1:][0][0])
    x = alph.alphToCode(alph.most_frequent[0])
    k = findK(x,y)
    decryptedBlock = []
    for i in block:
        yCode = alph.alphToCode(i)
        letter = (yCode - k) % alph.m
        decryptedBlock.append(alph.codeToAlph(letter))
    return (decryptedBlock, alph.codeToAlph(k))

def dec(key,text):
    newText =''
    for i in range(len(text)):
        x = (alph.alphToCode(text[i]) - alph.alphToCode(key[i % 17])) % alph.m
        newText += alph.codeToAlph(x)
    return newText

def main():
    input_file = ''
    cracked_file = ''
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        cracked_file = sys.argv[2]
    else:
        print "Usage: %s <input filename> <enciphered filename>" % sys.argv[0]
        sys.exit(0)
    enc = fileRead(input_file)
    n = len(enc)
    #for i in range(n):
    #   calcD(enc,i,n)

    r = 17
    blocks = makeBlocks(enc,n,r)
    key = ''
    decBlocks = []
    for block in blocks:
        decrypted, k = decryptBlock(block)
        decBlocks.append(decrypted)
        key +=k

    plainText = ''
    i=0
    for j in range(len(decBlocks[0])):
        for block in decBlocks:
            if(i>len(block)-1):
                continue
            else:
                plainText +=block[i]
        i += 1
    #print plainText

    myKey = u'возвращениеджинна'
    text = dec(myKey,enc)
    print text
    print "key %s" % myKey
    f = codecs.open(cracked_file,'w','utf-8')
    f.write(text)
    f.close
if __name__ == "__main__":
    main()