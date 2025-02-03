import tkinter as tk

def main():
    root = tk.Tk()
    
    root.geometry("125x250")
    root.title("Multiplication Table")    

    n = tk.IntVar()
    l = tk.Label(root,text="Multiplication Table")
    l.grid(row=1,column=3)
    e = tk.Entry(root,textvariable=n)
    e.grid(row=2,column=3)
    
    x = tk.Label(root,height=10 ,text="Hello",pady=10)
    x.grid(row=4,column=3)
    
    
    def Result():
        res = ""
        for i in range(1,11):
            res+= f"{n.get()}X{i}={n.get()*i}\n"
        x.config(text=res)
            
            
    btn = tk.Button(root,text="Result",command=Result)
    btn.grid(row=5,column=3)
    
    root.mainloop()
    
if __name__=="__main__":
    main()