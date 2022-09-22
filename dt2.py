# Datetime Basics 2

## Manipulate Time

# In this exercise, we will focus on the use and manipulation of time in Python

# - Subtract time
# - Add time
# - Write a program to remind a tenant to pay rent on time

from datetime import datetime, timedelta
cdt = datetime.now()

### Task 1

# Using the variable called `current_datetime`,
#  subtract 15 days from the current time.

x = cdt + timedelta(days = -15)
print(x)


### Task 2

# Using the variable called `current_datetime`, 
# add 7 days to your current day.

y = cdt + timedelta(days = +7)
print(y)


### Task 3

# Your task is to determine when rent is due for a customer, 
# we shall make assumption that tenant always pays 25 days 
# from the first day of a month. Create a string that stores a message 
# to a customer called Friedrich, print out the message to the terminal.

#Start by creating a datetime instance with 25 January, 2021.

# `start_date = datetime(year=2020, month=1, day=1)`

# - Your result should look like this:

# ```
# Hello Friedrich, your rent of 300 € is due on 25 January, 2021.
# ```


sdt = datetime(2021, 1, 25)
sdt1 = datetime.strftime(sdt, "%d %B, %Y")


print("Hello Friedrich, you rent of 300€ is due on", sdt1)