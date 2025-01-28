import csv
with open("CCSSVV.csv","w",newline="") as f:
    obj1 = csv.writer(f)
    obj1.writerow(["pid","Pname","Pmarks"])
    n = int(input("Enter the number of rows: "))
    for i in range(n):
        pid = input("Enter the pid: ")
        name = input("Enter the name: ")
        marks = input("Enter the marks: ")
        obj1.writerow([pid,name,marks])
        print()
    print("CSV File is created")
        
        
        
        
        
        
import csv
with open("CCSSVV.csv","r") as f:
    obj = csv.reader(f)
    print(obj)
    for i in obj:
        print(i)