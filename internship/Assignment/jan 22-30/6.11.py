def details():
    global name,phno,dept,exp,empid,email,addr,edu
    
    name = input("Enter your Full Name: ")
    phno = int(input("Enter your phone number: "))
    dept = input("Enter your Department: ")
    exp = int(input("Enter your Experience: "))
    
    empid = int(input("Enter your Employee id: "))
    email = input("Enter your Email: ")
    addr = input("Enter your address: ")
    edu = input("Enter your Education: ")
    
    
def getDetails():
    print(f"Full Name: {name}")
    print(f"phone number: {phno}")
    print(f"Department: {dept}")
    print(f"Experience: {exp}")
    print(f"Employee id: {empid}")
    print(f"Email: {email}")
    print(f"address: {addr}")
    print(f"Full Name: {name}")
    print(f"Education: {edu}")
    

def salary():
    global months,sal
    # months = ['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']
    months = ['jan','feb']
    
    sal ={ k: [0 for _ in range(4)] for k in months}
    # print(sal)
    for m,s in sal.items():
        sal[m][0] = float(input(f"Enter {m} salary amount: ")) 
        sal[m][1] = int(input(f"Enter {m} leave amount: "))
        sal[m][2] = float(input(f"Enter {m} PI amount: ")) 
        sal[m][3] = float(input(f"paid {m} salary: ")) 
        
# sal()            
def getSalary():
    L = [0,0,0,0]
    for k,v in sal.items():
        L[0] += v[0]
        L[1] += v[1]
        L[2] += v[2]
        L[3] += v[3]
    print(f"Total Financial Year Amount: {L[0]}")
    print(f"Total Number of leaves: {L[1]}")
    print(f"Total PI amount debited: {L[2]}")
    print(f"Total Paid salary: {L[3]}")
    
    
if __name__=="__main__":
    details()
    print()
    print()
    getDetails()
    print()
    print()
    salary()
    print()
    print()
    getSalary()
        
    