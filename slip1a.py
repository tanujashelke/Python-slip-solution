from tkinter import *
top = Tk()
top.geometry("500x500")
l1=Label(text="hello world")
def click():
    l2=Label(top,text="sentance in click method")
    l2.pack()
b1=Button(top,text="click me",command=click)
b1.pack()
l1.pack()
top.mainloop()