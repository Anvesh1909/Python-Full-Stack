# 1
x = 10
y = 5
print("x=",x)
print("y=",y)
x,y = y,x
print("x=",x)
print("y=",y)
# or
x = 10
y = 5
print("x=",x)
print("y=",y)
temp = x
x = y
y = temp
print("x=",x)
print("y=",y)



# 2
i = 10
f = 20.192
c = 10+5j
print(i,f,c)



# 3
# 36
# 3
x = 6
y = 2
print(x**y)
print(x//y)




# 4
'''
4    -> 0100
11   -> 1011
4|11 -> 1111 -> 15

4    -> 0100
4>>2 -> 0001 -> 1
'''
a = 4
b = 11
print(a|b)
print(a>>2)



# 5
# error
y = 10
# x = y+=2
x = y+2
print(x)


# 6
'''
 2*3**3*4
 2*9*4
 72
'''
print(2*3**3*4)



# 7
'''
10-4*2
10-8
2
'''
print(10-4*2)





# 8
'''
-18//4
18/4 = 4.5
-4.5 -> -5
'''
print(-18//4)




# 9
'''
x ** 2 > 100 and y < 100
10 ** 2 > 100 and 50 < 100
100>100 and 50<100
false and true
false
'''

x = 10
y = 50 
if x ** 2 > 100 and y < 100:
    print(x,y)
    
    
    
    
# 10
'''
50
'''
x = 100
y = 50 
print(x and y)





# 11
'''
<class 'range'>
'''
print(type(range(10)))




# 12
'''
<class 'int'>
'''
print(type(10))



