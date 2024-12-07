Uname = input("Enter Username : ")
PassW = input("Enter Password : ")

if Uname == "anvesh" and PassW == "123":
    print(Uname,PassW," : welcome")
else:
    print(Uname,PassW," : invalid")


# firstName = input("enter first name : ")
# lastName = input("enter last name : ")
# userNmae = input("enter username : ")
# p1 = input("enter password : ")
# p2 = input("Confirm password : ")

# print()

# if firstName == "Anvesh" or lastName == "M" 

n = int(input("Enter a number: "))

if n%2 == 0 or n > 100:
    print("n is even or it is greater than 50")
else:
    print("n is nither even or greater than 50")



n = True 
print(n)
print(not n)