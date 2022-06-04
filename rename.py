from ast import Str
import os
import uuid

path = 'O'

files = os.listdir(path)

for file in files:
    os.rename(os.path.join(path,file), 'O.'+str(uuid.uuid1())+'.jpg')
