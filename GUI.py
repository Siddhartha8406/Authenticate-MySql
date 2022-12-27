from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from Backend import *
from tkinter import font

def errorWindow():
    root.destroy()
    answer = askretrycancel(
        title='Credential error',
        message='Username/password is wrong. Do you want to retry?'
    )
    if answer:
        new_username()

def submit():
    root.destroy()
    uname = uvar.get()
    password = passvar.get()
    if Authenticate(uname,password):
        print('Done')
    else:
        errorWindow()

def new_username():
    new_gui = Tk()
    uname = StringVar()    
    new_gui.geometry('345x65')
    
    def check():
        user_name = uname.get()
        if Check(user_name):
            submit.grid(pady=3)
            new_gui.geometry('345x83')
            Label(new_gui, text="The username already exits. Try another username", font=('red', 11)).grid(row=1, columnspan=3)
        else:
            print("OK")

    Label(new_gui, text='Enter username', font=(11)).grid(row=2, column=1, padx=15, pady=2)
    Entry(new_gui, textvariable=uname, font=(11)).grid(row=2, column=2, pady=2)

    submit = Button(new_gui, text="Check", command=check)
    submit.grid(row=3, column=1, pady=4)
    new_gui.mainloop()

def CheckKey():
    root.destroy()
    #This function checks if username and recovery key matches
    def check():
        user_name = uname.get()
        key = ukey.get()
        if RecoveryCheck(user_name, key):
            print("OK")
        else:
            Label(new_gui, text="The username/recovery key is wrong.", 
                font=('regular', 17), bg='#2B2827', fg='red').place(x=8, y=235)

    new_gui = Tk()
    uname = StringVar()    
    ukey = StringVar()
    new_gui.geometry('400x300')
    new_gui.configure(bg="#2B2827")

    #Heading
    Label(new_gui, text="Password Recovery", font=("Arial", 18), bg="#424242", fg="#FFFFFF").place(x=90, y=35)

    #Entry of username
    Label(new_gui, text='Enter username', font=("Arial", 11), bg="#2B2827", fg="#FFFFFF").place(x=45, y=90)
    Entry(new_gui, textvariable=uname, font=("Arial", 11), bg="#808080").place(x=165, y=90)

    #Entry of Recover Key
    Label(new_gui, text='Enter Recovery ID', font=("Regular", 11), bg="#2B2827", fg="#FFFFFF").place(x=25, y=120)
    Entry(new_gui, textvariable=ukey, font=("Regular", 11), bg="#808080").place(x=165, y=120)

    #Submit button
    submit = Button(new_gui, text="Continue", font=("Regular", 12), bg="#3E3A39", command=check)
    submit.place(x=145, y= 160)

    new_gui.mainloop()

def newuserpass(uname):
    
    def add():
        if pass1.get() == pass2.get():
            Add(uname, pass1.get())
            new_pass.destroy()
        else:
            Label(new_pass, text="Given passwords don't match. Try again.", 
                    font=('regular', 16), bg='#2B2827', fg='red').place(x=8, y=235)

    new_pass = Tk()
    new_pass.geometry('400x300')
    new_pass.configure(bg="#2B2827")

    pass1 = StringVar()
    pass2 = StringVar()

    #Heading
    Label(new_pass, text="Password Recovery", font=("Arial", 18), bg="#424242", fg="#FFFFFF").place(x=90, y=35)

    #Entry of username
    Label(new_pass, text='Enter Password', font=("Arial", 11), bg="#2B2827", fg="#FFFFFF").place(x=45, y=90)
    Entry(new_pass, textvariable=pass1, font=("Arial", 11), bg="#808080").place(x=165, y=90)

    #Entry of Recover Key
    Label(new_pass, text='Confirm Password', font=("Regular", 11), bg="#2B2827", fg="#FFFFFF").place(x=25, y=120)
    Entry(new_pass, textvariable=pass2, font=("Regular", 11), bg="#808080").place(x=165, y=120)

    #Submit button
    submit = Button(new_pass, text="Sign Up", font=("Regular", 12), bg="#3E3A39", command=add)
    submit.place(x=145, y= 160)

    new_pass.mainloop()

def main():
    global root, uvar, passvar

    root = Tk()
    uvar = StringVar()
    passvar = StringVar()

    Label(root, text='Enter your Username', font=(12)).grid(column=0, row=1)
    Entry(root, textvariable=uvar, font=(15)).grid(column=1, row=1)

    Label(root, text='Enter your password', font=(12)).grid(column=0, row=2)
    Entry(root, textvariable=passvar, show='*', font=(15)).grid(column=1, row=2)

    Button(root, text='Login', command=submit, font=(12)).grid(column=0, row=3)

    link = Label(root, text="Forgot Password", font=(12), fg="blue", cursor="hand2")
    link.grid(row=3, column=1)
    link.bind("<Button-1>", lambda e:CheckKey())
    root.mainloop()

if __name__ == '__main__':
    main()