# Task is to create a
# Birthday Day Calculator
# - takes birthday as input
# - prints out years, months, weeks & days since

import os, datetime

os.system("clear")
a = input("Enter birthday d,m,y:")
x = datetime.date(a)
y = datetime.date.fromisoformat(x)
z = datetime.date.today()

print(x)