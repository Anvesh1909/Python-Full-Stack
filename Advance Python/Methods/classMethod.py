class Students:
    @classmethod
    def strength(cls):
        print("class method")


Students.strength()
i = Students()
i.strength()