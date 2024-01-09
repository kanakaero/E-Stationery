import sqlmodule as s
import regmodule as r
import misc as m
import cart
print("Welcome to E-Stationery Portal")
q=input('Are you a new user (Y/N)?')
q=q.upper()
if q=='Y' :
    n=input('Would you like to sign up (Y/N)?')
    n=n.upper()
    if n=='Y':
        r.adduser()
        cart.Cart()
    else:
        m.catStat()
else:
    w=input('Would you like to sign in (Y/N)?')
    w.upper()
    if w=='Y' :
        m.signin()
    else:
        m.catStat()
