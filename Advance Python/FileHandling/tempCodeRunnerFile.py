        
        
import csv
with open("CCSSVV.csv","r") as f:
    obj = csv.reader(f)
    print(obj)
    for i in obj:
        print(i)