s = input("Enter a string : ")

def vowels():
    c = 0
    for i in s:
        if i in "AEIOUaeiou":
            c+=1
    print("No of vowels",c)


def consonents():
    c = 0
    for i in s:
        if i not in "AEIOUaeiou":
            c+=1
    print("No of consonets",c)


def reverseString():
    print(s[::-1])

def checkPali():
    if s==s[::-1]:
        print("palindrome")
    else:
        print("Not a palindrome")


if(__name__ =="__main__"):
    vowels()
    consonents()
    reverseString()
    checkPali()
