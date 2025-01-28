'''
Given two positive integers a and b, find GCD of a and b.

Note: Don't use the inbuilt gcd function

Examples:

Input: a = 3, b = 6
Output: 3
Explanation: GCD of 3 and 6 is 3
Input: a = 1, b = 1
Output: 1
Explanation: GCD of 1 and 1 is 1
Constraints:
1 ≤ a, b ≤ 109
'''

def GCD(a,b):
    if a%b == 0:
        return b
    return GCD(b,a%b)
    
print(GCD(3,6))
print(GCD(20,6))
print(GCD(1180,412))
