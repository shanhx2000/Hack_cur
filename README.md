# The Hack 2019 召集假人精灵元素极壁

## Description
>Intro: This is an intelligent knowledge management system.  
>Members: Chen Yanjun, Shan Haoxuan, Wang Hanyu, Yang Jiamin. 

## Guide

### Install MongoDB
1. Install pymongo from:  
```
    $ pip install pymongo
```
2. Download MongoDB from:  
(i). For windows server :  https://www.mongodb.com/download-center  
(ii). For linux server :  

Download by wget:  
```
    $ mkdir -p /home/tools
    $ cd /home/tools
    $ wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.2.tgz
```
Then add the path:
```
    $ export PATH=/home/tools/mongodb/bin:$PATH
```

### Initialize the database:
```
    $ mkdir -p /data/db
    $ mongod --dbpath /data/db
```

## Run server program
For the server mode, starting the progarm with:
```
    $ mongod --dbpath /data/db
    $ python app.py
```

## Related Functions

### >string_dispose.py
`process(string)`: Return the list of high frequence words.  

### >app.py
`app.route('/')`: Show the index interface.  
`app.route('/<tag>')`: Show the inside interface.

### >data.py
#### >>class profile
`__init__`: connect to the MongoClient 'mongodb://localhost:27017/' and clear the original files.  
`add(dictionay)`: add the dictionary to the database.  
`add_auto(string)`: autometically add the context to the database.  
`Find(string)`: Return the list of records with given tag.  

#### >>class data
`__init__`: create a piece of new data  
`tolist`: convert the data in to a list  
`todict`: convert the data in to a dictionary  

## Structure
>Hack_cur  
>&emsp;&emsp;|--templates  
>&emsp;&emsp;&emsp;&emsp;|--index.html  
>&emsp;&emsp;&emsp;&emsp;|--inside.html    
>&emsp;&emsp;|--static  
>&emsp;&emsp;|--data  
>&emsp;&emsp;&emsp;&emsp;|--db  
>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--data  
>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--stopwords  
>&emsp;&emsp;|--app.py  
>&emsp;&emsp;|--data.py  
>&emsp;&emsp;|--process.py  
>&emsp;&emsp;|--plugin  
