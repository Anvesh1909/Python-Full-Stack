try:
    a = eval(input("Enter number: "))
    print(a)
except ArithmeticError as e:
    print(e)
except:
    print("Except block")
else:
    print("result :",a)
finally:
    print("finally")