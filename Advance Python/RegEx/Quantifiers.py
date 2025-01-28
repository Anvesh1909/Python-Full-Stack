import re


s = """
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corrupti dolor, culpa ut possimus exercitationem molestiae corporis rerum officiis! Beatae distinctio ab optio laboriosam nam facilis placeat asperiores? Sapiente, eum voluptate.
"""
res = re.finditer("a",s)
c=0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)


import re
s = """aabcbeikccbiaaaucbneuibiaaacuonueonuaaaaaaa"""
# min one a or more than 1 a
res = re.finditer("a+",s)
c=0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)


import re
s = """aabcbeikccbiaaaucbneuibiaaacuonueonuaaaaaaa"""
# Minimum one A or more than one A with zero number of A's(other than a) and end+1
res = re.finditer("a*",s)
c=0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)




import re
s = """aabcbeikccbiaaaucbneuibiaaacuonueonuaaaaaaa"""
# only A's and Zero number of A's with end+1
res = re.finditer("a?",s)
c=0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)





import re
s = """abcbeikccbiaaaucbneuibiaaacuonueonuaaaaaaa"""
# minimum 2 A's and maximum 4 A's
res = re.finditer("a{2,4}",s)
c=0
for i in res:
    print(i.start(),"--",i.end(),"--",i.group())
    c+=1
print(c)


