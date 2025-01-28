'''
You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

Examples:

Input: 200
Output: 2
Explanation: By reversing the digits of number, number will change into 2.
Input : 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.
Constraints:
1 <= n <= 106
'''


'''
n = 122
rn = 0 

a = n%10 = 2  
rn*10 + a
n//=10  12

a = n%10 = 2
rn*10+a
n//=10   1

a = n%10  = 1
rn*10+a
n//=10  0

while n>0 
'''

def reverseNumber(n):
    rn = 0
    while n>0:
        a = n%10
        rn = rn*10+a
        n//=10
    return rn

print(reverseNumber(200))
print(reverseNumber(122))

        