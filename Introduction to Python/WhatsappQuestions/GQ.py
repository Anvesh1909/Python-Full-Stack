# 1> Write a Python function that accepts a string and counts the number of upper 
#    and lower case letters.
#    Sample String : 'The quick Brow Fox'
#    Expected Output :
#    No. of Upper case characters : 3
#    No. of Lower case Characters : 12


s = input("Enter a String : ")
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("No. of Upper case characters :",upper)
print("No. of Lower case Characters :",lower)



# 2> Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#    Sample List : [1,2,3,3,3,3,4,5]
#    Unique List : [1, 2, 3, 4, 5]

L = [1,2,3,3,3,3,4,5]
print("Sample List :",L)

U = []

for i in L:
    if i not in U:
        U += [i]

print("Unique List :",U)



# 3> Write a Python function that takes a number as a parameter and checks whether
#    the number is prime or not.
#    Note : A prime number (or a prime) is a natural number greater than 1 
#           and that has no positive divisors other than 1 and itself.

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input("Enter a number : "))
if isPrime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")



# 4> write a function to check whether the given string is Palindrome or not ?
def palindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

s = input("Enter a String : ")
if palindrome(s):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")


# 5> write a function to take n inputs of student's marks and 
# calculate sum and average of the marks ? define a function for that ?


n = int(input("Enter number of subjects : "))

def sumOfMarks(marks):
    sum = 0
    for i in marks:
        sum+=i
    return sum


def students_marks(n):
    marks = []
    for i in range(n):
        m = int(input(f"Enter marks of {i}: "))
        marks += [m]
    

    return marks

def averageMarks(marks,n):
    total = sumOfMarks(marks)
    return total/n

marks = students_marks(n)
print("sum of marks : ",sumOfMarks(marks))
print("average marks: ",averageMarks(marks,n))
