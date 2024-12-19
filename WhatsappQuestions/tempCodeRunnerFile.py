
n = int(input("enter a number: "))

L = lambda n : [i for i in range(2,int(n)+1) if n%i==0 ] == []
if L(n) : print(n,": is a prime number")
else : print(n,":is not a prime number")