s = "my name is Anvesh and my age is 21"

print(s)

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

print()

print(s.find('21'))
print(s.index('21'))

print(s.find('z'))
# print(s.index('z'))

# s[33] = '2'



print()

s = s.replace('21','22')

print(s)


print()


s = s.split()

# s[8] = "22"

print(s)
s = " ".join(s)
print(s)


print()

message1 = "         hello how are you"
message2 = """



    good night sweet dreams take care             


"""
message3 = "What are you doing...                   "

print(message1)
print(message2)
print(message3,"String end")

print()

message1 = message1.lstrip()
print(message1)

message2 = message2.strip()
print(message2)

message3 = message3.rstrip()
print(message3,"String end")




name = "anvesh"
age = 22

print("My nane is",name,"and my age is",age)
print(f"My name is {name} and my age is {age}")
print("My name is {} and my age is {}".format(name,age))

message1 = message1.split()

for i in message1:
    print(i)

message1 = " ".join(message1)
print(message1)