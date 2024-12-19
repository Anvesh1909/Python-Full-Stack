class Div:
    def div(a,b):
        if b==0:
            return None
        else:
            return a/b


class Add(Div):
    def add(a,b):
        return a+b


class Sub(Add,Div):
    def sub(a,b):
        return a-b
    

class Mul(Add,Div):
    def mul(a,b):
        return a*b






print(Div.mro())
print(Mul.mro())
print(Add.mro())
print(Sub.mro())
