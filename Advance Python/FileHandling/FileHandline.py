f = open("append.txt","w")


s = ["HEllo\n","Bunny\n","World!\n"]

f.writelines(s)

f.close()





f = open("append.txt","a+")
f.write("bvedbvuo\n")
print(f.tell())
f.seek(0)
print(f.tell())
res = f.read()
print(res)
f.close()