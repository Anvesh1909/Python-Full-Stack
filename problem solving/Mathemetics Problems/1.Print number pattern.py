'''You are given a number n. You need to generate and print a pattern based on the given value of n.

1. For each row, starting from the first, print numbers in descending order from n down to 1.
2. Each number in a row is repeated as many times as the current row index (starting from n).
3. Instead of printing each row on a new line, separate rows with -1.
4. Instead of a newline at the end of each row, print -1 to indicate row separation. After printing the entire pattern, end the output with -1.

For n= 3,
pattern:    3 3 3 2 2 2 1 1 1
            3 3 2 2 1 1 
            3 2 1

For n= 2,
pattern:  2 2 1 1
          2 
          
          
Examples :

Input: 2
Output: [2, 2, 1, 1, -1, 2, 1, -1]
Input: 3
Output: [3, 3, 3, 2, 2, 2, 1, 1, 1, -1, 3, 3, 2, 2, 1, 1, -1, 3, 2, 1, -1]
Input: 1
Output: [1, -1]
Constraints:
1 <= n <= 40


'''
          
'''
            j   3      2        1
    3        k3 3 3 k2 2 2 k1 1 1
    2         3 3 2 2 1 1 
    1         3 2 1       

'''

n = int(input("Enter a number: "))
res = []

for i in range(3,0,-1):
    for j in range(3,0,-1):
        for k in range(i):
            # print(j,end=" ")
            res.append(j)
    # print()
    res.append(-1)
    
print(res)