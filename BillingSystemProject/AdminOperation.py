from tkinter import *
import tkinter as tk
from tkinter import ttk,font
from tkinter import messagebox
import mysql.connector as sql
import re

def clear():
    email_entry.delete(0, END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)

def connect_database():
    con = sql.connect(host='localhost', user='root', password='root', database='userdata')
    mycursor = con.cursor()
    if email_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror('Error', 'All Fields Are Required',parent=root)
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_entry.get()):
        messagebox.showerror('Error', 'Invalid email format',parent=root)
        return
    elif len(password_entry.get()) < 8:
        messagebox.showerror('Error', 'Password must be at least 8 characters',parent=root)
        return

    query = 'select * from Casherusers where password=%s'
    mycursor.execute(query, (password_entry.get(),))
    row = mycursor.fetchone()
    if row != None:
        messagebox.showerror('Error', 'password Already exists',parent=root)
        return

    query = 'select * from Casherusers where email=%s'
    mycursor.execute(query, (email_entry.get(),))
    row = mycursor.fetchone()
    if row != None:
        messagebox.showerror('Error', 'email must be unique',parent=root)
        return

    else:
        try:
            con = sql.connect(host='localhost', user='root', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity issue, Please Try Again',parent=root)
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table Casherusers(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')
        query = 'select * from Casherusers where username=%s'
        mycursor.execute(query, (username_entry.get(),))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already exists',parent=root)
        else:
            # Insert data into database
            insert_query="INSERT INTO Casherusers (email,username, password) VALUES (%s,%s, %s)" #(username, password, email))
            insert_data=(email_entry.get(),username_entry.get(), password_entry.get())
            mycursor.execute(insert_query,insert_data)
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful',parent=root)
            clear()
            update_table()

def update_info():
    con = sql.connect(host="localhost", user="Rupali", password="root",database="userdata" )
    mycursor = con.cursor()
    selected_item = tree.selection()
    if selected_item:
        email = email_entry.get()
        username=username_entry.get()
        password=password_entry.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+",  email):
            messagebox.showerror("Error", "Invalid email format",parent=root)
            return

        # Validate password
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters",parent=root)
            return

        user_id = tree.item(selected_item)['values'][0]

        # Check if password is unique
        query="SELECT * FROM Casherusers WHERE password=%s AND id != %s"
        mycursor.execute(query,(password,user_id))
        if mycursor.fetchone():
            messagebox.showerror("Error", "Password must be unique",parent=root)
            return

        # Check if email is unique
        query="SELECT * FROM Casherusers WHERE email=%s AND id != %s"
        mycursor.execute(query,(email,user_id))
        if mycursor.fetchone():
            messagebox.showerror("Error", "email must be unique",parent=root)
            return

        query="UPDATE Casherusers SET  email=%s,username=%s, password=%s WHERE id=%s"
        mycursor.execute(query,(email,username,password,user_id))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Update data is Successful',parent=root)
        clear()
        update_table()

def delete_info():
    con = sql.connect(host="localhost", user="Rupali", password="root",database="userdata")
    mycursor = con.cursor()
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a user to delete",parent=root)
        return
    elif selected_item:
        user_id = tree.item(selected_item)['values'][0]
        mycursor.execute("DELETE FROM Casherusers WHERE id = %s", (user_id,))
       # con.commit()
        messagebox.showinfo("Success", "User deleted successfully",parent=root)
        con.commit()
        con.close()
        update_table()

def check_info():
    update_table()

def update_table():
    con = sql.connect(host="localhost", user="Rupali", password="root",database="userdata")
    mycursor = con.cursor()
    for row in tree.get_children():
        tree.delete(row)
    mycursor.execute("SELECT * FROM Casherusers")
    rows = mycursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    con.commit()

root = tk.Tk()
root.title("User Information")
root.configure(bg='teal')

custom_font=font.Font(size=16)
# Entry fields
username_label = tk.Label(root, text="Username:",font=custom_font)
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(root,font=('arial',15),bd=7,width=18)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:",font=custom_font)
password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*",font=('arial',15),bd=7,width=18)
password_entry.grid(row=2, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:",font=custom_font)
email_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(root,font=('arial',15),bd=7,width=18)
email_entry.grid(row=4, column=1, padx=5, pady=5)

#button
check_button = tk.Button(root, text="Check Information",font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=15,pady=10,
                         command=check_info)
check_button.grid(row=6, column=0, padx=7, pady=5)

save_button = tk.Button(root, text="Save",font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=10,pady=10,
                        command=connect_database)
save_button.grid(row=6, column=1, padx=7, pady=5)

update_button = tk.Button(root, text="Update",font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=10,pady=10,
                          command=update_info)
update_button.grid(row=6, column=2, padx=7, pady=5)

delete_button = tk.Button(root, text="Delete",font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=10,pady=10,
                          command=delete_info)
delete_button.grid(row=6, column=3, padx=7, pady=5)

# Table to display user information
tree = ttk.Treeview(root, columns=("ID", "Email", "Username", "Password"), show="headings")
tree.heading("ID", text="user_id")
tree.heading("Email", text="email")
tree.heading("Username", text="username")
tree.heading("Password", text="password")

tree.grid(row=7, columnspan=4, padx=5, pady=5)

root.mainloop()