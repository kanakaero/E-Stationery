import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='passwd',database='estationery');

def addstat():
    try:
        code=int(input('Enter the code:'))
        name=input('Enter the name:')
        price=int(input('Enter the price:'))
        category=input('Enter the category:')
        quantity=int(input('Enter the quantity:'))
        desc=input('Enter the description:')
        myCursor=mydb.cursor()
        myCursor.execute('insert into inventory values(%d,%s,%d,%s,%d,%s)',(code,name,price,category,quantity,desc));
        mydb.commit()
        print('Record inserted successfully...')
    except mysql.connector.errors.IntegrityError:
        print('This item already exists!')
        addstat()
    finally:
        myCursor.close()
        mydb.close()

def showStat():
    try:
        myCursor=mydb.cursor();
        myCursor.execute('select * from inventory');
        myTable=myCursor.fetchall();
        n=1
        for row in myTable:
            print('=========================================================')
            print("Item code:",n)
            print('Name of the item:',row[1])
            print('Price of the item:',row[2])
            print('Quantity available on sale:',row[4])
            print('Description of the item:',row[5])
            print('=========================================================')
            print()
            n=n+1
    finally:
        myCursor.close()
        mydb.close()

def updateStat():
    try:
        code=input('Enter the code of the stationery item to update:')
        quantity=input('Enter the new quantity:')
        myCursor=mydb.cursor();
        myCursor.execute("select quantity from inventory where code=%s"%(code));
        rec=myCursor.fetchone()
        a=eval(quantity)+rec[0]
        quantity=str(a)
        myCursor.execute("update inventory set quantity=%s where code=%s"%(quantity,code));
        print('Record updated successfully...')
        mydb.commit();
        showStat()
    except Exception:
        print('Try again!')
    finally:
        myCursor.close()
        mydb.close()

def delstat():
    try:
        code=int(input('Enter the code of the stationery item to be deleted:'))
        myCursor=mydb.cursor();
        sql_query = "select * from inventory where code = '%d'" %(code);
        myCursor.execute(sql_query)
        record = myCursor.fetchone()
        print(record)
        myCursor.execute("DELETE FROM inventory WHERE code = '%d'" % (code));
        mydb.commit();
        print(myCursor.rowcount,' record(s) deleted')
        showStat()
    except Exception:
        print('This record is already deleted')
        delstat()
    finally:
        myCursor.close()
        mydb.close()
        print('Record deleted successfully...')

def log():
    myCursor=mydb.cursor();
    myCursor.execute("select * from log")
    myTable=myCursor.fetchall()
    for row in myTable:
        print(row)
