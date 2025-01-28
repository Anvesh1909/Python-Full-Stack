f = open("FileHandling/abc.txt","r")
print("File name : ",f.name)
print("File mode : ",f.mode)
print("File closed : ",f.closed)
print("File readable() : ",f.readable())
print("File writable() : ",f.writable())
f.close()
print("File closed : ",f.closed)







f = open("FileHandling/abc.txt","r+")
print("File name : ",f.name)
print("File mode : ",f.mode)
print("File closed : ",f.closed)
print("File readable() : ",f.readable())
print("File writable() : ",f.writable())
f.close()
print("File closed : ",f.closed)







f = open("FileHandling/abc.txt","w")
print("File name : ",f.name)
print("File mode : ",f.mode)
print("File closed : ",f.closed)
print("File readable() : ",f.readable())
print("File writable() : ",f.writable())
f.close()
print("File closed : ",f.closed)







f = open("FileHandling/abc.txt","w+")
print("File name : ",f.name)
print("File mode : ",f.mode)
print("File closed : ",f.closed)
print("File readable() : ",f.readable())
print("File writable() : ",f.writable())
f.close()
print("File closed : ",f.closed)









f = open("FileHandling/abc.txt","w")
f.write("ABC\n")
f.write("DEF\n")
f.write("GHI\n")
print("content changed")
f.close()



f = open("FileHandling/abc.txt","w")
f.write("123\n")
f.write("456\n")
f.write("789\n")
print("Existing data removed and new data inserted")
f.close()





f = open("FileHandling/abc.txt","a")
f.write("123\n")
f.write("456\n")
f.write("789\n")
print("content added without changing the existing data")
f.close()



# FileExistsError: [Errno 17] File exists: 'FileHandling/abc.txt'
try:
    f = open("FileHandling/abc.txt","x")
    f.write("123\n")
    f.write("456\n")
    f.write("789\n")
    print("Existing data removed and new data inserted")
    f.close()
except FileExistsError as e:
    print(e)





try:
    f = open("FileHandling/xyz.txt","x")
    f.write("123\n")
    f.write("456\n")
    f.write("789\n")
    print("Existing data removed and new data inserted")
    f.close()
except FileExistsError as e:
    print(e)









f = open("FileHandling/abc.txt","a")
f.write("123\n")
f.write("456\n")
f.write("789\n")
print("content added without changing the existing data")
f.close()









f = open("FileHandling/abc.txt","w")
l1 = ["101\n","Anvesh\n","30000.00\n","Software developer\n","Hello\n"]
l2 = ["102\n","Anvesh2\n","30001.00\n","Software developer2\n","Hello\n"]

f.writelines(l1)
f.writelines(l2)
print("content changed")
f.close()









f = open("FileHandling/abc.txt")

res = f.read()
print("file name is :",f.name)
print("----------------------")
print(res)

f.close()





f = open("FileHandling/abc.txt")

res = f.read(20)
print("file name is :",f.name)
print("----------------------")
print(res)

f.close()







f = open("FileHandling/abc.txt")

res = f.readline()
print("file name is :",f.name)
print("----------------------")
print(res)

f.close()








f = open("FileHandling/abc.txt")

res = f.readlines()
print("file name is :",f.name)
print("----------------------")
# print(res)
# for i in res:
#     print(i)
# for i in res:
#     print(i,end="")
for i in res:
    print(i[:-1])


f.close()





f = open("FileHandling/abc.txt")

print("file name is :",f.name)
print("----------------------")
for i in f:
    print(i)

f.close()






# tell and seek
f = open("abc.txt","r")
pos = f.tell()
print("Current position of the file pointer: ",pos)
res = f.read(4)
print(res)
pos = f.tell()
print("Current position of the file pointer: ",pos)
f.close()






f = open("abc.txt","r")
pos = f.tell()
print("Current position of the file pointer: ",pos)

f.seek(7)
pos = f.tell()
print("Current position of the file pointer: ",pos)

f.seek(0)
pos = f.tell()
print("Current position of the file pointer: ",pos)

f.close()








with open("abc.txt","r") as f:
    print("====file information====")
    print("File name : ",f.name)
    print("File mode : ",f.mode)
    print("File closed : ",f.closed)
    print("File readable() : ",f.readable())
    print("File writable() : ",f.writable())
print("=======================")
print("After with block")
print("File closed : ",f.closed)




