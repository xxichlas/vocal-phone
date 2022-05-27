from ast import Str
import os
import uuid

path = 'U'

files = os.listdir(path)

for file in files:
    os.rename(os.path.join(path,file), 'U.'+str(uuid.uuid1())+'.jpg')
