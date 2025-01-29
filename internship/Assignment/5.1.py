import tkinter as tk

def main():
        
    root = tk.Tk()
    
    root.title("GUI Addition")
    root.geometry('300x300')
    
    first = tk.IntVar()
    secound = tk.IntVar()
    
    
    
    firstNoLabel = tk.Label(root,text="Enter The First Number: ")
    firstNoEntry = tk.Entry(root,width=20,textvariable=first)
    
    firstNoLabel.grid(row=100 ,column=20)
    firstNoEntry.grid(row=100 , column=100)
    
    secoundNoLabel = tk.Label(root,text="Enter The First Number: ")
    secoundNoEntry = tk.Entry(root,width=20,textvariable=secound)
    
    secoundNoLabel.grid(row=200 ,column=20)
    secoundNoEntry.grid(row=200 , column=100)
    
    
    def add():
        a = first.get()+secound.get()
        print(a)
        first.set(0)
        secound.set(0)
        result = tk.Label(root,text=f"Result : {a}")
        result.grid(row=250,column=20)
        
    submit = tk.Button(root,text="Submit",command=add)
    submit.grid(row=300, column=100)
    
    root.mainloop()

if __name__ == "__main__":
    main()