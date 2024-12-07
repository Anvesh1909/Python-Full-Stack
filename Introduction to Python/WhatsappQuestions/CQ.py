# 1.If the string S="Rossum" then if i've enter 3 as user input then output should be 'sum'.Explain with code.

S = "Rossum"

a = int(input("enter a numebr : "))

print(S[-a:])



# 2.Checkout whether the first element and last element are same in the list [4,3,5,2,6,2,4],if yes show output as "True" OR "False".
l = [4,3,5,2,6,2,4]
if l[0] == l[-1]:
    print("True")
else:
    print("False")


# 3.If num=3579 then show the output as "9 7 5 3"(With separated empty spaces).

num = 3579
num = " ".join(list(str(num))[::-1])
print(num)



# 4.Calculate the tax for the purchase amount,if the purchase amount is less than 13000 then 0% tax,
# if purchase is in between 13000 to 21000 then tax should be 15%,if purchase is morethan 21000 then tax should be 18%.
# (Purchase should be take as dynamically)

amt = float(input("Enter the amount : "))
if amt<13000:
    print(amt,"with 0% tax")
elif 13000<=amt<21000:
    amt = amt*(115/100)
    print(amt,"with 15% tax")
elif amt>= 21000:
    amt = amt*(118/100)
    print(amt,"with 18% tax")


# 5.Write a code that accepts three names in the user input,show the output as follows without using indexing or slicing.
#   output: Name1 : Mahendra
#           Name2 : Singh
#           Name3 : Dhoni
# FullName : Mahendra Singh Dhoni

FullName = input("enter fitst middle last name: ")
FullName = FullName.split(" ")
print("Name1 :",FullName[0])
print("Name2 :",FullName[1])
print("Name3 :",FullName[2])


# 6.Create a string that takes the first character,middle character,last character from the string. 
#   (Ex: input="James" output: 'Jms')

Name = input("Enter name: ")
print(Name[::2])


# 7.Create a string that contains another string in the middle position of it's string.
#   (Ex: input1="Hel0",input2="Hi" output: 'HeHilo')
s1 = input("Enter input 1 : ")
s2 = input("Enter input 2 : ")

m = len(s1)//2
res = s1[:m] +s2 +s1[m:]
print(res)


# 8.Write a python code to convert the string "Python" into "nhyPto".
s = input("Enter a string: ")

res = s[::-2]+s[::2]
print(res)


# 9.Write a python code to convert the two strings s1="ABC",s2="xyz" into "AzByCx".
s1 = "ABC"
s2 = "xyz" 
res = ""
for i in range(len(s1)):
    res += s1[i]+s2[-i-1]

print(res)

# 10.Convert the string "Ram-is-a-DataScientist" into 'Ram is a Data-Scientist" without using replace().

s = "Ram-is-a-DataScientist"
s = s.split("-")
s[3] = s[3][:4]+"-"+s[3][4:]
print(" ".join(s))