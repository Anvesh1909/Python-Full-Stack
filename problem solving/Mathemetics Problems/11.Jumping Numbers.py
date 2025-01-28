'''
Given a positive number X. Find the largest Jumping Number which is smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1.
                All single-digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are 
                Jumping numbers but 796, 677 and 89098 are not.

 

Example 1:

Input:
X = 10
Output:
10
Explanation:
10 is the largest Jumping Number
possible for X = 10.
Example 2:

Input:
X = 50
Output:
45
Explanation:
45 is the largest Jumping Number
possible for X = 50.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function jumpingNums()
which takes an Integer X as input and returns the largest Jumping Number less than or equal to X.

 

Expected Time Complexity: O(k), where k is no of jumping numbers
Expected Auxiliary Space: O(k), where k is no of jumping numbers

 

Constraints:
1 <= X <= 109
'''


'''
n = 8987
1st iteration 
    7 and 8  
2nd iteration
    8 and 9  
3rd iteration
    9 and 8
return True


n = 13234
1 iteration
    4 and 3
2 iteration
    3 and 2
3 iteration 
    2 and 3
4 iteration
    3 and 1  return False
    
    
n = 13234
while n>0:
    a = n%10
    n//=10
    b = n%10
    if abs(a-b) != 1:
        return False
return True

n = 23234
a = n%10 = 4
n//=10 = 2323
b = n%10 = 3
abs(a-b) = 1

a = n%10  = 3
n//=10 = 232
b = n%10 = 2
abs(a-b) = 1


a = n%10 = 2
n//=10 = 23
b = n%10 = 3
abs(a-b) = 1


a = n%10 = 3
n//=10  = 2
b = n%10 =  2
abs(a-b) = 1

while n>9:

return true
    

'''

def jumpingNumber(n):
    while n>9:
        a = n%10
        n//=10
        b = n%10
        if abs(a-b) != 1:
            return False
    return True

# print(jumpingNumber(7))
# print(jumpingNumber(8987))
# print(jumpingNumber(4343456))

# print(jumpingNumber(796))
# print(jumpingNumber(677))
# print(jumpingNumber(89098))


'''
n = 50  -> not a jumping number
49 -> not a jumping number
48 -> not a jumping number
47 -> not a jumping number
46 -> not a jumping number
45 -> jumping number
'''

def closestJumpingNumber(n):
    while n>0:
        if jumpingNumber(n):
            return n
        n-=1

print(closestJumpingNumber(10))
print(closestJumpingNumber(50))
print(closestJumpingNumber(200))
print(closestJumpingNumber(10000))
print(closestJumpingNumber(9000))
print(closestJumpingNumber(8988))






