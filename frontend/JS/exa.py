import re

n = input("Enter number: ")
res = re.fullmatch(n,"[6-9]{1}[0-9]{9}")
print(res)