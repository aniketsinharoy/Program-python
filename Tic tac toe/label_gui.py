from tkinter import *
root= Tk()
root.geometry("500x500")
f=Frame(root,bg="green",border=6,relief= SUNKEN)
f.pack(fill=BOTH)
Label(f,text="",bg="green").pack()
Label(f,text="ABC").pack()
Label(f,text="",bg="green").pack()
root.mainloop()
