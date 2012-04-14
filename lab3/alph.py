#!/usr/bin/python
# -*- coding: utf-8 -*- #

alphabet = {u'а':0,u'б':1,u'в':2,u'г':3,u'д':4,u'е':5,u'ж':6,u'з':7,u'и':8,u'й':9,u'к':10,u'л':11,u'м':12,u'н':13,u'о':14,u'п':15,u'р':16,u'с':17,u'т':18,u'у':19,u'ф':20,u'х':21,u'ц':22,u'ч':23,u'ш':24,u'щ':25,u'ъ':26,u'ы':27,u'ь':28,u'э':29,u'ю':30,u'я':31}
m = len(alphabet)
most_frequent = [u'о',u'а',u'е',u'и',u'н']


def alphToCode(letter):
    code = alphabet[letter]
    return code

def codeToAlph(code):
    return [key for key, value in alphabet.items() if code == value][0]