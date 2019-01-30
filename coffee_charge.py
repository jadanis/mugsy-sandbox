import venmo
import os

CHARGE_COMMAND = f'charge {} {} \"Freedom ain't free, and neither is coffee!\"'

def charge_setup():
  os.system("venmo configure")

def charge_for_coffee(user, price):
  chargeString = CHARGE_COMMAND % (user, price)
  os.system(chargeString)
