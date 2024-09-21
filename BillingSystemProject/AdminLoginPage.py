import tkinter as tk
from tkinter import *
import os,smtplib
from PIL import Image,ImageTk
def Update_Pdr():
    import Stock_detail

def admin_page():
    import AdminOperation

# GUI setup
root = tk.Tk()
root.title("User Management System")

def AddCasher1():
    root.destroy()
    os.system('python AdminOperation.py')

buttonFrame = Frame(root, bd=12, relief=GROOVE)
buttonFrame.grid(row=0, column=0,pady=20,padx=20)

# Buttons
CustomerAddButton=Button(buttonFrame,text='CasherDetail',font=('arial',16,'bold'),bg='teal',fg='white',bd=5,width=20,pady=20,command=admin_page)
CustomerAddButton.grid(row=0,column=0,pady=40,padx=5)

checkstockButton=Button(buttonFrame,text='Product Details',font=('arial',16,'bold'),bg='teal',fg='white',bd=5,width=20,pady=20,command=Update_Pdr)
checkstockButton.grid(row=1,column=0,pady=50,padx=5)

DisplayFrame = Frame(root, bd=8, relief=GROOVE)
DisplayFrame.grid(row=0, column=3,padx=0, pady=0)

# Create a frame
frame = tk.Frame(root)
frame.grid(row=0,column=0)

# Load the image
image = Image.open("stock1.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label within the frame to display the image
label = tk.Label(DisplayFrame, image=photo)
label.image = photo  # Keep a reference to avoid garbage collection
label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()