l1 = [1,2,3,4,5]
l2 = [6,7,8,9]

for i,j in zip(l1,l2):
    print(i,j)
    
    
    
d = {
    "name" : 'Anvesh',
    "rollno" : 22,
    "fee" : 200.20,
    "Collage" : "SVIT",
    "Present" : True,
    "Backlogs" : None
}
l1 = [1,2,3,4,5]
l2 = [6,7,8,9]

for k in zip(d,l1,l2):
    print(k,d[k[0]])





