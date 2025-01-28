import re

res = re.finditer("ABC","ABCUCBNEUBUABCUIECBNUABABC")

for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    
print(res)    
    

import re

res = re.finditer("ABC","ABCUCBNEUBUABCUIECBNUABABC")

c = 0
for i in res:
    c+=1
print(f"ABC {c} times")    
    
    
    
    
# charecter class

import re

res = re.finditer("[ABC]","ABCUCBNEUBUABCUIECBNUABABC")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)    


import re

res = re.finditer("[A-Z]","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)  


import re

res = re.finditer("[^A-Z]","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)


import re

res = re.finditer("[a-z]","ABCUCBNEUBUABCUIECBNUABABCabcs")

c = 0
for i in res:
    c+=1
print(f"ABC {c} times")  




import re

res = re.finditer("[0-9]","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    c+=1
print(f"ABC {c} times") 


import re

res = re.finditer("[a-zA-Z]","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    c+=1
print(f"ABC {c} times") 


import re

res = re.finditer("[a-zA-Z0-9]","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    c+=1
print(f"ABC {c} times") 




import re

res = re.finditer("[^a-zA-Z0-9]","ABCU CBNEU@# 18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    c+=1
print(f"ABC {c} times") 








import re

res = re.finditer("\S","ABCUCB   NEU@#18383**&&#BUABCUIECBNUABABCabcs")
print(type(res))
c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)



import re

res = re.finditer("\s","ABCUCBN   EU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)


import re

res = re.finditer("\D","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)



import re

res = re.finditer("\d","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)





import re

res = re.finditer("\W","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)





import re

res = re.finditer("\w","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)




import re

res = re.finditer(".","ABCUCBNEU@#18383**&&#BUABCUIECBNUABABCabcs")

c = 0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)









