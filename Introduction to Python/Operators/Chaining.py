# atm range limit
n = int(input("Enter amount to widthdraw between(100,25000): "))

if 100<n<25000:
    print(n,"/- amount widthdrawn")
else:
    print("enter amount within range of 100-25000")




# product filter using cost

products = { 'bag': 1500, 'book': 259, 'pen': 50, 'charger': 900, 'shirt': 700,
             'laptop': 45000, 'notebook': 120, 'headphones': 2300, 'jacket': 2500, 
             'mouse': 800, 'keyboard': 1500, 'backpack': 1800, 'wallet': 600, 
             'sunglasses': 1200, 'watch': 4000, 'shoes': 3200
            }

min_range = int(input("enter min range if not -1 : "))
max_range = int(input("Enter max range if not -1 : "))

print("products in range",min_range,max_range,"is")

for k,v in products.items():
    if max_range == -1 and v>= min_range:
        print(k,":",v)
    elif min_range == -1 and v < max_range:
        print(k,":",v)
    # chaining operator
    elif min_range <= v < max_range:
        print(k,":",v)





# simple chaining operator code 

a = int(input("Enter marks of a: "))
b = int(input("Enter marks of b: "))
c = int(input("Enter marks of c : "))


if a<b<c:
    print("1st c , 2nd b , 3rd a")

if a>b>c:
    print("1st a , 2nd b , 3rd c")

if b>a>c:
    print("1st b , 2nd a , 3rd c")

if c>a>b:
    print("1st c , 2nd a , 3rd b")

if a<b>c:
    print("1st b")

if a>b<c:
    print("2nd b")


if a==b==c:
    print("1st a,b,c")

if a==b!=c:
    print("a and b have same marks and c has diffrent")

if a!=b==c:
    print("b and c have same marks and a has diffrent")

if a==c!=b:
    print("a and c have same marks and b has diffrent")


# real world use case


