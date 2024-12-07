v = eval(input("enter any data: "))
print(v)



# sep attribute
d,m,y = 13,11,2024
print("date is")
print(d,m,y,sep="/")
print()

h,m,s = 16,45,40
print("time is")
print(h,m,s,sep=":")
print()

l,t,o = 1,10,101
print("rupees in lakhs")
print(l,t,o,sep=",")
print()



# end attribute
print("multiline contant")
for i in range(1,6):
    print(i)

print()
print("single line contant")
for i in range(1,6):
    print(i,end=" ")


