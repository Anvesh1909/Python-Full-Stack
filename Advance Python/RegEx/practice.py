import re

# A -> pattern
# AAAaaaBBBbbbbCCCccc -> string
res = re.findall("A","AAAaaaBBBbbbbCCCccc111222333444555666777888")

print(res)



import re

# \s spaces
res = re.finditer("\s","AAA      aaa BBB bbbb CCC ccc 111 222 333 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)
    




import re

# \S except spaces
res = re.finditer("\S","AAA      aaa BBB bbbb CCC ccc 111 222 333 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)




import re

# \d only digit
res = re.finditer("\d","AAA      aaa BBB bbbb CCC ccc 111 222 333 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)



import re

# \D except digit
res = re.finditer("\D","AAA      aaa BBB bbbb CCC ccc 111 222 333 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)







import re

# pattern -> a 
res = re.finditer("a","AAA      aaa BBB bbbb CCC ccc 111 222 333 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)




import re

# pattern -> a+ min 1 a or more than 1 a
res = re.finditer("a+","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)




import re

# A* -> Minimum one A or more than one A with zero number of A's and end+1
# A* -> no means a " " ,a means no of a's
res = re.finditer("a*","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)

print(len("AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888"))




import re

# A? -> only one A at time and Zero number of A's with end+1
# A? -> no means a " " ,a means a
res = re.finditer("a?","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)




import re

res = re.finditer("a{2,3}","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)



import re


res = re.finditer("a{2}","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)




import re

res = re.search("^A","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")
# print(res)
if res:
    print("True Starts")
else:
    print("False Start")
    
    
    
import re

res = re.search("8$","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")
# print(res)
if res:
    print("True end")
else:
    print("False end")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import re


res = re.finditer("[a-z]+","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)



import re

res = re.finditer("[0-9]+","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555a666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)




import re

res = re.finditer("\S+","AAA      aaa BBB bbbb CCC ccc 111 aa 222 333 a 444555a666777888")

c=0
for i in res:
    print(i.start(),"--",i.end(),"---",i.group())
    c+=1
print(c)