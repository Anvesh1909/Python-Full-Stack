# 16:33
a = "anvesh"
if a == 'anvesh':
    print("hello")

b = 20
if b >= 18:
    print("Adult")

if b < 18:
    print("child")


age = 25

if age<18:
    print("child")
if age >=18 or age<= 55:
    print("Adult")
if age > 55:
    print("old age")


speed = 95
if speed >= 100:
    print("over speed finne 1000")

if speed < 100:
    print("safe speed")


a = 10
b = 20

if a> b:
    print("a is greater than b")
 
if a < b:
    print("a is less than b")

if a == b:
    print("a is equal to b")


year = 400

if year%4 == 0:
    if year% 100 == 0:
        if year% 400 != 0:
            print("leap year")


# 16:39

l = [10,20,40,11,34]
n = int(input())

if n in l:
    print("n is present")

if n not in l:
    print("n is not present")


s = "malayalam"

if s==s[::-1]:
    print("palindrome")


if s!=s[::-1]:
    print("not palindrome")

n = 100

if n%2 ==0:
    print("even")

if n%2 != 0:
    print("odd")


# 16:43
n = 200

if 100<n<25000:
    print("N is with  in range of 100 and 25000")


s = 10

if s&(s-1)==0:
    print("s is power of square")

if s&(s-1)!=0:
    print("s is not power of square")



s = "wsnvesh"
if s.startswith("A"):
    print("name starts with A")

if not s.startswith("A"):
    print("Please enter a name starts with A")