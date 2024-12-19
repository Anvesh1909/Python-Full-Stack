# 1> create a function that takes parameter as a string to display the count of characters that 
# how many times repeated in the string "software engineer".
# input:- software engineer
# output:- {'s': 1, 'o': 1, 'f': 1, 't': 1, 'w': 1, 'a': 1, 'r': 2, 'e': 4, ' ': 1, 'n': 2, 'g': 1, 'i': 1}

s = "software engineer"

def CountString(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    print(d)

CountString(s)




# 2> explain the difference between for loop and while loop ? and print the following pattern
#            ****
#             ****
#              ****
#               ****

n = 4 

for i in range(n):
    print(" "*i,end="")
    for j in range(n):
        print("*",end="")
    print()

n=4
i = 0 
while i<n:
    print(" "*i,end="")
    print("*"*n)
    i+=1


# 3> print the following pattern by using for loop and while loop ?
# 0 - 11111
# 1 - 22222
# 2 - 33333
# 3 - 44444
# 4 - 55555
# 5 - 66666

n = 5
for i in range(n):
    print(i,"-",end=" ")
    for j in range(n):
        print(i+1,end="")
    print()


# 4> write a code to check whether the given string is palindrome or not w/o using built-in functions?

s = input("Enter a string : ")
i = 0
j = len(s)-1
while i<j:
    if s[i]!=s[j]:
        print(s,"Not a palindrome")
        break
    i+=1
    j-=1
else:
    print("It is a palindrome")



# 5> write a code to check whether the given number is palindrome or not w/o using built-in functions?

n = int(input("Enter a number : "))
temp = n
place = 1
while temp>9:
    temp //= 10
    place *= 10

rn = 0
temp = n
while temp>0:
    rn += (temp%10)*place
    temp //= 10
    place //= 10

if n == rn:
    print(n,rn,"Number is palindrome")
else:
    print(n,rn,"is not a palindrome")





n = int(input("Enter a number : "))

NoOfDigits = 0 
temp = n
while temp>0:
    temp //= 10
    NoOfDigits += 1

rn = 0
temp = n

# while NoOfDigits != 0:
#     rn = rn*10 + temp%10
#     temp //= 10
#     NoOfDigits -=1

for i in range(NoOfDigits):
    rn = rn*10 + temp%10
    temp //= 10

print(rn)

