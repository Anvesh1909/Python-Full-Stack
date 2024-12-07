s = input("Enter a string : ")

i = 0
while i< len(s):
    print(i)
    i+=1

i=0
while i<len(s):
    print(s[i])
    i+=1

i=0
while i< len(s):
    print(s[i],"-",i)
    i+=1








i = 1
while i<5:
    print(i)
    j = 1
    while j<5:
        print(j,end=" ")
        j+=1
    print()
    i+=1










# output 1
l1 = eval(input("Enter 1st list : "))
l2 = eval(input("enter 2nd list : "))

i = 0
while i< len(l1):
    print(l1[i])
    j = 0
    while j < len(l2):
        print(l2[j])
        j+=1
    i+=1



# output 2
l1 = eval(input("Enter 1st list : "))
l2 = eval(input("enter 2nd list : "))

i = 0
while i< len(l1):
    j = 0
    while j < len(l2):
        print(l1[i],"--",l2[j])
        j+=1
    print()
    i+=1






# while with else block 
l1 = eval(input("Enter 1st list : "))
l2 = eval(input("enter 2nd list : "))

i = 0
while i< len(l1):
    j = 0
    while j < len(l2):
        print(l1[i],"--",l2[j])
        j+=1
        break
    print()
    i+=1
else:
    print("HEllo")






