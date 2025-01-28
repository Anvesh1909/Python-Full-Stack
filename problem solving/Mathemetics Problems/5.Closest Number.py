'''Closest Number.py
Given two integers n and m. The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

Examples :

Input: n = 13 , m = 4
Output: 12
Explanation: 12 is the Closest Number to 13 which is divisible by 4.
Input: n = -15 , m = 6
Output: -18
Explanation: -12 and -18 are both similarly close to -15 and divisible by 6. but -18 has the maximum absolute value. So, Output is -18
Input: n = -6 , m = 39
Output: 0
Constraints:
-105 <= n, m <= 105
'''


''' n = 13 , m = 4
4*1 = 4
4*2 = 8
4*3 = 12
4*4 = 16

n-a = 13-12 = 1
n-b = 13-16 = -3
            =  3
            
abs() -> return absolute diffrence value
abs(-3) = 3
abs(3) = 3
'''


def closestNumber(n,m):
    sign = 1
    if n<0:
        sign = -1
    n = abs(n)

    i = 0
    a,b = 0,0
    while m*i<n:
        a = m*i
        i+=1
    b = m*i

    if abs(n-a) < abs(n-b):
        print(sign*a)
    else:
        print(sign*b)

closestNumber(13,4)
closestNumber(-15,6)
closestNumber(-6,39)
