@Even
def number(n):
    print(n)


def Even(func):
    def inner(n):
        if n%2==0:
            func(n)
        else:
            print("please pass even number")
    return inner

number(10)
number(9)