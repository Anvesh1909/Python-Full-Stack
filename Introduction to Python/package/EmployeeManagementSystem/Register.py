
def register(name,pass1,pass2,email):
    print("__ register __")
    print("Name : ",name)
    print("Pass1 : ", pass1 )
    print("Pass2 : ", pass2)
    print("email : ",email)
    
    if pass1 != pass2:
        print("Registration fail")
    else:
        print("Registration successful")