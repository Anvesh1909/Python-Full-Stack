class TrainInfo:
    def __init__(self,tno,tname,arrtime,depttime,date,source,destination):
        self.tno = tno
        self.tname = tname
        self.arrtime = arrtime
        self.depttime = depttime
        self.date = date
        self.source = source
        self.destination = destination
        
    def m1(self):
        print(self.tno,self.tname,self.arrtime,self.depttime,self.date,self.source,self.destination)
        
        
# import pickle
        
# with open("Pickle.txt","wb") as f:
#     t = TrainInfo(12345,"RE","11","12","12/2/2334","hyderabad","pakistan")
#     pickle.dump(t,f)
#     print("Pickling done successfully")
    
    

import pickle
with open("pickle.txt","rb") as f:
    obj = pickle.load(f)
    obj.m1()
    
    
    

    
    
    