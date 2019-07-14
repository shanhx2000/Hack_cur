import os, re

route = u"/home/jessica/r"
dir = []
dir1 = os.listdir(route)
for i in range(0, len(dir1)):
    dir2 = os.listdir(route+"/"+dir1[i])
    dir.insert(i, [dir1[i], dir2])


tags = []


def search(word, dir1_num):
    if dir1_num < len(dir):
        for dir2s in dir[dir1_num][1]:
            f = open(route + "/" + dir[dir1_num][0] + "/" 
                     + dir2s + "/" + "a.txt", 'r')
            words = f.read()
            if re.search(word, words):
                tags.append(dir2s)
                if dir[dir1_num][0] not in tags:
                    tags.append(dir[dir1_num][0])
        search(word, dir1_num+1)
    else:
        return


search("a", 0)
print(tags)
