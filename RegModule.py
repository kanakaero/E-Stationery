import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='passwd',database='estationery'); 

def adduser(): 
    try:
        userid=input('Enter your userid:')
        passwd=input('Enter your Password:')
        name=input('Enter your name:')
        phoneno=int(input('Enter your Phone number:'))
        emailid=input('Enter your Email-ID:')
        Address=input('Enter your Address:')
        myCursor=mydb.cursor()
        myCursor.execute('insert into user_details values(%s,%s,%s,%s,%s)',(userid,name,phoneno,emailid,Address));
        myCursor.execute('insert into userpass values(%s,%s)',(userid,passwd));
        mydb.commit()
        print('Record inserted successfully...')
    except Exception:
        print('Please try again!')
        adduser()
    finally:
        myCursor.close()
        mydb.close()
