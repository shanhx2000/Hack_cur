from flask import Flask, session, redirect, url_for, escape, request, render_template
from data import data, profile

app = Flask(__name__)
mydata = profile()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<tag>')
def loadtag(tag):
    mydata.add_auto('CYJ is fake, CYJ is strong, CYJ is human, CYJ sits besides me.')

    return render_template('tags.html',tag_list=mydata.taglist, tag=tag, data_list=mydata.Find(tag),length=len(mydata.Find(tag)))

if(__name__=='__main__'):
    app.run()