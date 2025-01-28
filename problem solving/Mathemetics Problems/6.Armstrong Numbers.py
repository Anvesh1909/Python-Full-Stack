'''
You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

Note: Return true if it is an Armstrong number else return false.

Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. 
Input: n = 372
Output: false
Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. 
Input: n = 100
Output: false
Explanation: 100 is not an Armstrong number since 13 + 03 + 03 = 1. 
Constraints:
100 ≤ n <1000 
'''



'''
n = 153

1*3 + 5*3 + 3*3
= 3 + 125 + 27 
= 153


no of digits 
p = 0 - 1 - 2 - 3

while n>0
n = 153//10 = 15  p+=1
n = 15//10 = 1  p+=1
n = 1//10 = 0 p+=1



each num power digit 
s = 0 - 27 - 152 - 153

n = 153%10 = 3
3**3 = 27  s+=27
n = 153//10  =15

n = 15%10  = 5
5**3 = 125  s+=125
n = 15//10  =1

n = 1%10 = 1
10)1(0
  -0
   _
   1
1**3 = 1 s+= 1
n = 1//10  = 0 

while n>0: 


'''
def armstrongNumber(n):
    p = 0
    temp = n
    while temp>0:
        temp//=10
        p+=1
        
    temp = n
    s = 0
    while temp>0:
        a = temp%10
        s+=a**p
        temp//=10
        
    return n==s
    
    

print(armstrongNumber(153))
print(armstrongNumber(372))
print(armstrongNumber(100))

