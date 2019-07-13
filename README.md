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

### Run server program
For the server mode, starting the progarm with:
```
    $ python app.py
```

## Structure
>Hack_cur  
>&emsp;&emsp;|--templates  
>&emsp;&emsp;&emsp;&emsp;|--index.html  
>&emsp;&emsp;&emsp;&emsp;|--inside.html    
>&emsp;&emsp;|--static  
>&emsp;&emsp;|--data  
>&emsp;&emsp;&emsp;&emsp;|--db  
>&emsp;&emsp;|--app.py

