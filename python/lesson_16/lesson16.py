from tkinter import *

window = Tk()

window.title('Tkinter Sample Window')

window.geometry('300x300')

greeting = Label(text="Hello User", fg='black', bg='white')

button = Button(text="Click me", bg='black', fg='white')

greeting.pack()

entry = Entry(fg="yellow", bg="blue", width=50)

button.pack()

entry.pack()

frame = Frame(master=window, relief = RAISED, borderwidth=5)

frame.pack()

label1 = Label (master=frame, text='Sample Frame')

label1.pack()

textbox = Text(fg='green', bg='yellow')

textbox.pack()

window.mainloop()