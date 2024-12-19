# 1> Python Program for Binary To Decimal Conversion ?
def BinToDeci(n):
    res = 0
    p = 0
    while n>0:
        a = n%10
        res+= 2**p * a
        p+=1
        n//=10
    return res

n = int(input("enter binary number : "))
print(BinToDeci(n))


# 2> Python program for octal to decimal conversion ?
def octToDeci(n):
    res = 0
    p = 0
    while n>0:
        a = n%10
        res+= 8**p * a
        p+=1
        n//=10
    return res

n = int(input("enter binary number : "))
print(octToDeci(n))


# 3> Python program for decimal to binary conversion ?
def DeciToBin(n):
    s = ""
    D = ["0","1"]
    while n>0: 
        a = n%2
        s = D[a] + s
        n//=2
    return s

n = int(input("enter number : "))
print(DeciToBin(n))


# 4> Python program to find number of integers which has exactly x divisors? 
def factors(n):
    L = []
    for i in range(1,n+1):
        if n%i==0:
            L+=[i]
    return L
n = int(input("enter number : "))
print(factors(n))


# 5> write a program to replace the character 'e' with the character 's' and
#  the character 's' with character 'e' in the following string list
#    str_lst = ['geeks','for','geeks']

str_lst = ['geeks','for','geeks']
def replaceSE(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] =="s":
            s[i] = "e"
        elif s[i] == "e":
            s[i] = "s"
    return "".join(s)

for i in str_lst:
    print(replaceSE(i))