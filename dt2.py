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

sdt = 