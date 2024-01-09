import mysql.connector
import regmodule as r
import sqlmodule as s
import cart
mydb=mysql.connector.connect(host='localhost',user='root',passwd='passwd',database='estationery')

def catStat():
    print()
    print('Select desired category of items based on numbered value')
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
            b=0
            while True:
                b=int(input("Enter your choice:"))
                if 1<=b<=11:
                    break
                else:
                    print('Invalid Choice')
                    continue
            c=l[b-1]
            try:
                myCursor=mydb.cursor();
                myCursor.execute("select * from inventory WHERE category='%s'" %(c));
                myTable=myCursor.fetchall();
                n=1
                for row in myTable:
                    print('===================================================')
                    print("Item code:",row[0])
                    print('Name:',row[1])
                    print('Price:',row[2])
                    print('Quantity:',row[4])
                    print('Description:',row[5])
                    print('=====================================================')
                    print()
                    n=n+1
                    b=input('Want to continue (Y/N)?')
                    b.upper()
                    if b=='Y':
                        catStat()
            finally:
                myCursor.close()
                mydb.close()

def updatePass():
    try:
        userid=input('Enter your username:')
        passwd=input('Enter the new password:')
        myCursor=mydb.cursor();
        myCursor.execute("update userpass set pass=%s where userid=%s",(userid,passwd));
        print('Password updated successfully...')
        mydb.commit();
    except Exception:
        print('Try again!')
    finally:
        myCursor.close()
        mydb.close()

def signin():
    global userid
    userid=input('Enter your username:')
    myCursor=mydb.cursor();
    myCursor.execute("select userid from userpass")
    myTable=myCursor.fetchall()
    for i in range(0,len(myTable)):
        b=[]
        b.append(userid)
        if b==list(myTable[i]):
            break
        else:
            print('Username does not exist please create account')
            r.adduser()
            p=input('Enter password:')
            mycursor=mydb.cursor()
            mycursor.execute("select pass from userpass where userid='%s'" %(userid))
            a=mycursor.fetchall()
            l=[]
            l.append(p)
            l=tuple(l)
            if l==a[0]:
                print('Sign in successful')
            else:
                print('Wrong password, Forgot password? Reset Now!')
                c=input('Do you want to update password (Y/N)?')
                if c=='Y':
                    updatePass()
                else:
                    print('Try again!')
                    signin()
            mydb.commit();
            if userid=='admin':
                admin()
            else:
                cart.Cart()
            mydb.commit();
            if a!='Y':
                myCursor.close()
                mydb.close()
def admin():
    print('Welcome to admin functions')
    print('You may perform the following functions:')
    print()
    print('Choose function according to numbered menu')
    print('1. Update Inventory-Quantity of stationery items')
    print("2. Delete item from Inventory")
    print("3. Add item in Inventory")
    print("4. Show items in Inventory")
    print("5. View Purchase Log")
    print()
    a=int(input('Enter your choice:'))
    if a==1:
        s.updateStat()
    elif a==2:
        s.delstat()
    elif a==3:
        s.addstat()
    elif a==4:
        s.showStat()
    else:
        s.log()
    b=input('Want to continue (Y/N)?')
    b=b.upper()
    if b=='Y':
        admin()
            
