import os
import chardet
add=os.getcwd()
def Test2(rootDir):
    name=[]
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        name.append(path)
        if os.path.isdir(path):
            Test2(path)
    for i in name:
        if os.path.isfile(i):
            fr = open(i,'r')
            content=fr.read()
            new=content.decode('GB2312').encode('utf-8')
            fr.close()
            fr=open('i','w')
            fr.write(new)
            fr.close()


Test2(add)
