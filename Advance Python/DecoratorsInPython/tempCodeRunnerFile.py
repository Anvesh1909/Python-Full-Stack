def PrimeDecorator(prime):
    
    def checkPrime(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
    def inner(n):
        if checkPrime(n):
            return prime(n)
        else:
            return False
    return inner


@PrimeDecorator
def number(n):
    return n

print(number(10))
print(number(7))