'''
Given two numbers A and B, find Kth digit from right of A^B.
 

Example 1:

Input:
A = 3
B = 3
K = 1
Output:
7
Explanation:
3^3 = 27 and 1st
digit from right is 
7
Example 2:

Input:
A = 5
B = 2
K = 2
Output:
2
Explanation:
5^2 = 25 and second
digit from right is
2.

Your Task:
You don't need to read input or print anything. Your task is to complete the function kthDigit() which takes integers A, B, K as input parameters and returns Kth Digit of AB from right side.
 

Expected Time Complexity: O(log A^B)
Expected Space Complexity: O(1)
 

Constraints:
1 <= A,B <= 15
1 <=K<= digits in A^B
'''




'''
A = 5
B = 3
A^B = 125
k = 2
retun 2

n = A^B = 125
a = n%10 = 5
n//=10 = 12

a = n%10 = 2
n//=10 = 1

repeat k times 

return a

'''


def kthDigit(A,B,k):
    n = A**B
    for i in range(k):
        a = n%10
        n//=10
    return a

print(kthDigit(5,3,3))
print(kthDigit(3,3,1))
print(kthDigit(5,2,2))

