'''
Given a number n. Return true if the digit sum(or sum of digits) of n is a Palindrome number otherwise false.

A Palindrome number is a number that stays the same when reversed

Examples:

Input: n = 56
Output: true
Explanation: The digit sum of 56 is 5+6 = 11. Since, 11 is a palindrome number.Thus, answer is true.
Input: n = 98
Output: false
Explanation: The digit sum of 98 is 9+8 = 17. Since 17 is not a palindrome,thus, answer is false.
Constraints:
1 <= n <= 10^9
'''


n = 153

'''
s = 0 - 3 - 8 - 9
n = 153
n%10 = 3  s+= 3
n//10 = 15

n%10 = 5 s+=5
n//10 = 1

n%10 = 1 s+=1 
n%10 = 0

while n>0:
'''
def sumOfDigit(n):
    s = 0
    while n>0:
        a = n%10
        s+=a
        n//=10
    return s

# print(sumOfDigit(1542))

'''
rn = 0  - 3  - 35 - 351
n = 153

n%10 = 3  rn= rn*10 + 3
n//=10 = 15

n%10 = 5  rn = rn*10 + 5
n//=10 = 1

n%10 = 1 rn = rn*10 + 1
n//10 = 0
while n>0

n == rn
'''
def palindromeNumber(n):
    temp = n
    rn = 0
    while temp>0:
        a = temp%10
        rn = rn*10 + a
        temp//=10
    return n==rn
# print(palindromeNumber(153))



def SumOfDigitIsPalindromeOrNot(n):
    s = sumOfDigit(n)
    return palindromeNumber(s)

print(SumOfDigitIsPalindromeOrNot(56))
print(SumOfDigitIsPalindromeOrNot(98))
print(SumOfDigitIsPalindromeOrNot(151))
print(SumOfDigitIsPalindromeOrNot(72))


