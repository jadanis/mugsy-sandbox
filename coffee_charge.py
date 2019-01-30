import venmo
import os
import mysql

CHARGE_COMMAND = f'venmo charge %(user) %(amount) \"Freedom ain't free, and neither is coffee!\"'

def charge_setup():
  os.system("venmo configure")

def charge_for_coffee(user, price):
  cur = mysql.connect().cursor()
  cur.execute("select * from mugsy.profile where userID=(%s)",user)
  r = [dict((cur.description[i][0], value)
            for i, value in enumerate(row)) for row in cur.fetchall()]
  
  chargeString = CHARGE_COMMAND % {"user" : user_num, "amount" : price}
  os.system(chargeString)
