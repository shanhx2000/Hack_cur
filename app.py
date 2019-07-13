from flask import Flask, session, redirect, url_for, escape, request, render_template
from data import data, profile

app = Flask(__name__)
mydata = profile()

@app.route('/', methods=['POST', 'GET'])
def indexsearch():
    if request.method == 'POST':
        newtag = request.form['search-key']
        if(newtag not in mydata.taglist):
            mydata.add_auto(newtag)
            return redirect("/" + mydata.taglist[0])
        else:
            return render_template('tags.html',tag_list=mydata.taglist, tag=newtag, data_list=mydata.Find(newtag),length=len(mydata.Find(newtag)))
    else:
        return render_template('index.html')

@app.route('/<tag>', methods=['POST', 'GET'])
def loadnewtag(tag):
    if request.method == 'POST':
        newtag = request.form['search-key']
        return render_template('tags.html',tag_list=mydata.taglist, tag=newtag, data_list=mydata.Find(newtag),length=len(mydata.Find(newtag)))
    else:
        return render_template('tags.html',tag_list=mydata.taglist, tag=tag, data_list=mydata.Find(tag),length=len(mydata.Find(tag)))

if(__name__=='__main__'):
    app.run()