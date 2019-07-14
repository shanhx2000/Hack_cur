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
stopwords = ['、','（','）','，','。','：','“','”',
             '\n\u3000','\u3000','的','‘','’',
             'a','in','also','below','am','is','are','have',
             'the','of',',',' ']


def process():
    cur_dir = os.getcwd()
    print(cur_dir)
    subdir = os.listdir(cur_dir+'/data/wordcloud/')
    print(subdir)    
    
    for f in subdir: # 遍历文件夹下的文件
        #dictionary = {}
        uf = open(cur_dir+'/data/wordcloud/'+f, 'r',encoding='UTF-8',errors='ignore')
        
        textori = open(cur_dir+'/data/wordcloud/'+f, 'r',encoding='UTF-8',errors='ignore').read() # 读取文本内容
        nam = f.split(".")
        
        wr = open(cur_dir+'/data/rev_getAlpha/'+nam[0]+'_rev.txt', 'w', encoding='UTF-8',errors='ignore')
        output_wr = ""
        #delete unimportant character
        for line in textori:
            for word in line:
                if word.isalpha() or word == ' ':
                    output_wr = output_wr + word
                elif word == '\n' or word == '_':
                    output_wr = output_wr + ', '
                else:
                    output_wr = output_wr + ' '
        
        for word in output_wr:
            wr.write(word)
        wr.close()
        
        print(cur_dir+'/data/wordcloud/'+f)
        
        text = open(cur_dir+'/data/rev_getAlpha/'+nam[0]+'_rev.txt', 'r',encoding='UTF-8',errors='ignore').read() # 读取文本内容
        
        fredist = nltk.FreqDist(text.split(' ')) # 获取单文件词频
        
        print(fredist)
        
        for localkey in fredist.keys(): # 所有词频合并。 如果存在词频相加，否则添加
            if localkey in stopwords: # 检查是否为停用词
                continue
            if(len(localkey)< 3):
                continue
            if not localkey.istitle():
                continue
            
            if localkey in dictionary.keys(): # 检查当前词频是否在字典中存在
             #   print('--> 重复值：', localkey, dictionary[localkey]+fredist[localkey],fredist[localkey])
                dictionary[localkey] = dictionary[localkey] + fredist[localkey] # 如果存在，将词频累加，并更新字典值
            else: # 如果字典中不存在
                dictionary[localkey] = fredist[localkey] # 将当前词频添加到字典中
                print('--> 新增值：', localkey, dictionary[localkey])
            
        words = []
        for word in dictionary:
             tt = ()
             tmp_list = [word,dictionary[word]]
             
             tt = tuple(tmp_list)
             if word not in stopwords:
                 words.append(tt)
        
        tmp = sorted(words,key=lambda x:x[1],reverse=True)
        
        new_folder = cur_dir+'/new'
        os.mkdir(new_folder)
        write_to_file(tmp,new_folder+'/'+nam[0]+'_result.txt')
        uf.close()

def write_to_file(words, file='results.txt'):
    f = open(file, 'w')
    for item in words:
       f.write(str(item[0])+' ')
       f.write(str(item[1]))#+','
       f.write('\n')
    f.close()

process()
