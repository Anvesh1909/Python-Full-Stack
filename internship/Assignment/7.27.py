import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("500x750")
    
    root.title("Radio Button")
    
    l = tk.Label(text = "Select Your Favourite Programming Language")
    l.grid(row=1,column=1)
    
    
    selected = tk.StringVar()
    
    def display():
        l.config(text=f"Your are selected the option: {selected.get()}")
        
    
    r1 = tk.Radiobutton(root, text='Python', value='Python', variable=selected,command=display)
    r2 = tk.Radiobutton(root, text='Java', value='Java', variable=selected,command=display)
    r3 = tk.Radiobutton(root, text='DBMS', value='DBMS', variable=selected,command=display)
    r1.grid(row=2,column=5)
    r2.grid(row=3,column=5)
    r3.grid(row=4,column=5)
    
    
    l = tk.Label(text="")
    l.grid(row=5,column=5)
    

    
    root.mainloop()

if __name__=="__main__":
    main()