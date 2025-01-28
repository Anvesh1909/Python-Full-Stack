'''
1.Retrieve the palindrome numbers from the list
  without using built-in functions
ex: nums = [535,7823,172,1233,35353,37273]
output : [535,35353,37273]

2. Retrieve the unique digits from the number and arrange them in decending order in integer format
ex: num = 516150
output : 6510

3. Find the prime numbers and composite numbers by creating two diffrent lambda functions
'''


'''
1.Retrieve the palindrome numbers from the list
  without using built-in functions
ex: nums = [535,7823,172,1233,35353,37273]
output : [535,35353,37273]


reverse number 

rn = 0 -> 5 -> 53 -> 535
5
50 + 3 = 53
530 + 5 = 535

n = 535
%10 -> last digit 535%10 -> 5
//10 -> remove last digit  535//10 -> 53

53%10 -> 3
53//10 -> 5

5%10 -> 5
5//10 -> 0
'''



def reverseNumber(n):
    rn = 0
    while n>0:
        a = n%10
        rn = rn*10 + a 
        n//=10
    return rn

# reverseNumber(22321)

nums = [535,7823,172,1233,35353,37273]
pali = []

for i in nums:
    if i == reverseNumber(i):
        # pali.append(i)
        pali += [i]
print(pali)




# l1 = [1,4,5,6]
# l2 = [123]

# print(l1+l2)

# l1+=[9]
# print(l1)


# print(l1[1]+l2[0]) 




'''
2. Retrieve the unique digits from the number and arrange them in decending order in integer format
ex: num = 516150
output : 6510


516150

unique : [5,1,6,0]
sort   : [6,5,1,0]
single number : 6510



1st step: unique

uniqueList = [] -> [0] -> [0,5] ->  [0,5,1] -> [0,5,1,6]

516150
516150%10 -> 0 
516150//10 -> 51615

51615%10-> 5 
51615//10 -> 5161

5161%10 -> 1
5161//10 -> 516

516%10 -> 6
516//10 -> 51

51%10 -> 1   donot append because already exists
51//10 -> 5

5%10-> 5    donot append because already exists
5//10 -> 0 


2nd step sort reverse
uniqueList.sort(reverse=True)

3rd single number
[6, 5, 1, 0]
n = 0
6
60 + 5 = 65
650 + 1 = 651
6510 + 0 = 6510
'''



def uniqueNo(n):
    uniqueList = []
    while n>0:
        a= n%10
        if a not in uniqueList:
            # uniqueList.append(a)
            uniqueList += [a]
        n//=10
    
    uniqueList.sort(reverse=True) 
    
    n=0
    for i in uniqueList:
        n= n*10 + i
    
    return n


print(uniqueNo(516150))



'''
3. Find the prime numbers and composite numbers by creating two diffrent lambda functions


13 -> prime
2 to 12 -> 0 factors 

12 -> composite 
2 to 11 -> 2,3,4,6 -> 4 factors

'''

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True



def factors(n):
    # f = []
    # for i in range(2,n):
    #     if n%i==0:
    #         f+=[i]
    # return f
    return [ i for i in range(2,n) if n%i==0]


n = 23
if factors(n) == []:
    print("Prime")
else:
    print("Composite")



factors = lambda n: [ i for i in range(2,n) if n%i==0]

prime = lambda n: factors(n) == []

# n = 23
# if prime(n):
#     print("Prime number")
# else:
#     print("Compoite number")


primeNo = []
composite = []

for i in range(1,101):
    if prime(i):
        primeNo+=[i]
    else:
        composite+=[i]

print("prime numbers are : ",primeNo)
print("composite numbers are : ",composite)    
    
    
    
    
    
    
    
    
    
    
l = []
for i in range(1,10):
    l.append(i)
print(l)


l = [ i for i in range(1,10) ]
print(l)



l = []
for i in range(1,10):
    if i%2==0:
        l.append(i)
print(l)


l = [ i for i in range(1,10) if i%2==0]
print(l)