class OuterClass:

    def __init__(self):
            print("outer class constructor")

    class InnerClass:

        def __init__(self):
            print("Inner class constructor")

        def method(self):
            print("Instence method")



# O = OuterClass()

# I = O.InnerClass()


# I = OuterClass().InnerClass()

# I = OuterClass().InnerClass().method()





class OuterClass:

    def __init__(self):
            print("outer class constructor")
            self.name = "Python"
            self.dor = self.InnerClass()

    def method(self):
        print("Name of the language : ",self.name)
        self.dor.method()

    class InnerClass:

        def __init__(self):
            print("Inner class constructor")
            self.date = "16/7/1989"

        def method(self):
            print("date of relese is : ",self.date)


O = OuterClass()

O.method()
