import venmo
import os
import mysql

def charge_setup():
  os.system("venmo configure")

def charge_for_coffee(user, price):
  cur = mysql.connect().cursor()
  cur.execute("select * from mugsy.profile where userID=(%s)",user)
  r = [dict((cur.description[i][0], value)
            for i, value in enumerate(row)) for row in cur.fetchall()]
  user_num = r[0] #Need to extract number from mysql query
  CHARGE_COMMAND = f'venmo charge {user_num} {price} \"Freedom ain\'t free, and neither is coffee!\"'
  ret_val = os.system(CHARGE_COMMAND)
  return ret_val
