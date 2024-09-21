from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as sql
import os

#functions
def switch_Admin():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror('Error','All fields are Required')
    else:
        try:
            con = sql.connect(host='localhost', user='Rupali', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from AdminUsers where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if None == row:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome','Login is Successful')
            login_window.destroy()
            os.system('python AdminUserlogin.py')

def switch_Casher():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror('Error','All fields are Required')
    else:
        try:
            con = sql.connect(host='localhost', user='Rupali', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from Casherusers where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if None == row:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome','Login is Successful')
            login_window.destroy()
            os.system('python RetailBilling.py')

def hide():
    openeye.config(file='Images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.title('Login Page')
login_window.resizable(0,0)
bgImage=ImageTk.PhotoImage(file='bg (1).jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='ADMIN LOGIN',font=('microsoft yahei UI Light',18,'bold'),bg='white',fg='teal')
heading.place(x=620,y=120)

usernameEntry=Entry(login_window ,width=20,font=('microsoft yahei UI Light',11,'bold'),bd=0,fg='teal')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window ,width=20,font=('microsoft yahei UI Light',11,'bold'),bd=0,fg='teal')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

loginButton=Button(login_window,font=('Open sans',16,'bold'),text='Admin Login',fg='white',bg='teal',
                   activeforeground='white',activebackground='teal',cursor='hand2',bd=0,width=19,command=switch_Admin) #login_Admin
loginButton.place(x=578,y=310)

orlable=Label(login_window,text='-------------- OR --------------',font=('Open sans',16,'bold'),fg='teal',bg='white')
orlable.place(x=583,y=360)

loginButton=Button(login_window,font=('Open sans',16,'bold'),text='Casher Login',fg='white',bg='teal',
                   activeforeground='white',activebackground='teal',cursor='hand2',bd=0,width=19,command=switch_Casher) #login_user
loginButton.place(x=578,y=410)

facebook_logo=PhotoImage(file='Images/facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=480)

googe_logo=PhotoImage(file='Images/google.png')
googleLabel=Label(login_window,image=googe_logo,bg='white')
googleLabel.place(x=690,y=480)

twitter_logo=PhotoImage(file='Images/twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=480)

login_window.mainloop()
