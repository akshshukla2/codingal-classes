from tkinter import *

root = Tk()
root.geometry("200x300")
root.title("MAIN BOX")
l = Label(root, fg= "brown", text = "This is the main box.")
def func():
    top = Toplevel()
    top.geometry("150x100")
    top.title("TOP BOX")
    l2 = Label(top, fg="black", text = "This is the top window")

button =  Button(root, text = "Click me.", command = func)

l.pack()
root.mainloop()