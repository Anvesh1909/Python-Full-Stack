


n = int(input("Enter a number : "))

i = 0
a,b = 0,1
print(a,b,end= " ")
while True:
    if i==n:
        break
    z = a+b
    print(z,end=" ")
    a = b
    b = z
    i+=1



n = []

i = 0
while i<100:
    i+=1    
    if i%5!=0:
        continue
    n.append(i)
print(n)



s = input("Enter a string : ")

i = 0
j = len(s)-1
while i<j:
    if s[i] != s[j]:
        print("It is not a palindrome string")
        break
    i+=1
    j-=1
else:
    print("It is a palindrome string ")




s = input("enter a string : ")
for i in range(0,len(s)):
    if s[i] != s[len(s)-i-1]:
        print("it is not a palindrome")
        break
else:
    print("It is a palindrome")




n = int(input("Enter a prime number : "))

i = 2
while i<n:
    if n%i==0:
        print("it not a prime number")
        break
    i+=1
else:
    print("it is a prime number")





n = int(input("Enter a prime number : "))

i = 2
while i<n:
    if n%i!=0:
        i+=1
        continue
    print("it not a prime number")
    break
else:
    print("it is a prime number")




n = int(input("Enter a number: "))
for i in range(2,int(n**0.5)+1):
    if n%i != 0:
        continue
    print("It is not a prime number")
    break
else:
    print("It is a prime number")














i = 0
while i<20:
    print(i)
    i+=2

i = 0
while i<10:
    if i%2==0:
        print(i)
    i+=1


