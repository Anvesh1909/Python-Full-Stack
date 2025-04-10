class Abc:

    # cls and self default varible
    # self is to assign or access instance varible 
    # cls is to assign or access static variable
    def __init__(self):
        self.name = 'anvesh' # instance variable
        Abc.name = 'parana' # static variable 
    
    @classmethod
    def hello(cls):
        print(cls.name)
        cls.name = "apra" # class variable
        print(cls.name)


a = Abc()
Abc.hello()



