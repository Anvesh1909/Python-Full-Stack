import csv
with open("Students.csv","w",newline="") as f:
    res1 = csv.writer(f)
    res1.writerow(["id","name","age"])
    n = int(input("Enter the number of rows"))
    for i in range(n):
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        res1.writerow([id,name,age])
    