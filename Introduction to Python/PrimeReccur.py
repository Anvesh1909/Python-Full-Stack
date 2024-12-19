# def isPrime(n):
#     def prime(n, i=2):
#         if n <= 2:
#             return n == 2
#         if n % i == 0:
#             return False
#         if i * i > n:
#             return True
#         return prime(n, i + 1)

#     return prime(n)

# n = int(input("Enter a number: "))
# print(isPrime(n))



def isPrime(n):
    def prime(n, i=2):

        if n % i == 0:
            return False
        if i == n-1:
            return True
            
        return prime(n, i + 1)

    return prime(n)

n = int(input("Enter a number: "))
print(isPrime(n))
