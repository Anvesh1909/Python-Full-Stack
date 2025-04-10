# 1
light = input("Enter the color : ")

if light.lower() == "green":
    print("Car is allowed to go")
elif light.lower() == "yellow":
    print("Car has to wait")
elif light.lower() == "red":
    print("Car has to stop")
else:
    print("unrecognized signal. Example black, blue, etc...")



# 2
name = input("Enter Student Name: ")
stdClass = int(input("Enter class: "))
section = input("Enter section: ")
g = input("Enter Student Grade : ")

print("-----------------------------------------------------------")
print("Name:",name)
print("Class:",stdClass)
print("Section:",section)

if g.lower() == "a":
    print("Gread: Outstanding")
elif g.lower() == "b":
    print("Gread: Excellent")
elif g.lower() == "c":
    print("Gread: Very Good")
elif g.lower() == "d":
    print("Gread: Good")
elif g.lower() == "e":
    print("Gread: Satisfactory")
else:
    print("Gread: Unrecognized")



# 3
name = input("Enter Student Name: ")
stdClass = int(input("Enter class: "))
section = input("Enter Section: ")
cMark = int(input("Enter C-Language Mark: "))
jMark = int(input("Enter Java Mark: "))
pMark = int(input("Enter Python Mark: "))
wMark = int(input("Enter Web Development Mark: "))
dMark = int(input("Enter Data Base Mark: "))



print("---------Student Details-------------")
print("Name:",name)
print("Class:",stdClass)
print("Section:",section)

per = (cMark+jMark+pMark+wMark+dMark)/5
print("Presentage:",per)

if per > 45:
    print("Pass!")
else:
    print("Fail!")

if per < 45:
    print("Remark: Fail!")
elif per >= 45 and per < 60:
    print("Remark: Pass!")
elif per >= 60 and per < 75:
    print("Remark: Good!")
elif per >= 75 and per < 85:
    print("Remark: Very Good!")
elif per >= 85 and per <= 100:
    print("Remark: Excellent!")
else:
    print("If the percentage is below zero or above 100, it's an error.")




# 4
name = input("Enter Student Name: ")
stdClass = int(input("Enter class: "))
section = input("Enter Section: ")
subject = int(input("Enter The Subject Name: "))
mark = int(input("Mark scored in that subject: "))


print("------ Tracing your Python Mark ------")
print("Name:",name)
print("Class:",stdClass)
print("Section:",section)

per = (cMark+jMark+pMark+wMark+dMark)/5
print(subject,"Mark is: ",per)

if per > 50:
    print("Congratulations! Pass in",subject)
else:
    print("Congratulations! Fail in",subject)

if per < 50:
    print("Remark: Fail! in",subject)
elif per >= 50 and per < 60:
    print("Remark: Good! in",subject)
elif per >= 60 and per < 80:
    print("Remark: Very Good! in",subject)
elif per >= 80 and per < 100:
    print("Remark: Outstanding! in",subject)
else:
    print("If the percentage is below zero or above 100, it's an error.",subject)


# 5
sal = int(input("Enter Salary: "))
exp = int(input("Enter Experience: "))

if exp>=5:
    print(sal*(105/100))
else:
    print(sal)


# 6
l = int(input("Enter length: "))
b = int(input("Enter Breadth: "))

if l==b:
    print("It is a square")
else:
    print("It is not a square")



# 7
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a>b:
    print("A is greater ")



# 8
qnt = int(input("Enter the quantity: "))
cost = int(input("Enter the cost: "))
total = qnt*cost

if total > 1000:
    total *= 90/100

print("Total cost = ",total)




# 9
marks = int(input("Enter Marks: "))

if marks < 25:
    print("F")
elif 25 <= marks < 45:
    print("E")
elif 45 <= marks < 50:
    print("D")
elif 50 <= marks < 60:
    print("C")
elif 60 <= marks < 80:
    print("B")
elif 80 <= marks <= 100:
    print("A")



# 10
a = int(input("Enter first : "))
b = int(input("Enter secound : "))
c = int(input("Enter third : "))

if a>b and a>c:
    print("A is oldest")
elif b>c:
    print("B is oldest")
else:
    print("C is oldest")


if a<b and a<c:
    print("A is youngest")
elif b<c:
    print("B is youngest")
else:
    print("C is youngest")


# 11 
i = int(input("Enter an integer"))
print(abs(i))


# 12
total_classes = int(input("Enter the total number of classes : "))
attended_classes = int(input("Enter the number of classes attended : "))

percentage = (attended_classes/total_classes)*100

print(percentage)
if percentage<75:
    print("you are not allowed")
else:
    print("you are allowed")


# 13
total_classes = int(input("Enter the total number of classes : "))
attended_classes = int(input("Enter the number of classes attended : "))

percentage = (attended_classes/total_classes)*100

medicalCause = input("has medical cause or not ('Y' or 'N') :")
if medicalCause == "Y":
    print("you are allowed")
else:
    print(percentage)
    if percentage<75:
        print("you are not allowed")
    else:
        print("you are allowed")


# 14
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year% 400 == 0:
            print(year,"leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"leap year")
else:
    print(year,"is not a leap year")



# 15
age = int(input("Enter the age: "))
sex = int(input("Enter the sex: "))
ms = input("Enter maritial status: ")

if sex=="F":
    print("she will work only in urban areas.")
elif age>=20 and age<40:
    print("he may work in anywhere.")
elif age>=40 and age<=60:
    print("he will work in urban areas only. ")
else:
    print("ERROR")


# 16
n = int(input("Enter a number: "))

if n%2==1 and n%3==0:
    print("number is odd and divisible by 3. ")
else:
    print("number is not odd and divisible by 3. ")
