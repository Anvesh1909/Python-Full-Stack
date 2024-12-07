# 1
age = int(input("enter age : "))
if age< 18:
    print(age,"year old : your not eligible")
else:
    print(age,"year old : your eligible")


# 2
marks = eval(input("enter marks list : "))
avg = sum(marks)/len(marks)

if avg <=35:
    print(avg,"% your fail")
else:
    print(avg,"% your pass")


# 3
users = {
    'Anvesh':'1234', 'Surya' : '123' , 'Karthik' : '12' , 'Dheeraj' : '1'
}

username = input("Enter username : ")
password = input("Enter password : ")

if users.get(username) == password:
    print(f'Hello {username} you logged in')
else:
    print('username or password wronge')


# 4
a = int(input("enter angle a : "))
b = int(input("enter angle b : "))

if a+b==90:
    print(a,b,"are complementary angles")
else:
    print(a,b,"are not complementary angles")


# 5
a = int(input("enter side a : "))
b = int(input("enter side b : "))
c = int(input("enter side c : "))

if a+b>c:
    print(a,b,c,"triangle is possible")
else:
    print(a,b,c,"triangle is not possible")


# 6
a = int(input("enter side a : "))
b = int(input("enter side b : "))
c = int(input("enter side c : "))

if a+b>c:
    sides = [a,b,c]
    h = max(sides)
    sides.remove(h)
    if sides[0]**2+sides[1]**2 == h**2:
        print("right angled triangle")
    else:
        print("not a right angled tringle")
else:
    print(a,b,c,"triangle is not possible")
    

# 7
products = { 'bag': 1500, 'book': 259, 'pen': 50, 'charger': 900, 'shirt': 700,
             'laptop': 45000, 'notebook': 120, 'headphones': 2300, 'jacket': 2500, 
             'mouse': 800, 'keyboard': 1500, 'backpack': 1800, 'wallet': 600, 
             'sunglasses': 1200, 'watch': 4000, 'shoes': 3200
            }

search = input("search item: ")

for k,v in products.items():
    if k.startswith(search):
        print(k,v,sep=" : ")


# 8
s = input("enter a string to check palindrome : ")

if s == s[::-1]:
    print(s,"it is a palindrome")
else:
    print(s,s[::-1],"not a palindroms")


# 9
even = []
odd = []

for i in range(1,30):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even: ",even)
print("Odd : ",odd)




# 10
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

prime = []
composite = []

for i in range(2,50):
    if isPrime(i):
        prime.append(i)
    else:
        composite.append(i)

print("prime : ",prime)
print("compo : ",composite)



# 11 abs 
a = int(input("Enter a number to get absulute value : "))
if a < 0:
    print(-(a))
else:
    print(a)

# 12
num = 15
guess = int(input("guess number between 0-20 : "))

if num == guess:
    print("guess is correct :", guess)
else:
    print("plese try again")


# 13
import random
num = random.randrange(1,100)

for i in range(1,11):
    print("guess : ",i)
    guess = int(input("enter a number with in 1-100 : "))
    if num==guess:
        print("You won in guess",i)
        break
    if num > guess:
        print("number is greater than guess",guess)
    else:
        print("number is less than guess",guess)

# 14
Employees = ["Anvesh","surya","bunny","karthik","dheeraj"]

name = input("Enter your name : ")

if name in Employees:
    print("welcome",name )
else:
    print("Your an outsider")



# 15
def isValidIdentifier(s):

    import keyword
    if s in keyword.kwlist:
        return False

    s = list(s)

    if s[0].isnumeric():
        return False


    for i in s:
        if '_' == i:
            continue
        if i.isalnum():
            continue
        return False
    
    return True

identifier = input("Enter name of the identifier : ")
if isValidIdentifier(identifier):
    print("valid identifier",identifier)
else:
    print("Not a valid identifier",identifier)




# 16
d = {}
# 1,2,3,3,3,1,1,2,2,1 
l =  eval(input("Enter a list of items : "))

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print("Count the number of items")
print(d)




# 17
year = int(input("enter year : "))

if ( year%4 ==0 or year% 100== 0 ) and year%400 !=0:
    print(year,": a leap year")
else:
    print(year,": not a leap year")


# 18
