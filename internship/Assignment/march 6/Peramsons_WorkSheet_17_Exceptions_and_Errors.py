# 1
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2 
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Invalid integer input.")

# 3
try:
    with open("jioduyvsubdhjcevui.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# 4
try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = num1 + int(num2)
except TypeError:
    print("Error: Inputs must be numbers.")


# 5
try:
    with open("QT_Home_Work_18_Python_File_Handling.pdf", "w") as file:
        content = file.writelines("Jello")
        
except PermissionError:
    print("Error: Permission denied.")

# 6
try:
    lst = [1, 2, 3]
    index = int(input("Enter index: "))
    print(lst[index])
except IndexError:
    print("Error: Index out of range.")

# 7
try:
    num = int(input("Enter a number: "))
except KeyboardInterrupt:
    print("\nError: User interrupted input.")

# 8
try:
    a = 10 / 0
except ArithmeticError:
    print("Error: Arithmetic operation failed.")

# 9
try:
    num = 10
    num.append(5)  
except AttributeError:
    print("Error: Attribute does not exist.")

# 10
try:
    emp_id = int(input("Enter Employee ID: "))
    print(f"Employee ID: {emp_id}")
except ValueError:
    print("Error: Invalid Employee ID.")
finally:
    print("Employee record processing complete.")

# 11
try:
    student_name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    print(f"Student: {student_name}, Age: {age}")
except ValueError:
    print("Error: Invalid age input.")
finally:
    print("Student record processing complete.")
