import fileinput
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
from datetime import datetime

#functionality part
def update_time():
    global current_time
    current_time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    text_box.delete(1.0,END)
    text_box.insert(END, current_time)
    text_box.after(1000, update_time)  # Update every second

def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    sugarEntry.delete(0, END)
    wheatEntry.delete(0, END)
    teaEntry.delete(0, END)

    maazaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    dewEntry.delete(0, END)
    frootiEntry.delete(0, END)
    cococolaEntry.delete(0, END)

    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    teaEntry.insert(0, 0)

    maazaEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    cococolaEntry.insert(0, 0)

    cosmeticTaxEntry.delete(0, END)
    groceryTaxEntry.delete(0, END)
    drinksTaxEntry.delete(0, END)

    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)
def send_email():
    def send_email():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray28')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text="password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text=' RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial', 16, 'bold'),width=15,command=send_email)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
def search_bill():
    for i in os.listdir('Bills/'):
        if int(i.split('.')[0])== int(billnumberEntry.get()):
            f = open(f'Bills/{i}', 'r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')

if not os.path.exists('Bills'):
    os.mkdir('Bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm','Do you want  to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'Bills/ {billnumber}.txt','w')
        file.write(bill_content)


        #riceEntry.insert(0, textarea.get().replace('\t\t\t', '\t\t\t\t'))


        file.close()
        messagebox.showinfo('success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(100,500)

billnumber=random.randint(100,500)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')

    elif not all(char.isalpha() or char.isspace() for char in (nameEntry.get())):
        messagebox.showerror('Error', 'Name should contain only letters and spaces.')

    elif not (phoneEntry.get()).isdigit() or len(phoneEntry.get()) != 10:
        messagebox.showerror('Error', 'Invalid phone number.Please enter a 10-digit numeric value.')

    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are Selected')

    elif cosmeticpriceEntry.get()=='0Rs' and grocerypriceEntry.get()=='0Rs' and drinkspriceEntry.get()=='0Rs':
        messagebox.showerror('Error', 'No Products are Selected')

    else:
        textarea.delete(1.0,END)


        textarea.insert(END,f'\t\t**WELCOME CUSTOMER**\n')
        textarea.insert(END, f'\t\t               Date:{current_time}\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END, '\n\n=======================================================')
        textarea.insert(END, '\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')

        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{ hairgelprice} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\nBodyLotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')

        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{ riceprice} Rs')
        if daalEntry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')

        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if dewEntry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootprice} Rs')
        if cococolaEntry.get() != '0':
            textarea.insert(END, f'\nCoco_Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')

        textarea.insert(END, '\n-------------------------------------------------------')

        if cosmeticTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmetic Tax\t\t\t\t{cosmeticTaxEntry.get()}')
        if groceryTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Grocery Tax\t\t\t\t{groceryTaxEntry.get()}')
        if drinksTaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\n Drinks Tax\t\t\t\t{drinksTaxEntry.get()}')

        textarea.insert(END,f'\n Total Bill \t\t\t\t{totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')
        save_bill()

def total():
    global soapprice,hairsprayprice,hairgelprice,facecreamprice,facewashprice,bodylotionprice
    global riceprice,daalprice,oilprice,sugarprice,wheatprice,teaprice
    global maazaprice,frootprice,dewprice,pepsiprice,spriteprice,cococolaprice
    global totalbill

    #cosmetics price calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairsprayprice = int(hairsprayEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 80
    bodylotionprice = int(bodylotionEntry.get()) * 60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice}Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmeticTaxEntry.delete(0,END)
    cosmeticTaxEntry.insert(0,str(cosmetictax)+'Rs')

    #grocery price calculation
    riceprice=int(riceEntry.get())*30
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    sugarprice=int(sugarEntry.get())*40
    teaprice=int(teaEntry.get())*140
    wheatprice=int(wheatEntry.get())*80

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+'Rs')
    grocerytax=totalgroceryprice * 0.05
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, str(grocerytax) +'Rs')

    #ColdDrink price calculation
    maazaprice=int(maazaEntry.get())*50
    frootprice=int(frootiEntry.get())*20
    dewprice = int(dewEntry.get())*30
    pepsiprice = int(pepsiEntry.get())*20
    spriteprice = int(spriteEntry.get())*45
    cococolaprice = int(cococolaEntry.get())*90

    totaldrinksprice=maazaprice+frootprice+dewprice+pepsiprice+spriteprice+cococolaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,str(totaldrinksprice)+'Rs')
    drinkstax=totaldrinksprice * 0.08
    drinksTaxEntry.delete(0, END)
    drinksTaxEntry.insert(0, str(drinkstax) +'Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax


#GUI Part
root=Tk()
root.title('Retail Billing System')
root.geometry('1320x780')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='teal',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

Customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),bg='teal',fg='gray20',bd=8,relief=GROOVE)
Customer_details_frame.pack(fill=X)

nameLabel=Label(Customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='teal',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(Customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(Customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='teal',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(Customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(Customer_details_frame,text='Bill Number',font=('times new roman',15,'bold')
                ,bg='teal',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(Customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(Customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=18,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

text_box = Text(Customer_details_frame,font=('arial',16,'bold'),height=1, width=18,relief=GROOVE)
text_box.grid(row=0,column=7,padx=20,pady=8)
update_time()


productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='turquoise',fg='gray20',bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold')
                ,bg='turquoise',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                                  ,bg='turquoise',fg='gray20',bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold')
                ,bg='turquoise',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='oil',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Cold drinks',font=('times new roman',15,'bold'),bg='turquoise',fg='gray20',bd=8,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

maazaLabel=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinksFrame,text='Coco-cola',font=('times new roman',15,'bold'),bg='turquoise',fg='white')
cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


BillmenuFrame=LabelFrame(root,text='Bill menu',font=('times new roman',15,'bold'),bg='turquoise',fg='gray20',bd=8,relief=GROOVE)
BillmenuFrame.pack()

cosmeticpriceLabel=Label(BillmenuFrame,text='Cosmetic price',font=('times new roman',13,'bold'),bg='turquoise',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cosmeticpriceEntry=Entry(BillmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(BillmenuFrame,text='Grocery price',font=('times new roman',13,'bold'),bg='turquoise',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry(BillmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(BillmenuFrame,text='Cold drinks price',font=('times new roman',14,'bold'),bg='turquoise',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry=Entry(BillmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmeticTaxLabel=Label(BillmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='turquoise',fg='white')
cosmeticTaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

cosmeticTaxEntry=Entry(BillmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticTaxEntry.grid(row=0,column=3,pady=9,padx=10)

groceryTaxLabel=Label(BillmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold'),bg='turquoise',fg='white')
groceryTaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

groceryTaxEntry=Entry(BillmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
groceryTaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinksTaxLabel=Label(BillmenuFrame,text='Cold drinks Tax',font=('times new roman',14,'bold'),bg='turquoise',fg='white')
drinksTaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinksTaxEntry=Entry(BillmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
drinksTaxEntry.grid(row=2,column=3,pady=6,padx=10)

totalButton=Button(BillmenuFrame,text='Total',font=('arial',13,'bold'),bg='turquoise',fg='white',bd=5,width=8,pady=8,command=total)
totalButton.grid(row=3,column=2,pady=6,padx=10)

buttonFrame=Frame(BillmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=1,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=1,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=1,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='turquoise',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=1,column=4,pady=20,padx=5)

root.mainloop()