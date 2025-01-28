'''
Given a Binary Number b, find its decimal equivalent.

Examples:

Input: b = 10001000
Output: 136
Input: b = 101100
Output: 44
Constraints:
1 <= number of bits in binary number  <= 16
'''

'''
b = 101100 
2^5    2^4    2^3   2^2    2^1   2^0
 32     16     8     4       2     1
 1       0     1     1       0     0
 
0-> 0-> 4 -> 12 ->  12 -> 44

s = 0
i = 0 
while b>0:
    a = b%10
    s+= a*2**i
    b//=10
    i+=1

'''

def BinToDec(b):
    s = 0
    i = 0 
    while b>0:
        a = b%10
        s+= a*2**i
        b//=10
        i+=1
    return s

print(BinToDec(10001000))
print(BinToDec(101100))



# 546
# 15
# 6 
# # if 1 then perfect number

# 154
# 10
# 1

