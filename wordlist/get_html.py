# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:03:49 2019

@author: shanhx
"""


#链接的正则表达式，注意是在标签中的href属性里的才是真正的链接

PATTERN_URl = "<a.*href=\"(https?://.*?)[\"|\'].*"

import requests

#获取网页源代码，注意使用requests时访问https会有SSL验证，需要在get方法时关闭验证

def getHtml(url):

    res = requests.get(url,verify=False)
    
    text = res.text
    wr = open('source.txt', 'w', encoding='UTF-8')
    wr.write(text)
    return text

#有时还是会有警告，可以采用以下方式禁用警告

#import urllib3

#urllib3.disable_warnings()

 

#获取指定页面中含有的url

def getPageUrl(url,html=None):

    if html == None:

        html = getHtml(url)

    uList = re.findall(PATTERN_URl, html)

    return uList


getHtml("https://myvocabulary.com/word-list/automotive-repair-vocabulary/")