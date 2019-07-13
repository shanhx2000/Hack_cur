class data:
    def __init__(self,title,content,time,tags):
        self.title = title
        self.content = content
        self.time = time
        self.tags = tags
    def tolist(self):
        return [self.title,self.content,self.time,self.tags]
    def todict(self):
        return {'title':self.title, 'content':self.content,'time':self.time,'tags':self.tags}
        
def tolist(x):
        return [x['title'],x['content'],x['time'],x['tags']]
    
