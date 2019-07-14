from pymongo import MongoClient
from string_dispose_new import process
import time

class profile:
    def __init__(self):
        myclient = MongoClient('mongodb://localhost:27017/')
        mydatabase = myclient['db']
        mydata = mydatabase['data_list']
        mydata.delete_many({})
        self.file = mydata
        self.taglist = ['fake']
        self.badtag = [' ','is','and','to','are','?',',','.','if','what','where','when']
    
    def add(self,dict):
        for tag in dict['tags']:
            if(tag not in self.taglist and tag not in self.badtag):
                self.taglist.append(tag)
        if self.file.find({'content':dict['content']}):
            self.file.insert_one(dict)

    def add_auto(self,text):
        dict = data()
        dict.title = process(text)[0]
        dict.content = text
        dict.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dict.tags = process(text)
        self.add(dict.todict())

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
    
