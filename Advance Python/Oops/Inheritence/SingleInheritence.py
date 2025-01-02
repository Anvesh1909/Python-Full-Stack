class Univercity:

    def __init__(self):
        print("Univercity Constructor")

    def univercityName(self):
        print("Univercity name")

class Collage(Univercity):
    def __init__(self):
        print("collage Constructor")

    def collageName(self):
        print("Collage name")

x = Collage()
x.collageName()
x.univercityName()