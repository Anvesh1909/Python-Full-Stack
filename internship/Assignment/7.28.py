import tkinter as tk
from datetime import datetime

def main():
    root = tk.Tk()
    
    root.geometry("500x500")
    root.title("Age Calculator")
    
    d = tk.IntVar()
    m = tk.IntVar()
    y = tk.IntVar()
    
    l = tk.Label(text="ACCURATE AGE CALCULATOR APP")
    l.grid(row=1,column=1)
    
    l = tk.Label(text="BIRTH DATE:")
    l.grid(row=2,column=1)
    e = tk.Entry(root,textvariable=d)
    e.grid(row=2,column=2)
    
    l = tk.Label(text="BIRTH MONTH:")
    l.grid(row=3,column=1)
    e = tk.Entry(root,textvariable=m)
    e.grid(row=3,column=2)
    
    
    l = tk.Label(text="BIRTH YEAR:")
    l.grid(row=4,column=1)
    e = tk.Entry(root,textvariable=y)
    e.grid(row=4,column=2)
    
    
    def getAge():
        date = int(datetime.now().strftime('%d'))-d.get()
        month = int(datetime.now().strftime('%m'))-m.get()
        year = int(datetime.now().strftime('%Y'))-y.get()
        
        
        r = f"Your Age is \n {year} years {month} months and {date} days"
        res.config(text=r)
    
    def clearRecord():
        d.set(0)
        m.set(0)
        y.set(0)
        
    get = tk.Button(root,text="Get Age",command=getAge)
    get.grid(row=5,column=1)
    clear = tk.Button(root,text="CLEAR",command=clearRecord)
    clear.grid(row=5,column=2)
    
    res = tk.Label(root,text="")    
    res.grid(row=6,column=1)
    
    
    root.mainloop()
    
    
# from datetime import datetime
# date = datetime.now().strftime('%Y-%m-%d')
# print(date)

if __name__=="__main__":
    main()