#  to convert integer to char

x1 = chr(65)
x2 = chr(66)
x3 = chr(67)

y1 = chr(97)
y2 = chr(98)
y3 = chr(99)

print(x1,x2,x3)
print()
print(y1,y2,y3)

#  convert char to int


x1 = ord('a')
x2 = ord('b')
x3 = ord('c')

y1 = ord('A')
y2 = ord('B')
y3 = ord('C')

print(x1,x2,x3)
print()
print(y1,y2,y3)


for i in range(ord('a'),ord('z')+1):
    print(chr(i),end=' ')

print()

for i in range(ord('A'),ord('Z')+1):
    print(chr(i),end=' ')


