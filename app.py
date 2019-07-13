from flask import Flask, session, redirect, url_for, escape, request, render_template
#import pymongo

#myclient = pymongo.MongoClient('mongoodb://localhost:27017/')
#mydb = myclient['db']
#mycol = mydb['name']

#mydict = {'name':'run','alexa':'1000','url':'http://www.runoob.com'}

#x = mycol.insert_one(mydict)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tag_lists=["23","32","$243"])

#if(__name__=='__main__'):
#    app.run()