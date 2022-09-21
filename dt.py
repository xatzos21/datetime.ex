# Datetime Basics 1

## Python datetime module

# In this exercise, we will focus on creating datetime objects in Python, 
# including printing special string formating of time.

# - create a variable that stores the current time
# - print out current year
# - Print the weekday of the week
# - Write a program to determine if a provided date is a leap year
# - Convert a string into a datetime object

##

import os, time
from datetime import datetime

current_datetime = datetime.now()

### Task 1

#Using the variable called `current_datetime`, print out the current year
# os.system("clear")
# print("Current year: ", current_datetime.year)
# time.sleep(3)
# os.system("clear")


### Task 2

#Using the variable called `some_date`, print out the current week day

# some_date = datetime(2022,9,21)
# print("Week day:", some_date.strftime("%w"))
# time.sleep(3)
# os.system("clear")


### Task 3

#Write a Python program to determine whether the year 2021 is a leap year.

# import calendar

# x = datetime(2021, 1, 1)
# if x == calendar.isleap(2021):
#     print(x, " is a leap year!")
# else:
#     print(x, " is not a leap year")


### Task 4

#Your task is to convert a user provided string into a datetime object.

# datestring = "Feb 14, 2021"
# date_string = datetime.strptime(datestring, "%b %d, %Y")
# print(date_string)
