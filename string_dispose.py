# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def process(textori):
    dictionary = {}
    stopwords = ['、','（','）','，','。','：','“','”',
                '\n\u3000','\u3000','的','‘','’',
                'a','in','also','below','am','is','are','have',
                'the','of',',',' ','and','this','to','be',
                'that','it','was','by']
    output_wr = ""
    for line in textori:
        for word in line:
            if word.isalpha() or word == ' ':
                output_wr = output_wr + word
            elif word == '\n' or word == '_':
                output_wr = output_wr + ', '
            else:
                output_wr = output_wr + ' '

    text = output_wr
    
    fredist = nltk.FreqDist(text.split(' '))
    
    print(fredist)
    
    for localkey in fredist.keys(): # 所有词频合并。 如果存在词频相加，否则添加
        if localkey in stopwords: # 检查是否为停用词
            continue
        if localkey in dictionary.keys(): # 检查当前词频是否在字典中存在
            dictionary[localkey] = dictionary[localkey] + fredist[localkey] # 如果存在，将词频累加，并更新字典值
        else: # 如果字典中不存在
            dictionary[localkey] = fredist[localkey] # 将当前词频添加到字典中
    
    words = []
    for word in dictionary:
         tt = ()
         tmp_list = [word,dictionary[word]]
         
         tt = tuple(tmp_list)
         if word not in stopwords:
             words.append(tt)

    tmp = sorted(words,key=lambda x:x[1],reverse=True)
    output = []
    for i in range(min([4,len(tmp)])):
        output.append(tmp[i][0])
    return output
