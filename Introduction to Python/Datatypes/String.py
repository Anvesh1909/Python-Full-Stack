s1 = 'Anvesh'
s2 = "Bunny"
s3 = '''Hello'''
s4 = """world!"""

print(s1,s2,s3,s4)
print()


s5 = '''
String data type
String can be represented as collection of charecters or sequence of charecters enclosed with ' ' or " " or ''' ''' or """ """.
while working with string data type space is also considered as a charecter.
python supports positive index which start from 0 to length-1. it is also known as forword direction
python also supports negitive direction which starts from -1 to -length. it is also known as backword direction
''' ''' or """ """ also used for multiline content
'''

print("multi line sting")
print(s5)


print(type(s1), type(s2), type(s3), type(s4), type(s5))


# I will be a 'software developer' after full stack python development
solution1 = "I will be a 'software developer' after full stack python development"
print(solution1)

solution2 = '''I will be a 'software developer' after full stack python development'''
print(solution2)

solution3 = """I will be a 'software developer' after full stack python development"""
print(solution3)

# error
# solution4 = 'I will be a 'software developer' after full stack python development'
# print(solution4)

solution4 = 'I will be a \'software developer\' after full stack python development'
print(solution4)





# indexing
name = "Anvesh"
# positive direction
#   0   1   2   3   4   5
# | --------------------- |
# | A | n | v | e | s | h |
# | --------------------- |
#   -6  -5  -4 -3  -2  -1
# negitive direction


print(name[0])
print(name[1])

print(name[-1])
print(name[-2])

# slicing
name = "Anvesh Bunny"
print("farword direction\n")
print(name[2:])
print(name[:9])
print(name[1:9])
print(name[::2])
print(name[1:10:2])
print()

print("backwards direction\n")
print(name[::-1])
print(name[::-2])
print(name[9:0:-2])
# print(name[::0])

