
# uniary operator
x1 = True
print("X1 = ",x1)

x2 = not x1

print("Uniary operation x2 = ",x2)

# binary operator

x1 = 100
x2 = 200

x3 = x1 + x2
print("Binary operator x1,x2", x3)


# ternary operator

a = eval(input("Enter the value of a : "))
b = eval(input("Enter the value of b : "))

print(a,b)

max_value = a if a > b else b

print(max_value)


a = eval(input("Enter the value of a : "))
b = eval(input("Enter the value of b : "))
c = eval(input("Enter the value of c : "))


print(a,b,c)

max_value = a if a > b and a > c else b if b > c else c

print(max_value)