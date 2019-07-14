# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#with open (file) as f:
 #   for line in f:
  #      do something...

import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


dictionary = {}
force_stopwords = ['、','（','）','，','。','：','“','”',
             '\n\u3000','\u3000','的','‘','’',
             'a','in','also','below','am','is','are','have',
             'the','of',',',' ','and','this','to','be',
             'that','it','was','by']
stopwords=[]

def process(textori):

    #textori = input()
    output_wr = ""
    for line in textori:
        for word in line:
            if word.isalpha() or word == ' ':
                output_wr = output_wr + word.lower()
            elif word == '\n' or word == '_':
                output_wr = output_wr + ' '
            else:
                output_wr = output_wr + ' '
    
    text = output_wr
    
    fredist = nltk.FreqDist(text.split(' ')) # 获取单文件词频
    
    print(fredist)
    
    f_s_w = open('stopwords.txt','r')
    #print(f_s_w)
    for line in f_s_w:
        #print(line)
        stopwords.append(line[:len(line)-1])
    #print(stopwords)
    
    for localkey in fredist.keys(): # 所有词频合并。 如果存在词频相加，否则添加
        if (localkey in stopwords) or (localkey in force_stopwords): # 检查是否为停用词
         #   print('-->停用词：', localkey)
            continue
        if localkey in dictionary.keys(): # 检查当前词频是否在字典中存在
         #   print('--> 重复值：', localkey, dictionary[localkey]+fredist[localkey],fredist[localkey])
            dictionary[localkey] = dictionary[localkey] + fredist[localkey] # 如果存在，将词频累加，并更新字典值
        else: # 如果字典中不存在
            dictionary[localkey] = fredist[localkey] # 将当前词频添加到字典中
        #    print('--> 新增值：', localkey, dictionary[localkey])
    
    words = []
    for word in dictionary:
         tt = ()
         tmp_list = [word,dictionary[word]]
         
         tt = tuple(tmp_list)
         if word not in stopwords:
             words.append(tt)
    #print(words)

    tmp = sorted(words,key=lambda x:x[1],reverse=True)
    #print(tmp)
    output_str = []
    for item in tmp:
        output_str.append(item[0])
    return output_str
    #write_to_file(tmp,cur_dir+'/data/result/'+nam[0]+'_result.txt')
    #print(nam)
    
    
    '''
    '''
    #uf.close()
    '''
    '''
    #    print('===================================================')
     #   print(sorted(dictionary.items(), key = lambda  x:x[1])) # 根据词频字典值排序，并打印

def write_to_file(words, file='results.txt'):
    f = open(file, 'w')
    for item in words:
       # for field in item:
       f.write(str(item[0])+' ')
       f.write(str(item[1]))#+','
       f.write('\n')
    f.close()
