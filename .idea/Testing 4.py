from tkinter import *
import tkinter.messagebox as tkMessageBox
#import sqlite3
import tkinter as tk
import tkinter.ttk as ttk

root = Tk()
root.title("Python: Personal information management")
USERNAME = StringVar()
PASSWORD = StringVar()
width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#9BE3DE")



def policydocument():
    global policydoc
    policydoc = Toplevel()
    policydoc.config(bg="#BEEBE9")
    scrollbar = Scrollbar(policydoc)
    scrollbar.pack(side=RIGHT, fill=Y)
    policydoc.title("Personal Ainformation Management/policydoc")
    width = 500
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    policydoc.geometry("%dx%d+%d+%d" % (width, height, x, y))
    policydoc.resizable(0, 0)
    file = open('PI.txt', 'r+')  # Text file i am using
    with open('PI.txt') as file:  # Use file to refer to the file object
        data = file.read()  # date=current text in text file
    policy_txt = Text(policydoc, yscrollcommand=scrollbar.set, height=20, width=40)
    policy_txt.insert('1.0', data)
    policy_txt.pack()
    chkValue =BooleanVar()
    chkValue.set(False)
    Checkbutton(policydoc, text="I Agree", var=chkValue).pack()
    #chkAgree.grid(row = 1,column=0)
    #btn_continue = Button(policydoc, Text="Continue", font=('arial', 16), command=ContinuetodataBase(root)).grid()
    #btn_continue.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_continue = Button(policydoc, text="Continue")
    btn_continue.pack(side=TOP, padx=10, pady=10, fill=X)

def callback():
     Acclogin.destroy()
     policydocument()

def Accountlogin():
    global Acclogin
    Acclogin = Toplevel(root)
    Acclogin.title("Personal information Management/login")
    lbl_username = Label(Acclogin, text="Username:", font=('arial', 25), bd=1)
    lbl_username.grid(row=0)
    username=Entry(Acclogin, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0,column=1)
    lbl_password= Label(Acclogin, text="Password:", font=('arial', 25), bd=1)
    lbl_password.grid(row=1)
    password = Entry(Acclogin, textvariable=PASSWORD, font=('arial', 25), width=15)
    password.grid(row=1,column=1)
    login_button = Button(Acclogin, text="LOGIN",font=('arial',16),command=callback).grid()
    login_button.pack(padx=20, pady=40)
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Acclogin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Acclogin .resizable(0, 0)


lbl_display = Label(root, text="Personal Information Management", font=('arial', 40), width=800).pack()
btn_display = Button(root, text="ACCOUNT LOGIN", font=('arial', 16), command= Accountlogin)
btn_display.pack(fill=tk.X, padx=400, pady=250)

root.mainloop()