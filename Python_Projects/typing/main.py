from tkinter import *

t = Tk()
t.title('Typing')
t.geometry("1024x720")
t.resizable(0, 0)
t.config(background="green")
lb1 = Label(t, text="hello", padx=100, pady=100, background="red", fg="yellow", font="Arial 25 bold")
txt = Entry(t)
btn = Button(t)


def fun():
    text = txt.get()
    print(text)

btn.config(command=fun)


lb1.pack()
txt.pack()
btn.pack()
btn.pack(side=RIGHT)
t.mainloop()
