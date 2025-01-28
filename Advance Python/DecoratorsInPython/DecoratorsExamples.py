# Decorators allow us to wrap another function in order to extend 
# the behaviour of the wrapped function, without permanently modifying it



# decorators in Python to modify the functionality of a function by wrapping it in another function.



# write a program to return even number
def even(n):
    return n

print(even(20))
print(even(5))


def checkDecorator(even):
    # wrapper function
    def innerFunc(n):
        if n%2==0:
            return even(n)
        else:
            return "Enter even number "
    return innerFunc


@checkDecorator
def even(n):
    return n
    
print(even(20))
print(even(5))








def PrimeDecorator(func):
    
    def checkPrime(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
    def inner(n):
        if checkPrime(n):
            return func(n)
        else:
            return False
    return inner

# return a number if it is a prime number
@PrimeDecorator
def number(n):
    return n

print(number(10))
print(number(7))


# extending properties for functions, testing 


# functional programming is faster then opp