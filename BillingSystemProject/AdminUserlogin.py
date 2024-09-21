from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as sql
import os

def switch_file():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror('Error','All fields are Required')
    else:
        try:
            con = sql.connect(host='localhost', user='root', password='root')
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
            os.system('python AdminPage1.py')
def forget_pass():
    def change_password():
        if user_entry.get()=="" or newpass_entry.get()=="" or confirmpass_entry.get()=="":
            messagebox.showerror('Error','All fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching ',parent=window)
        else:
            con = sql.connect(host='localhost', user='root', password='root',database='userdata')
            mycursor = con.cursor()
            query='select * from AdminUsers where username=%s'
            mycursor.execute(query,(user_entry.get(),))
            row = mycursor.fetchone()
            if None == row:
                messagebox.showerror('Error', 'Incorrect Username',parent=window)
            else:
                query='update AdminUsers set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset,Please login with new password',parent=window)
                window.destroy()


    window= Toplevel()
    window.title('Change Password')
    bgPic=ImageTk.PhotoImage(file='background.jpg')
    backimgLabel=Label(window,image=bgPic)
    backimgLabel.grid()
    hedingLabel= Label(window,text='RESET PASSWORD',font=('arial','18','bold'),bg='white',fg='teal')
    hedingLabel.place(x=480,y=60)

    userLabel=Label(window,text='Username',font=('arial','12','bold'),bg='white',fg='teal')
    userLabel.place(x=470,y=130)

    user_entry=Entry(window,width=25,fg='teal',font=('arial','12','bold'),bd=0)
    user_entry.place(x=470,y=160)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)

    passwordLabel = Label(window, text='New Password', font=('arial', '12', 'bold'), bg='white', fg='teal')
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='teal', font=('arial', '12', 'bold'), bd=0)
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmLabel = Label(window, text='Confirm Password', font=('arial', '12', 'bold'), bg='white', fg='teal')
    confirmLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='teal', font=('arial', '12', 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton=Button(window,text='Submit',bd=0,bg='teal',fg='white',font=('Open Sans','16','bold'),width=19
                       ,cursor='hand2',activeforeground='white',activebackground='teal',command=change_password)
    submitButton.place(x=470,y=390)

    window.mainloop()

def login_user():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror('Error','All fields are Required')
    else:
        try:
            con = sql.connect(host='localhost', user='root', password='root')
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
def signup_page():
    login_window.destroy()
    import signup

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

forgetButton=Button(login_window,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('microsoft yahei UI Light',10,'bold'),activeforeground='teal',fg='teal',command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,font=('Open sans',16,'bold'),text='Login',fg='white',bg='teal',
                   activeforeground='white',activebackground='teal',cursor='hand2',bd=0,width=19,command=switch_file)  #login_user
loginButton.place(x=578,y=360)

orlable=Label(login_window,text='-------------- OR --------------',font=('Open sans',16,'bold'),fg='teal',bg='white')
orlable.place(x=583,y=400)

facebook_logo=PhotoImage(file='Images/facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

googe_logo=PhotoImage(file='Images/google.png')
googleLabel=Label(login_window,image=googe_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='Images/twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signuplable=Label(login_window,text='Dont have an account?',font=('Open sans',9,'bold'),fg='firebrick1',bg='white')
signuplable.place(x=590,y=500)

newaccountButton=Button(login_window,font=('Open sans',9,'bold underline'),text='Create new admin',fg='blue',bg='white'
                   ,activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

login_window.mainloop()