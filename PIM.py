from tkinter import *
import tkinter.messagebox as tkMessageBox
#import sqlite3
import pyodbc
import tkinter as tk
import tkinter.ttk as ttk

root = Tk()
root.title("Python: Personal information management")

width = 1024
height = 1000
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#9BE3DE")

USERNAME = StringVar()
PASSWORD = StringVar()
PETNAME = StringVar()
Name = StringVar()
Surname = StringVar()
EmployeeNo = IntVar()
Address = StringVar()
ContactDetail = StringVar()
DepartmentName = StringVar()
SEARCH = StringVar()

def Database():
   global conn, cursor
   conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\18131611\PycharmProjects\PIM\Database1.accdb;')
   cursor = conn.cursor()
   cursor.execute("SELECT *FROM 'Admin' WHERE 'Username' = 'ADMIN' AND 'Password' = 'ADMIN')")
   for row in cursor.fetchall():
      print (row)

def Exit():
    result = tkMessageBox.askquestion('Personal Information Management ', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Personal Information management', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def policydocument():
    global policydoc
    policydoc = Toplevel()
    policydoc.config(bg="#BEEBE9")
    scrollbar = Scrollbar(policydoc)
    scrollbar.pack(side=RIGHT, fill=Y)
    policydoc.title("Personal information Management/policydoc")
    width = 1000
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    policydoc.geometry("%dx%d+%d+%d" % (width, height, x, y))
    policydoc.resizable(0, 0)
    file = open('PIMPolicyDocument.txt', 'r+')  # Text file i am using
    with open('PIMPolicyDocument.txt') as file:  # Use file to refer to the file object
        data = file.read()  # date=current text in text file
    policy_txt = Text(policydoc, yscrollcommand=scrollbar.set, height=20, width=800)
    policy_txt.insert('1.0', data)
    policy_txt.pack()
    chkValue = BooleanVar()
    chkValue.set(False)
    check_btn = Checkbutton(policydoc, text="I Agree", variable=chkValue).pack()
    btn_continue = Button(policydoc, text="Continue", command=Home)
    btn_continue.pack(side=TOP, padx=10, pady=10, fill=X)

def callback():
    login()

def Accountlogin():
    global Acclogin
    global lbl_result
    Acclogin = Frame(root, width=800, height=10000, bd=1, relief=SOLID)
    Acclogin.pack(side=TOP)
    lbl_username = Label(Acclogin, text="Username:", font=('arial', 25), bd=1)
    lbl_username.grid(row=0)
    username = Entry(Acclogin, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    lbl_password = Label(Acclogin, text="Password:", font=('arial', 25), bd=1)
    lbl_password.grid(row=1)
    lbl_petname = Label(Acclogin, text="PetName:", font=('arial', 25), bd=1)
    lbl_petname.grid(row=2)
    petname=Entry(Acclogin,textvariable=PETNAME,font=('arial', 25),width=15)
    petname.grid(row=2,column=1)
    lbl_result = Label(Acclogin, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    password = Entry(Acclogin, textvariable=PASSWORD, font=('arial', 25), width=15)
    password.grid(row=1, column=1)
    login_button = Button(Acclogin, text="LOGIN", font=('arial', 16), command=callback).grid()
    login_button.pack(padx=20, pady=40)


def Home():
  global Home
  Home = Tk()
  Home.title("Personal information Management/Home")
  width = 1024
  height = 720
  screen_width = Home.winfo_screenwidth()
  screen_height = Home.winfo_screenheight()
  x = (screen_width/2) - (width/2)
  y = (screen_height/2) - (height/2)
  Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
  Home.resizable(0, 0)
  Title = Frame(Home, bd=1, relief=SOLID)
  Title.pack(pady=10)
  lbl_display = Label(Title, text="Personal information Management", font=('arial', 45))
  lbl_display.pack()
  menubar = Menu(Home)
  filemenu = Menu(menubar, tearoff=0)
  filemenu2 = Menu(menubar, tearoff=0)
  filemenu.add_command(label="Logout", command=Logout)
  filemenu.add_command(label="Exit", command=Exit2)
  filemenu2.add_command(label="Add Employee", command=ShowAddnew)
  filemenu2.add_command(label="View Employee", command=ShowView)
  menubar.add_cascade(label="Account", menu=filemenu)
  menubar.add_cascade(label="Employee", menu=filemenu2)
  Home.config(menu=menubar)
  Home.config(bg="#99ff99")

def ShowAddnew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Personal information management/Add new")
    width = 600
    height = 500
    screen_width= Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y= (screen_height/2)-(height/2)
    addnewform.geometry("%dx%d+%d+%d" %(width, height, x, y))
    addnewform.resizable(0,0)
    AddNewEmployeeForm()

def AddNewEmployeeForm():
    global EmployeeNo, Name, Surname, Address, ContactDetail, DepartmentName
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Employee", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_EmployeeNo = Label(MidAddNew, text="EmployeeNo:", font=('arial', 16), bd=10)
    lbl_EmployeeNo.grid(row=0, sticky=W)
    lbl_Name = Label(MidAddNew, text="Name:", font=('arial', 16), bd=10)
    lbl_Name.grid(row=1, sticky=W)
    lbl_Surname = Label(MidAddNew, text="Surname:", font=('arial', 16), bd=10)
    lbl_Surname.grid(row=2, sticky=W)
    lbl_Address = Label(MidAddNew, text="Address", font=('arial', 16), bd=10)
    lbl_Address.grid(row=3, sticky=W)
    lbl_ContactDetail= Label(MidAddNew, text="ContactDetail ", font=('arial', 16), bd=10)
    lbl_ContactDetail .grid(row=4, sticky=W)
    lbl_DepartmentName= Label(MidAddNew, text="DepartmentName", font=('arial', 16), bd=10)
    lbl_DepartmentName.grid(row=5, sticky=W)
    EmployeeNo = Entry(MidAddNew, textvariable=EmployeeNo, font=('arial', 25), width=15)
    EmployeeNo.grid(row=0, column=1)
    Name = Entry(MidAddNew, textvariable=Name, font=('arial', 25), width=15)
    Name.grid(row=1, column=1)
    Surname= Entry(MidAddNew, textvariable=Surname, font=('arial', 25), width=15)
    Surname.grid(row=2, column=1)
    Address = Entry(MidAddNew, textvariable= Address, font=('arial', 25), width=15)
    Address.grid(row=3, column=1)
    ContactDetail = Entry(MidAddNew, textvariable=ContactDetail , font=('arial', 25), width=15)
    ContactDetail.grid(row=4, column=1)
    DepartmentName = Entry(MidAddNew, textvariable=DepartmentName, font=('arial', 25), width=15)
    DepartmentName.grid(row=5, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 10), width=10, bg="#009ACD", command=AddNewEmployee)
    btn_add.grid(row=6, columnspan=2, pady=20)



def AddNewEmployee():
    Database()
    cursor.execute("INSERT INTO `EmployeeDetials` (EmployeeNo, Name, Surname, Address , ContactDetail, DepartmentName) VALUES(?, ?, ?)", (str(EmplyeeNo.get()),str(Name.get()),str(Surname.get()),str(Address.get()),str(ContactDetail.get()),str(DepartmentName.get())))
    conn.commit()
    EmployeeNo.set("")
    Name.set("")
    Surname.set("")
    Address.set("")
    ContactDetail.set("")
    DepartmentName.set("")
    cursor.close()
    conn.close()

def ViewEmployee():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Employee", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable= SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("EmployeeNo", "Name", "Surname", "Address", "ContactDetail" , "DepartmentName"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('EmployeeNo, text="EmployeeNO",anchor=W')
    tree.heading(' Name', text=" Name",anchor=W)
    tree.heading('Surname', text="Surname",anchor=W)
    tree.heading('Address, text="Address",anchor=W')
    tree.heading('ContactDetail, text=" ContactDetail",anchor=W')
    tree.heading('DepartmentName', text=" DepartmentName",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `EmployeeDetials`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `EmployeeDetails` WHERE ` Name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def cll():
    btn_display.configure(state=DISABLED)
    Accountlogin()

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Personal Information Management ', 'Are you sure you want to delete this employee?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `EmployeeDetail` WHERE `EmployeeNo` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Personal Information Management/View Employee")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewEmployee()


def login(event = None):
    global user_id
    if USERNAME.get() == "" or PASSWORD.get() == "" or PETNAME.get()=="":
        lbl_result.config(text="Please input your login details!", fg="red")
    else:
        if USERNAME.get() == "ADMIN" and PASSWORD.get() == "ADMIN" and PETNAME.get() == "NOON":
            lbl_result.config(text="")
            Acclogin.destroy()
            policydocument()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
            PETNAME.set("")




lbl_display = Label(root, text="Personal Information Management", font=('arial', 40), width=800).pack()
btn_display = Button(root, text="ACCOUNT LOGIN", font=('arial', 16), command= cll)
btn_display.pack(fill=tk.X, padx=400, pady=250)

def Logout():
    result = tkMessageBox.askquestion('Personal Information Management', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        Home.destroy()
        btn_display.configure(state= ACTIVE)

#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=Accountlogin)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
#lbl_display = Label(Title, text=" Personal information management", font=('arial', 45))
#lbl_display.pack()

root.mainloop()