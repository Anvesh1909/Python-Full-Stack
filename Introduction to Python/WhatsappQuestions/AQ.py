# 1. Combine the two dictionaries d1={'Eid':1,'Ename':'Ram'} and d2={'Salary':56000.0,'Company':'TCS'} as a single dicrtionay and add the all values to an empty list without using values()&append().


# Combine the two dictionaries

d1={'Eid':1,'Ename':'Ram'}
d2={'Salary':56000.0,'Company':'TCS'}

print("d1 = ",d1)
print("d2 = ",d2)

for k,v in d2.items():
    d1[k]=v

print("combined dict = ",d1)

l = [ d1[i] for i in d1.keys() ]

print("list is = ",l)



# 2. Convert the string "Iam a Angular Developer" into "IAM.a.ANGULAR.developer" within a single line of code.

s = "Iam a Angular Developer"

s = ".".join(s.split())
print(s)  # Iam.a.Angular.Developer



# 3. Show the output as follows by using Slicing to [[["Hi","Iam","a","Django","Developer","in","TCS","Company"]]].
#   Output:
#   'I-DJANGO-dEVELOPER-tcs.com'

l = [[["Hi","Iam","a","Django","Developer","in","TCS","Company"]]]

print(l[0][0][1][0],l[0][0][3].upper(),l[0][0][4].swapcase(),l[0][0][6].lower()+".com",sep="-")
# I-DJANGO-dEVELOPER-tcs.com






# 4. Write a python code to differentiate between '=='&'is' operator,'=='&'in' operator.

l1 = [1,2,3,4]
l2 = [1,2,3,4]

print(l1,l2)
print("l1==l2",l1==l2)
print("l1 is l2",l1 is l2)


print("1 in l2", 1 in l2)
print("5 in l2", 5 in l2)




# 5. Findout the values of A,B,C and guess the output :
#   A=4<<2
#   B=17>>3
#   C=19<<4 and 26>>3
#   print(A and B or C)

A=4<<2
B=17>>3
C=19<<4 and 26>>3
print(A and B or C)
