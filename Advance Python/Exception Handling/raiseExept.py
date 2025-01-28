try:
    n = int(input("Enter a even number: "))
    if n%2==0:
        print(n)
    else:
        raise Exception("enter only even number")
    print("HEllo")
except Exception as e:
    print(e)




n = int(input("Enter a even number: "))
if n%2==0:
    print(n)
else:
    raise Exception("enter only even number")
print("HEllo")




try:
    print("Division")
    10/0
except:
    print("Error")
print("After division")