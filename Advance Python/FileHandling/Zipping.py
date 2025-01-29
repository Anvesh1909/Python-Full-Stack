# zipping
from zipfile import *

f = ZipFile("zippedFile.zip","a",ZIP_DEFLATED)
f.write("abc.txt")
f.write("ccssvv.txt")
f.write("xyz.txt")
print("Zip Folder created successfully")
f.close()





# unzipping
from zipfile import *

f = ZipFile("zippedFile.zip","r",ZIP_STORED)
res = f.namelist()
print(res)
for i in res:
    f2 = open(i,"r")
    obj = f2.read()
    print(obj)
    print("---------------------")
f.close()