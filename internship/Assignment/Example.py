import tkinter as tk

root = tk.Tk()

def submit():
    print(s.get())

s = tk.StringVar()

entry = tk.Entry(root,textvariable=s)
entry.grid(row=10,column=30)
sub = tk.Button(text="Submit",command=submit)
sub.grid(row=40,column=30)

root.mainloop()