import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("700x700")
    
    details = {
        "Name" : tk.StringVar(),
        "Phone no": tk.IntVar(),
        "Dept" : tk.StringVar(),
        "Exp" : tk.IntVar(),
        "ID" : tk.IntVar(),
        "Email" : tk.StringVar(),
        "Address" : tk.StringVar(),
        "Education" : tk.StringVar()
    }
    
    r=0
    c=0
    for k,v in details.items():
        l = tk.Label(root,text=k)
        l.grid(row=r,column=c)
        e = tk.Entry(root,textvariable=v)
        e.grid(row=r,column=c+1)
        if r==3:
            c=2
            r=-1
        r+=1
    
    
    sal = {
        "jan" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "feb" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "march" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "april" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "may" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "june" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "july" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "aug" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "sep" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "oct" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "now" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "dec" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        
    }
    
    r = 4
    for k,v in sal.items():
        l1 = tk.Label(root,text=f"Enter {k} sal: ")
        l1.grid(row=r,column=0)
        e1 = tk.Entry(root,textvariable=v[0])
        e1.grid(row=r,column=1)
        
        l2 = tk.Label(root,text=f"Enter {k} leaves")
        l2.grid(row=r,column=2)
        e2 = tk.Entry(root,textvariable=v[1])
        e2.grid(row=r,column=3)
    
        l3 = tk.Label(root,text=f"Enter {k} PT amt")
        l3.grid(row=r,column=4)
        e3 = tk.Entry(root,textvariable=v[2])
        e3.grid(row=r,column=5)
    
        l4 = tk.Label(root,text=f"Enter {k} paid sal")
        l4.grid(row=r,column=6)
        e4 = tk.Entry(root,textvariable=v[3])
        e4.grid(row=r,column=7)
        r+=1
    
    
    def submit():
        r = 20
        c=0
        for k,v in details.items():
            l = tk.Label(root,text=k)
            l.grid(row=r,column=c)
            e = tk.Label(root,text=v.get())
            e.grid(row=r,column=c+1)
            c+=2
            if c==8:
                r+=1
                c=0
            
        Ts = 0
        Nl = 0
        PT = 0
        PS = 0
        for i in sal.values():
            Ts+=i[0].get()
            Nl+=i[1].get()
            PT+=i[2].get()
            PS+=i[3].get()
            
        r+=1
        l = tk.Label(root,text="Total Financial Year Amount: ")
        l.grid(row=r,column=0)
        l = tk.Label(root,text=Ts)
        l.grid(row=r,column=1)
        l = tk.Label(root,text="Total Number of Leaves: ")
        l.grid(row=r,column=2)
        l = tk.Label(root,text=Nl)
        l.grid(row=r,column=3)
        l = tk.Label(root,text="Total Pt Amount Debited: ")
        l.grid(row=r,column=4)
        l = tk.Label(root,text=PT)
        l.grid(row=r,column=5)
        l = tk.Label(root,text="Total paid salary: ")
        l.grid(row=r,column=6)
        l = tk.Label(root,text=PS)
        l.grid(row=r,column=7)
       
        
            
    subBtn = tk.Button(text="Submit",command=submit)
    subBtn.grid(row=r+1,column=1)
    
    
    root.mainloop()
    
    
    
if __name__=="__main__":
    main()