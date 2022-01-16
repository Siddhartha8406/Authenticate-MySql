import tkinter
import Backend
from tkinter.messagebox import *

def errorWindow():
    answer = askretrycancel(
        title='Credential error',
        message='Username/password is wrong. Do you want to retry?'
    )
    if answer:
        main()

def submit():
    root.destroy()
    uname = uvar.get()
    password = passvar.get()
    if Backend.authenticate(uname,password):
        pass
    else:
        errorWindow()

def main():
    global root, uvar, passvar

    root = tkinter.Tk()
    uvar = tkinter.StringVar()
    passvar = tkinter.StringVar()

    tkinter.Label(root, text='Enter your Username', font=(12)).grid(column=0, row=1)
    tkinter.Entry(root, textvariable=uvar, font=(15)).grid(column=1, row=1)

    tkinter.Label(root, text='Enter your password', font=(12)).grid(column=0, row=2)
    tkinter.Entry(root, textvariable=passvar, show='*', font=(15)).grid(column=1, row=2)

    tkinter.Button(root, text='Button', command=submit, font=(12)).grid(column=0, row=3)

    link = tkinter.Label(root, text="www.tutorialspoint.com", font=(15), fg="blue", cursor="hand2")
    link.grid(row=4, column=1)
    link.bind("<Button-1>", lambda e:errorWindow())
    root.mainloop()

if __name__ == '__main__':
    main()