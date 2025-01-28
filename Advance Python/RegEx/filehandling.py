f1 = open("data.txt","r")
f2 = open("mobileNo.txt","w")

import re

# print(f1)
for i in f1:
    l = re.findall("[+][9][1][-][6-9][0-9]{9}",i)
    for j in l:
        f2.write(j+"\n")
        print(j)

f1.close()
f2.close()