from tkinter import *
import tkinter as tk
from tkinter import ttk,font
from tkinter import messagebox
import mysql.connector as sql

#functions
def clear():
    Product_Name_entry.delete(0,END)
    Quantity_entry.delete(0,END)
    Price_entry.delete(0, END)

def connect_database():
    con = sql.connect(host='localhost', user='root', password='root', database='products')
    mycursor = con.cursor()
    if Product_Name_entry.get() == "" or Quantity_entry.get() == "" or Price_entry.get() == "":
        messagebox.showerror('Error', 'All Fields Are Required',parent=root)
    else:
        try:
            con = sql.connect(host='localhost', user='root', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity issue, Please Try Again',parent=root)
            return
        try:
            query = 'create database products'
            mycursor.execute(query)
            query = 'use products'
            mycursor.execute(query)
            query = 'create table products(id int auto increment primary key ,ProductName varchar(100),Quantity int,Price int)'
            mycursor.execute(query)
        except:
            mycursor.execute('use products')
        query = 'select * from products where ProductName=%s'
        mycursor.execute(query, (Product_Name_entry.get(),))
        row = mycursor.fetchone()
        if None != row:
            messagebox.showerror('Error', 'ProductName is Already exists',parent=root)
        else:
            # Insert data into database
            insert_query='INSERT INTO products(ProductName,Quantity,Price) VALUES (%s,%s,%s)' #(ProductName, Quantity, Price))
            insert_data=(Product_Name_entry.get(), Quantity_entry.get(), Price_entry.get())
            mycursor.execute(insert_query,insert_data)
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Stored data Successful',parent=root)
            clear()
            update_table()

def update_info():
    con = sql.connect(host="localhost", user="Rupali", password="root",database="products" )
    mycursor = con.cursor()
    selected_item = tree.selection()
    if selected_item:
        ProductName=Product_Name_entry.get()
        Quantity=Quantity_entry.get()
        Price = Price_entry.get()

        Product_id = tree.item(selected_item)['values'][0]

        query="UPDATE products SET ProductName=%s, Quantity=%s,Price=%s WHERE id=%s"
        mycursor.execute(query,(ProductName,Quantity,Price,Product_id))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Update data is Successful',parent=root)
        clear()
        update_table()

def delete_info():
    con = sql.connect(host="localhost", user="Rupali", password="root",database="products")
    mycursor = con.cursor()
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a user to delete",parent=root)
        return
    elif selected_item:
        Product_id = tree.item(selected_item)['values'][0]
        mycursor.execute("DELETE FROM products WHERE id = %s", (Product_id,))
       # con.commit()
        messagebox.showinfo("Success", "User deleted successfully",parent=root)
        con.commit()
        con.close()
        update_table()

def check_info():
    update_table()

def update_table():
    con = sql.connect(host="localhost", user="Rupali", password="root",database="products")
    mycursor = con.cursor()
    for row in tree.get_children():
        tree.delete(row)
    mycursor.execute("SELECT * FROM products")
    rows = mycursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    con.commit()

root = tk.Tk()
root.title("Products Information")
root.configure(bg='teal')

custom_font=font.Font(size=16)
# Entry fields
Product_Name_label = tk.Label(root, text="ProductName:",font=custom_font)
Product_Name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
Product_Name_entry = tk.Entry(root,font=('arial',15),bd=7,width=18)
Product_Name_entry.grid(row=0, column=1, padx=5, pady=5)

Quantity_label = tk.Label(root, text="Quantity:",font=custom_font)
Quantity_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
Quantity_entry = tk.Entry(root,font=('arial',15),bd=7,width=18)
Quantity_entry.grid(row=2, column=1, padx=5, pady=5)

Price_label = tk.Label(root, text="Price:",font=custom_font)
Price_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
Price_entry = tk.Entry(root,font=('arial',15),bd=7,width=18)
Price_entry.grid(row=4, column=1, padx=5, pady=5)

#button
check_button = tk.Button(root, text="Check Product",font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=15,
                                      pady=10,command=check_info)
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
tree = ttk.Treeview(root, columns=("ID", "ProductName", "Quantity", "Price"), show="headings")
tree.heading("ID", text="Product_id")
tree.heading("ProductName", text="Product_name")
tree.heading("Quantity", text="quantity")
tree.heading("Price", text="price")
tree.grid(row=7, columnspan=4, padx=5, pady=5)

root.mainloop()