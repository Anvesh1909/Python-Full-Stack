s = "My name is anvesh"

print(s.upper())
print(s.lower())
print(s.title())

i = s.index("anvesh")

print(s[i:])

# print(s.index('z'))

s = "my name is anvesh and my age is 21"

s = s.replace('21','22')
print(s)

s = "my name is anvesh and my age is 21"

s = s.split(" ")
print(s)


s = "my-name-is-anvesh-and-my-age-is-21"
s = s.split('-')
print(s)



name = 'anvesh'
age = 22

print("my name is",name,'my age is',age)

print(f"my name is {name} my age is {age}")
print("my name is {} my age is {}".format(name,age))

