import re

MN = input("Enter the mobile number: ")
# res = re.fullmatch("[6-9]\d{9}",MN)
res = re.fullmatch("[6-9][0-9]{9}",MN)

if res:
    print("Valid mobile Number :",MN)
else:
    print("Invalid mobile Number :",MN)
    
    
    

import re

gmail = input("Enter the mobile number: ")
res = re.fullmatch("\w[A-Za-z0-9]*@gmail[.]com",gmail)

if res:
    print("Valid mobile Number :",gmail)
else:
    print("Invalid mobile Number :",gmail)
    
    
    
    
import re

gmail = input("Enter the mobile number: ")
res = re.fullmatch("\w[A-Za-z0-9]*@(gmail|yahoo|outlook)[.]com",gmail)

if res:
    print("Valid mobile Number :",gmail)
else:
    print("Invalid mobile Number :",gmail)
    



import re

gmail = input("Enter the mobile number: ")
res = re.fullmatch("\w[A-Za-z0-9]*@(gmail|yahoo|outlook)([.]com|[.]com[.]in|[.]org)",gmail)

if res:
    print("Valid mobile Number :",gmail)
else:
    print("Invalid mobile Number :",gmail)
    
    
    
    

import re
# charecter class
res = re.sub("[a-z]","@","aaa111222bbb___3334444")

print(res)



import re
# predefined class
res = re.sub("\d","@","aaa111222bbb___3334444")

print(res)



import re

res = re.sub("[a-z ]","@","aaa 111 222 bbb___ 333 4444")

print(res)


import re

res = re.sub("(\s|\d)","@","aaa 111 222 bbb___ 333 4444")

print(res)



'''
write a python script create a regex object in such a way that
+91-9876543210
9876543210
91-9876543210
919876543210
'''

import re

MN = input("Enter mobile number: ")
res = re.fullmatch("[+]?[9]?[1]?[-]?[6-9][0-9]{9}",MN)
if res:
    print("Indian Phone number")
else:
    print("Not a valid phone number")
    
    
    
    
    
