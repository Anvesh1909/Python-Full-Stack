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
    for k,v in details.items():
        l = tk.Label(root,text=k)
        l.grid(row=r,column=0)
        e = tk.Entry(root,textvariable=v)
        e.grid(row=r,column=1)
        r+=1
    
    
    sal = {
        "jan" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "feb" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
        "march" : [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()] 
    }
    
    r = 9
    for k,v in sal.items():
        l1 = tk.Label(root,text=f"Enter {k} sal: ")
        l1.grid(row=r,column=0)
        e1 = tk.Entry(root,textvariable=v[0])
        e1.grid(row=r,column=1)
        
        l2 = tk.Label(root,text=f"Enter {k} leaves")
        l2.grid(row=r,column=0)
        e2 = tk.Entry(root,textvariable=v[1])
        e2.grid(row=r,column=1)
    
        l3 = tk.Label(root,text=f"Enter {k} PT amt")
        l3.grid(row=r,column=0)
        e3 = tk.Entry(root,textvariable=v[2])
        e3.grid(row=r,column=1)
    
        l4 = tk.Label(root,text=f"Enter {k} paid sal")
        l4.grid(row=r,column=0)
        e4 = tk.Entry(root,textvariable=v[3])
        e4.grid(row=r,column=1)
    
    
    root.mainloop()
    
    
    
if __name__=="__main__":
    main()