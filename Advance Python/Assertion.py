std_id = int(input("Enter id: "))
print()
assert std_id != 0 , "id is cannot be 0"
print()
print(std_id)




def square(n):
    return n**n

assert square(1) == 1, "1 case problem"
assert square(2) == 4, "2 case problem"
assert square(3) == 9, "3 case problem"
assert square(4) == 16, "4 case problem"
assert square(5) == 25, "5 case problem"



def std(std_id):
    print()
    assert std_id == 0 , "id is cannot be 0"
    print()
    print(std_id)

std_id(0)



