from flask import Flask, session, redirect, url_for, escape, request, render_template

from pymongo import MongoClient
from data import data

myclient = MongoClient('mongodb://localhost:27017/')
mydb = myclient['db']
mytags = mydb['tag_list']
mydata = mydb['data_list']

mydata.delete_many({})
mydata.insert_one(data('Chen Yanjun','He is a fake man.','2019.7.13',['fake','human']).todict())
mydata.insert_one(data('Shan Haoxuan','He is tired.','2019.7.13',['tired','human']).todict())

taglist = ['fake','tired','C++','python','html']

app = Flask(__name__)

def Find(databasem,tagname):
    ret = []
    for x in mydata.find({'tags':tagname}):
        ret.append(x)
    return ret

@app.route('/')
def index():
    return render_template('index.html', tag_list=["23","32","$243"], tag="23")

@app.route('/<tag>')
def loadtag(tag):
    return render_template('tags.html',tag_list=taglist, tag=tag, data_list=Find(mydata,tag), length=7)

if(__name__=='__main__'):
    app.run()