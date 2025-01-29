import tkinter as tk

def main():
        
    root = tk.Tk()
    
    root.title("Arthimetic operators")
    root.geometry('500x500')
    
    first = tk.IntVar()
    secound = tk.IntVar()
    
    
    
    firstNoLabel = tk.Label(root,text="Enter The First Number: ")
    firstNoEntry = tk.Entry(root,width=20,textvariable=first)
    
    firstNoLabel.grid(row=0 ,column=0)
    firstNoEntry.grid(row=0 , column=50)
    
    secoundNoLabel = tk.Label(root,text="Enter The First Number: ")
    secoundNoEntry = tk.Entry(root,width=20,textvariable=secound)
    
    secoundNoLabel.grid(row=20 ,column=0)
    secoundNoEntry.grid(row=20 , column=50)
    
    
    result = tk.Label(root,text=f"Result : 0")
    result.grid(row=40,column=10)
    
    
    def updateRes(text):
        result.config(text=text)
    
    def addition():
        a = first.get()+secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")
        
    def exponent():
        a = first.get()**secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")

    def Modulus():
        a = first.get()%secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")

    def floordivision():
        a = first.get()//secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")

    def division():
        a = first.get()/secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")

    def multiplecation():
        a = first.get()*secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")

        
    def subtraction():
        a = first.get()-secound.get()
        first.set(0)
        secound.set(0)
        updateRes(f"Reslut : {a}")
        
        
    
        
    add = tk.Button(root,text="addition +",command=addition)
    add.grid(row=50, column=5)
    sub = tk.Button(root,text="subtraction -",command=subtraction)
    sub.grid(row=50, column=20)
    mul = tk.Button(root,text="multiplecation *",command=multiplecation)
    mul.grid(row=50, column=40)
    mul = tk.Button(root,text="division /",command=division)
    mul.grid(row=50, column=80)
    mul = tk.Button(root,text="floor division //",command=floordivision)
    mul.grid(row=70, column=5)
    mul = tk.Button(root,text="Modulus %",command=Modulus)
    mul.grid(row=70, column=20)
    mul = tk.Button(root,text="exponent **",command=exponent)
    mul.grid(row=70, column=40)
    
    
    
    root.mainloop()

if __name__ == "__main__":
    main()