from flask import Flask, session, redirect, url_for, escape, request, render_template
from pymongo import MongoClient
from data import data,tolist

myclient = MongoClient('mongodb://localhost:27017/')
mydb = myclient['db']
mytags = mydb['tag_list']
mydata = mydb['data_list']

x = mydata.insert_one(data('Chen Yanjun','He is a fake man.','2019.7.13','fake').todict());
x = mydata.insert_one(data('Shan Haoxuan','He is tired.','2019.7.13','tired').todict());
taglist = ['fake','tired','C++','python','html']

app = Flask(__name__)

def Find(database):
    ret = []
    for x in mydata.find():
        ret.append(tolist(x))
    return ret

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<tag>')
def loadtag(tag):
    return render_template('inside.html',tag_list=taglist, tag=tag, data_list=Find(mydata))

#if(__name__=='__main__'):
#    app.run()