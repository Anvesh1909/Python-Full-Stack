def convert(s,n):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # alpha = [ord(i) for i in range(97,97+26)]
    i = 0
    while alpha[i]!=s:
        i+=1
    return alpha[(i+n)%26]

def strtonum(s):
    l = ['0','1','2','3','4','5','6','7','8','9']
    res = 0
    for i in s:
        i = 0 
        while l[i]!=s:
            i+=1
        res = res*10+i
    return res

s = "Hyb2erz1bx3a3"
res=""
i = 0
while i<len(s)-1:
    if s[i+1] in '0123456789':
        n = strtonum(s[i+1])
        res += convert(s[i],n)
        i+=1
    else:
        res+=s[i]
    i+=1
print(res)

  

print(ord("z"))


alpha = [chr(i) for i in range(97,97+26)]
print(alpha)

numbers = [ord(i) for i in alpha]
print(alpha)

d = {}
for i in range(0,26):
    d[alpha[i]] = numbers[i]
print(d)



d  = { chr(i+97): ord(chr(i+97)) for i in range(0,26)}
print(d)




try: 
    a = 10/0
except ValueError as e:
    print(e)
except:
    print("Error handled")