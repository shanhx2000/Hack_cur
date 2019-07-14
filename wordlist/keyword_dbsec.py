#from pymongo import MongoClient
from urllib.request import urlopen
import re
import os
from bs4 import *
import requests
import urllib3

#Mongo_client = MongoClient("localhost", 27017)

counter_word = 0
url_depth_dic = {}


def crawl_content(url,pos):
    res = requests.get(url, verify=False)
    urllib3.disable_warnings()
    text = res.text
    soup = BeautifulSoup(text, "lxml")
    body = soup.body
    content = str(body.find_all("p"))
    f = re.compile(r'<[^>]+>', re.S)
    par = f.sub('', content)
    #print(par)
    file = open(pos+"/" + "keyword_db.txt", "w",encoding='UTF-8',errors='ignore')
    file.write(par)
    file.close()


def get_name(url):
    res = requests.get(url, verify=False)
    urllib3.disable_warnings()
    soup = BeautifulSoup(res.content, 'lxml')
    name = soup.head.title.string
    return name


def get_href(url):
    #print('#\n')
    res = requests.get(url, verify=False)
    #urllib3.disable_warnings()
    soup = BeautifulSoup(res.content, "lxml")
    a = str(soup.find_all("ul", class_="no-bullet-list"))
    href_pre = re.findall(r'href="/.*"', a)
    ret = []
    for item in href_pre:
        ss = str(item)
        ss = 'https://www.encyclopedia.com' + ss[6:len(ss)-15]
        ret.append(ss)
    #print(ret)
    return ret

def link_for_page(url):
    res = requests.get(url, verify=False)
    urllib3.disable_warnings()
    soup = BeautifulSoup(res.content, "lxml")
    a = []
    a = str(soup.find_all("li", class_="pager__item pager__item--last"))
    if str(a) == '[]':
        return 0
    total_page = int(re.findall(r'[0-9]+', a)[0])
    return total_page

def my_deep_crawl(url,depth,pos):
    #if url_depth_dic[url][0] <= 4:
    web = requests.get(url, verify=False)
    urllib3.disable_warnings()
    if depth > 1:
        name_url = get_name(url)
        ss = str(name_url)
        ss = ss[:ss.find('|')-1]
        ss_c = ""
        for item in ss:
            if item.isalpha():
                ss_c = ss_c + item
        ss = ss_c
        
        nex_ind = pos+'/'+ss
        cur_ind = os.listdir(pos)

        if ss not in cur_ind:
            os.mkdir(nex_ind)
        
        tmp = get_href(url)
        for item in tmp:
            #print(item)
            my_deep_crawl(item, depth-1, nex_ind)
        
    elif depth == 1:
        name_url = get_name(url)
        ss = str(name_url)
        ss = ss[:ss.find('|')-1]
        ss_c = ""
        for item in ss:
            if item.isalpha():
                ss_c = ss_c + item
        ss = ss_c
        
        
        nex_ind = pos+'/'+ss
        cur_ind = os.listdir(pos)

        if ss not in cur_ind:
            os.mkdir(nex_ind)
        
        total_pg = link_for_page(url)
        #print(ss)
        
        cur_url = url
        tmp = get_href(cur_url)
       # print(tmp)
        for item in tmp:
           # print(item)
            my_deep_crawl(item, depth-1, nex_ind)
        
        for i in range(1,total_pg):
            cur_url = url+'?page='+str(i)
            tmp = get_href(cur_url)
            #print(tmp)
            for item in tmp:
                #print(item)
                my_deep_crawl(item, depth-1, nex_ind)

        
    elif depth == 0:
        name_url = get_name(url)
        ss = str(name_url)
        ss = ss[:ss.find('|')-1]
        ss_c = ""
        for item in ss:
            if item.isalpha():
                ss_c = ss_c + item
        ss = ss_c
        
        
        nex_ind = pos+'/'+ss
        cur_ind = os.listdir(pos)
        
        if ss not in cur_ind:
            os.mkdir(nex_ind)
            crawl_content(url,nex_ind)


#u"https://www.encyclopedia.com/earth-and-environment",
qwq_gr = [u"https://www.encyclopedia.com/history",
          u"https://www.encyclopedia.com/literature-and-arts",
          u"https://www.encyclopedia.com/medicine",
          u"https://www.encyclopedia.com/people",
          u"https://www.encyclopedia.com/philosophy-and-religion",
          u"https://www.encyclopedia.com/places",
          u"https://www.encyclopedia.com/plants-and-animals",
          u"https://www.encyclopedia.com/science-and-technology",
          u"https://www.encyclopedia.com/social-sciences-and-law",
          u"https://www.encyclopedia.com/sports-and-everyday-life",
          u"https://www.encyclopedia.com/references"]
for item in qwq_gr:
    url = item
    print(url)
    my_deep_crawl(url,3,os.getcwd())


#url = u"https://www.encyclopedia.com/earth-and-environment"
#my_deep_crawl(url,3,os.getcwd())
