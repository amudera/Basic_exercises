#!/usr/bin/env python3
import datetime 
from datetime import date

birthday = input('Please enter your birth date (mm/dd/yyyy): ')
birthday_date = datetime.datetime.strptime(birthday,'%m/%d/%Y')
today = datetime.datetime.now()
days = today - birthday_date

Years = ((days.total.seconds()) / (365.242*24*3600))
Yearsint = int(Years)
Month = Yearsint * 12
Monthint = int(Month)
Hours = Monthint * 30 * 24
Hoursint = int(Hours)

  
print("Years= " + str(Years))

