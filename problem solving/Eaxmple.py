'''
n = 27
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32


7
8 4 2 1
0 1 1 1 - 7


'''





def powerof2(n):
    # i = 0
    # while 2**i <= n:
    #     if 2**i==n:
    #         return True
    #     i+=1
    # return False
    return n&(n-1) == 0 

print(powerof2(28))
print(powerof2(72))
print(powerof2(16))
