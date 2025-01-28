import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("700x700")
    
    d = {
        "Name": tk.StringVar(),
        "Ph": tk.StringVar(),
        "Dept": tk.StringVar(),
        "Exp": tk.StringVar(),
        "ID": tk.StringVar(),
        "Email": tk.StringVar(),
        "Place": tk.StringVar(),
        "Edu": tk.StringVar()
    }
    
    r = 0
    for k, var in d.items():
        tk.Label(root, text=k).grid(row=r, column=0)
        tk.Entry(root, textvariable=var).grid(row=r, column=1)
        r += 1
    
    def submit():
        r = 10
        for k, var in d.items():
            tk.Label(root, text=k).grid(row=r, column=0)
            tk.Label(root, text=var.get()).grid(row=r, column=1)
            r += 1
    
    tk.Button(root, text="Submit", command=submit).grid(row=r, column=0, columnspan=2, pady=10)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    salary = {month: [tk.IntVar() for _ in range(4)] for month in months}
    
    r += 1
    for month, vars in salary.items():
        tk.Label(root, text=month).grid(row=r, column=0)
        for i, var in enumerate(vars):
            tk.Entry(root, textvariable=var, width=10).grid(row=r, column=i+1)
        r += 1
    
    def getSal():
        total_salary = 0
        total_leaves = 0
        total_pi = 0
        total_other = 0
        
        for vars in salary.values():
            total_salary += vars[0].get()
            total_leaves += vars[1].get()
            total_pi += vars[2].get()
            total_other += vars[3].get()
        
        print(f"Total Salary: {total_salary}, Leaves: {total_leaves}, PI: {total_pi}, Other: {total_other}")
    
    tk.Button(root, text="Submit Salary", command=getSal).grid(row=r, column=0, columnspan=5, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
