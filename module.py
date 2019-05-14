# a module is basically a file containing a set of functions to include in your application .
# There are core python modules , modules you can install using pip package manager 
# (including Django) as well as custom modules

# core modules:- 

# importing date and time module :- 

import datetime
from datetime import date
import time 
from time import time



# pip modules:- 
from camelcase  import CamelCase


# import custom modeule:- 
import validator
from validator import validate_email

today = datetime.date.today()

today2 = date.today()

# timestamp = time.time()   uncomment and run it 
timestamp2 = time() 

print(today)
print(today2)
# print(timestamp)     uncomment and run it 
print(timestamp2)

c = CamelCase() 

print(c.hump("hello there world"))


email = "test@test.com"
# email = "test#test.com"
if validate_email(email):
    print('Email is valid ')
else:
    print('email is invalid')
