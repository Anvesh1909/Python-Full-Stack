import re

s = input("Enter the pattern: ")
res = re.match(s,"Software Developer")
if res:
    print(s,"pattern is matched")
else:
    print(s,"Pattern is not matched ")
    
    
    
import re

s = input("Enter the pattern: ")
res = re.fullmatch(s,"Software Developer",re.I)
# or re.IGNORECASE
if res:
    print(s,"pattern is matched 100%")
else:
    print(s,"Pattern is not matched")
    

import re
res = re.findall("\d","Anvesh12345@gmail.com")
print(res)
print(type(res))
for i in res:
    print(i)
    
    
import re
res = re.findall("[A-Z]","Anvesh12345@gmail.com")
print(res)
print(type(res))
for i in res:
    print(i)
    


import re
res = re.findall("[a-z]","Anvesh12345@gmail.com")
print(res)
print(type(res))
for i in res:
    print(i)
    
    
    

import re
res = re.findall("[^A-Za-z0-9]","Anvesh12345@gmail.com")
print(res)
print(type(res))
for i in res:
    print(i)
    
    
    
import re

s = input("Enter the pattern: ")
res = re.search(s,"Django",re.I)

if res:
    print(s,"Pattern is matched")
else:
    print(s,"pattern is not matched")




import re

s = input("Enter the pattern: ")
res = re.search("^A",s,re.I)

if res:
    print(s,"Pattern is starting with A|a")
else:
    print(s,"Pattern is starting not with A|a")
    
    
    

import re

s = input("Enter the pattern: ")
res = re.search("A$",s,re.I)

if res:
    print(s,"Pattern is ending with A|a")
else:
    print(s,"Pattern is ending not with A|a")


    


import re 
res = re.sub("\d","*","ABC_abc_12345")
print(type(res))
print(res)


import re 
res = re.sub("[.]","@","ABC_abc_12345......")
print(res)






import re
res = re.subn("\d","@","ABC_abc_12345....@gmail.com")
print(res)





import re
dataSet = "100,101,102,103,104,105,106"
res = re.split(",",dataSet)
print(type(res))
print(res)



import re
data = "www.amazon.com"
res = re.split("[.]",data)
print(type(res))
print(res)