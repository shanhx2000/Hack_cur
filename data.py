from pymongo import MongoClient
from string_dispose import process
import time

class profile:
    def __init__(self):
        myclient = MongoClient('mongodb://localhost:27017/')
        mydatabase = myclient['db']
        mydata = mydatabase['data_list']
        mydata.delete_many({})
        self.file = mydata
        self.taglist = []
    
    def add(self,dict):
        (self.file).insert_one(dict)
        for tag in dict['tags']:
            if(dict.tags not in self.taglist):
                self.taglist.append(tag)

    def add_auto(self,text):
        dict = data()
        dict.title = process(text)[0]
        dict.content = text
        dict.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dict.tags = process(text)
        (self.file).insert_one(dict.todict())
        for tag in dict.tags:
            self.taglist.append(tag)

    def Find(self,tagname):
        ret = []
        for x in (self.file).find({'tags':tagname}):
            ret.append(x)
        return ret

class data:
    def __init__(self,title='',content='',time='',tags=''):
        self.title = title
        self.content = content
        self.time = time
        self.tags = tags
    def tolist(self):
        return [self.title,self.content,self.time,self.tags]
    def todict(self):
        return {'title':self.title, 'content':self.content,'time':self.time,'tags':self.tags}
    
