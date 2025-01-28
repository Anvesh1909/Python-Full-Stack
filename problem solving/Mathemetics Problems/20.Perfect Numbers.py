'''
Given a number n, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. 

Examples:

Input: n = 6
Output: true 
Explanation: Factors of 6 are 1, 2, 3 and 6. Excluding 6 their sum is 6 which is equal to N itself. So, it's a Perfect Number.
Input: n = 10
Output: false
Explanation: Factors of 10 are 1, 2, 5 and 10. Excluding 10 their sum is 8 which is not equal to N itself. So, it's not a Perfect Number.
Input: n = 11
Output: false
Explanation: Factors of 11 are 1, 11. Excluding 11 their sum is 1 which is not equal to N itself. So, it's not a Perfect Number.
Constraints:
1 <= n <= 109


'''




'''

sum of digit 
n = 514
s = 0
a = n%10 
s+=a
n//=10
'''


def sumOfDigits(n):
    s = 0
    while n>0:
        a = n%10
        s+=a
        n//=10
    return s


'''
n = 8128
sumofdigit(n) = 19
n = 19
sumofdigit(n) = 10
n = 10
sumofdigit(n) = 1

while n>9

'''

def perfectNumber(n):
    while n>9:
        n = sumOfDigits(n)
    return n==1

print(perfectNumber(8128))
print(perfectNumber(1))
print(perfectNumber(154))


print(perfectNumber(16))
print(perfectNumber(1987))
print(perfectNumber(1978))



