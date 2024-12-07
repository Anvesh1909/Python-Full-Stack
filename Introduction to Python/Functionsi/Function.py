def add(a,b): # formal parameter
    print(f"{a} + {b} = {a+b}")

if __name__ == "__main__":
    add(10,20) # actual parameter



# write a python script display 5 product information reading all product values from the keyboard by calling function once.



# map using namefull function
def mul(a):
    return a*10

l1 = [1,2,3,4,5]
l2 = list(map(mul,l1))
print(l1)
print(l2)



from functools import reduce

def add(x1,x2):
    return x1+x2

nums = [1,2,3,4,5]
total = reduce(add,nums)

print(total)