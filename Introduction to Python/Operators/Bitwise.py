a = 10
b = 8
print(a&b)
print(a|b)
print(a^b)
print(~a,~b)

print("a = ", a)
print("binary number of a :",bin(a))
print("octal number of a  :",oct(a))
print("Hexa decimal of a  :",hex(a))


a = 0b1010
print("a in binary", a)
print(int(a))
print(oct(a))
print(hex(a))

a = 0o712
print("a in octal",a)
print(int(a))
print(bin(a))
print(hex(a))

a = 0x12a
print("a in hexa decimal", a)
print(int(a))
print(oct(a))
print(bin(a))


a = "101"
print(int(a,2))


