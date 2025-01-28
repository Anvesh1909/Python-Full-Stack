'''

Given the first 2 terms a1 and a2 of an Arithmetic Series.Find the nth term of the series. 

Example 1:

Input:
a1 = 2
a2 = 3
n = 4
Output: 5
Explanation:
The series is: 2,3,4,5,6....
Thus,4th term is 5.

Example 2:

Input:
a1 = 1
a2 = 3
n = 10
Output: 19
Explanation:
The series is: 1,3,5,7,9,11,13,15,17,19,21....
Thus,10th term is 19.

Your Task:
You don't need to read input or print anything.Your Task is to complete the function nthTermOfAP() which takes three integers a1, a2 and n as input parameters and returns the nth term of the AP that has a1 and a2 as the first and second terms respectively.

Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)

Constraints:
-104 <= a1 , a2 <= 104
1 <= n <= 104



'''



'''
arthemetic progressions
an = a+(n-1)d
d = a2-a1

a1 = 3
a2 = 7
d = 7-3 = 4
a3 = 11
a4 = 15
3,7,11,15,19,23...

n = 6
an = 23


an = a+(n-1)d
an = 3+(6-1)4
   = 23

'''

# a1 = int(input())
# a2 = int(input())
# n = int(input())

# d = a2-a1
# print(a1+(n-1)*d)


def nthTermOfAP(a1,a2,n):
    # d = a2-a1
    # res = a1
    # for i in range(n-1):
    #     res+=d
    # print(res)
    
    d = a2-a1
    print(a1+(n-1)*d)
    
nthTermOfAP(2,3,4)
nthTermOfAP(1,3,10)



    