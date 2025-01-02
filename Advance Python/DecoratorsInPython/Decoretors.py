# def TestCase1(name):
#     print("Name of the language is :",name)
    
# TestCase1("Python")


def TestCase(func):
    def inner(name):
        if name=="Python":
            print(name,": general purpose programming language")
        else:
            func(name)
    return inner
            
@TestCase
def languageName(name):
    print("Name of the language is :" ,name)
    

languageName("Python")
languageName("python")



def maths(func):
    def zerodivision(a,b):
        if b==0:
            print("Cannot divide by zero")
        else:
            return func(a,b)
    return zerodivision

@maths
def div(a,b):
    return a/b

print(div(10,20))
print(div(49,0))
print(div(123,12))




def TestCase(func):
    def inner(name):
        if name=="Python":
            print(name,": general purpose programming language")
        else:   
            func(name)
    return inner
            
@TestCase
def languageName(name):
    print("Name of the language is :" ,name)
    

# languageName("Python")
# languageName("python")


print("Existing and additional function ")
decor = TestCase(languageName)
decor("Python")


















