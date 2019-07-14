# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:00:05 2019

@author: shanhx
"""

import os
from bs4 import *
import re
path = os.getcwd()
print(path)
htmlfile = open(path+"/source.txt", 'r', encoding='utf-8',errors='ignore')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, "lxml")
title = soup.head.title.string
# print(title)
body = soup.body
content = str(body.find_all("td"))
f = re.compile(r'<[^>]+>', re.S)
par = f.sub('', content)
# print(par)
f_title = open(path+"/title.txt", "w", encoding='utf-8',errors='ignore')
f_title.write(title)
f_title.close()
f_content = open(path+"/content.txt", "w", encoding='utf-8',errors='ignore')
f_content.write(par)
f_content.close()