import mysql.connector
import regmodule as r
import sqlmodule as s
import misc
mydb=mysql.connector.connect(host='localhost',user='root',passwd='passwd',database='estationery')
def cartStat():
    mycursor=mydb.cursor()
    mycursor.execute('SELECT category FROM inventory')
    myTable=mycursor.fetchall()
    l=[]
    for i in myTable:
        l+=i
        l=(list(set(l)))
        l.sort()
        for i in range (0,len(l)):
            print(i+1,'.',l[i])
            b=int(input("Enter your choice:"))
            c=l[b-1]
            myCursor=mydb.cursor();
            myCursor.execute("select * from inventory WHERE category='%s'" %(c));
            myTable=myCursor.fetchall();
            for row in myTable:
                print('============================================================')
                print("Item number:",row[0])
                print('Name:',row[1])
                print('Price of the item:',row[2])
                print('Quantity available on sale:',row[4])
                print('Description of the item:',row[5])
                print('============================================================')
                print()

def Cart():
    global cart
    global a
    cart={}
    a='Y'
    while a=='Y':
        cartStat()
        code=int(input('Enter the code:'))
        quantity=int(input('Enter the quantity:'))
        cart.update({code:quantity})
        print('Added to Cart successfully...')
        a=input('Want to add more(Y/N)?')
    if a!='Y':
        print('===============================================================')
        b=input('Would you like to continue to billing (Y/N)?')
        b=b.upper()
        if b=='Y':
            print('Welcome to billing section')
            billing()
        else:
            addcart()

def billing():
    print('Your Cart:')
    quantity=0
    code=0
    tot=0
    for key in cart:
        code=key
        value=cart[key]
        mycursor=mydb.cursor()
        mycursor.execute("Select Name,price from inventory where code='%s'"%(code));
        mytable=mycursor.fetchall()
        for i in mytable:
            print('=======================================================')
            print('Code:',code)
            print('Name:',i[0])
            print('Price:',i[1])
            print('Quantity:',value)
            print('========================================================')
            print()
            tot=tot+i[1]*value
        print('Total payment:',tot)
        Submitorder()

def billpay():
    print('Your Cart:')
    quantity=0
    code=0
    tot=0
    for key in cart:
        code=key
        value=cart[key]
        mycursor=mydb.cursor()
        mycursor.execute("Select Name,price from inventory where code='%s'"%(code));
        mytable=mycursor.fetchall()
        for i in mytable:
            print('======================================================')
            print('Code:',code)
            print('Name:',i[0])
            print('Price:',i[1])
            print('Quantity:',value)
            print('======================================================')
            print()
            tot=tot+i[1]*value
        print('Total payment:',tot)

def addcart():
    x='Y'
    while x=='Y':
        cartStat()
        code=int(input('Enter the code:'))
        quantity=int(input('Enter the quantity:'))
        cart.update({code:quantity})
        print('Added to Cart successfully...')
        x=input('Want to add more(Y/N)?')
        x=x.upper()
    if x!='Y':
        print('=============================================================')
        b=input('Would you like to continue to billing (Y/N)?')
        b=b.upper()
        if b=='Y':
            print('Welcome to billing section')
            billing()
        else:
            addcart()

def delcart():
    code=int(input('Enter the code of the item to be deleted:'))
    del cart[code]
    print('Updated Cart:')
    print()
    for key in cart:
        code=key
        value=cart[key]
        mycursor=mydb.cursor()
        mycursor.execute("Select Name,price from inventory where code='%s'"%(code));
        mytable=mycursor.fetchall()
        for i in mytable:
            print('=========================================================')
            print('Code:',code)
            print('Name:',i[0])
            print('Price:',i[1])
            print('Quantity:',value)
            print('=========================================================')
            print()

def Submitorder():
    z=input('Would you like to add anything to cart (Y/N)?')
    if z=='Y':
        addcart()
    else:
        x=input('Would you like to delete something from cart (Y/N)?')
        x=x.upper()
        if x=='Y':
            delcart()
    y=input('Are you ready to submit order (Y/N)?')
    y=y.upper()
    global userid
    print()
    userid=input("Enter userid:")
    if y=='Y':
        print('Your order summary:')
        billpay()
        r=input('Would you like to make payment(Y/N)?')
        r=r.upper()
        if r=='Y':
            print('Your details:')
            mycursor=mydb.cursor()
            mycursor.execute("Select Name,Phone_no,Email_ID,address from user_details where userid='%s'" %(userid));
            mytable=mycursor.fetchall()
            for i in mytable:
                print('==================================================')
                print('1.User Id:',userid)
                print('2.Name:',i[0])
                print('3.Phone Number:',i[1])
                print('4.Email ID:',i[2])
                print('5.Address:',i[3])
                print()
                s=input('Would you like to update user details (Y/N)?')
                s=s.upper()
                if s=='Y':
                    updatedet()
                else:
                    payment()
    else:
        z=input('Would you like to add anything to cart (Y/N)?')
        z=z.upper()
        if z=='Y':
            addcart()
        else:
            x=input('Would you like to delete something from cart (Y/N)?')
            if x=='Y':
                delcart()
            else:
                Submitorder()

def updatedet():
    a=int(input('What would you like to update?'))
    print()
    print('Choose option based on numbered menu')
    if a==2:
        b=input('Enter new name:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set Name=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    elif a==3:
        b=input('Enter new Phone number:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set Phone_no=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    elif a==4:
        b=input('Enter new Email ID:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set Email_ID=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    elif a==5:
        b=input('Enter new Address:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set address=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    payment()

def updatedet():
    print('Choose option based on numbered menu')
    a=int(input('What would you like to update?'))
    print()
    if a==2:
        b=input('Enter new name:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set Name=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    elif a==3:
        b=input('Enter new Phone number:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set Phone_no=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    elif a==4:
        b=input('Enter new Email ID:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set Email_ID=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    elif a==5:
        b=input('Enter new Address:')
        mycursor=mydb.cursor()
        mycursor.execute("update user_details set address=%s where userid=%s",(b,userid));
        mydb.commit()
        print('User details updated successfully')
    payment()

def payment():
    print("Welcome to payment Page")
    p=input('Would you like to confirm payment (Y/N)?')
    p=p.upper()
    if p=='Y':
        print()
        print()
        print('Payment Confirmed')
        print('Items will be delivered as soon as possible')
        print()
        print('Your bill:')
        tot=0
        for key in cart:
            code=key
            value=cart[key]
            mycursor=mydb.cursor()
            mycursor.execute("Select Name,price from inventory where code='%s'"%(code));
            mytable=mycursor.fetchall()
            for i in mytable:
                print('===================================================')
                print('Code:',code)
                print('Name:',i[0])
                print('Price:',i[1])
                print('Quantity:',value)
                print()
                myCursor=mydb.cursor();
                myCursor.execute('INSERT INTO log VALUES(%s,%s,%s,%s,%s,now())',(userid,code,i[0],i[1],value));
                myCursor.execute('UPDATE inventory SET inventory.quantity = inventory.quantity-%s WHERE code =%s',(value,code));mydb.commit()
                tot=tot+i[1]*value
                print('====================================================')
                print()
                print('Total payment made:',tot)
                print()
                print('=====================================================')
    else:
        Cart()
