def Even(func):
    def inner(n):
        if n%2==0:
            func(n)
        else:
            print("please pass even number")
    return inner

            
# @Even
# def number(n):
#     print(n)
    
    
# number(10)
# number(9)


def Even(func):
    def inner(n):
        if n%2==0:
            func(n)
        else:
            print("please pass even number")
    return inner



@Even
def number(n):
    print(n)
    
    
number(10)
number(9)
print(id(number))

# d = Even(number)
# d(10)
# d(9)

print(Even)
print(number)
                   