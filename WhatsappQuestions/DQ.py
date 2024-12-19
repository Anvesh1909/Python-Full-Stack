
# ***********
# * .  .  .  .  . *
# * .  .  .  .  . *
# * .  .  .  .  . *
# * .  .  .  .  . *
# * .  .  .  .  . *
# ***********


n = int(input("Enter a number : "))

for i in range(n+2):

    if i == 0:
        for j in range(n*2):
            print("*",end=" ")
        print()
    

    for j in range(n+2):
        if j == 0:
            print("* ",end="")
        elif j == n+2-1:
            print(" *",end="")
        else:
            print(" . ",end="")
    
    if i == n+1:
        print()
        for j in range(n*2):
            print("*",end=" ")
    
    print()






# * * * * *
#         *
# * * * * *
# *
# * * * * *


n = int(input("Enter a number : "))
left = False

for i in range(n):
    if i%2==0:
        print("*"*n)
    else:
        if i == 0 or i == n-1:
            print(" ")
        else:
            if left == True:
                print("*")
                left = False
            else:
                print(" "*(n-1)+"*")
                left = True










# ***********
# * .  .  . *
# * .  .  . *
# * .  .  . *
# * .  .  . *
# * .  .  . *
# ***********


n = int(input("Enter a number : "))

for i in range(n+2):
    if i == 0:
        print("* "*(n*2+1))
    elif i == n+1:
        print("* "*(n*2+1))
    else:
        for j in range(n+2):
            if j == 0:
                print("* ",end = "")
            elif j == n+1:
                print(" *",end = "")
            else:
                print(" . ",end="")
        print()



# * * * * *
#         *
# * * * * *
# *
# * * * * *

n = 5
left = False

for i in range(n):
    if i%2 == 0:
        print("* "*(n))
    else:
        if left:
            print("*")
            left = False
        else:
            print("  "*(n-1)+"*")
            left = True



# ***********
# *1        *
# *2 2      *
# *3 3 3    *
# *4 4 4 4  *
# *5 5 5 5 5*
# ***********

n = int(input("Enter a number : "))

for i in range(n+2):
    if i == 0:
        print("* "*(n*2))
    elif i == n+1:
        print("* "*(n*2))
    else:
        for j in range(n+2):
            if j == 0:
                print("* ",end ="")
            elif j == n+1:
                print(" *",end ="")
            else:
                if j<=i:
                    print(f" {i} ",end="")
                else:
                    print("   ",end="")
        print()





# ***********
# * .  .  . *
# * .  .  . *
# * .  .  . *
# * .  .  . *
# * .  .  . *
# ***********


n = int(input("Enter a number : "))

for i in range(n+2):
    if i == 0:
        print("* "*(n*2+1))
    elif i == n+1:
        print("* "*(n*2+1))
    else:
        print("* "+" . "*n+" *",end="")
        print()





n = 5
for i in range(n+2):
    if i == 0 or i== n+1:
        print("* "*(n*2))

    else:
        print("* "+" . "*n+" *",end="")
        print()




print('''
***********
* .  .  . *
* .  .  . *
* .  .  . *
* .  .  . *
* .  .  . *
***********
''')