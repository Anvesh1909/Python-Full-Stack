class Product_class:
    def setPid(self,pid):
        self.pid = pid
        
    def getPid(self):
        return self.pid

    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    
p1 = Product_class()
p1.setPid(1)
print(p1.getPid())
p1.setName("Laptop")
print(p1.getName())

print(p1.pid,p1.name)