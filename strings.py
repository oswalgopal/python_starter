# string in python are surrounded by either single or double quotation marks . Let's Look at starting formatting and some string methods

name = 'Brad'
age = 37 

#concatenate 

# print("hello my name is " + name + " and I am " + age)    gives us error so we will cast age to string using str()

print ("hello my name is " + name + "and I am " + str(age))

# string formatting 

# 1. arguments by position :- 

print('Hello  my name is {name} and I am {age}'.format(name= name , age=age))

# 2. using F-string :-  (only in python 3.6 +)
print(f'Hello My name is {name } and I am {age}')


#string methods 

s= 'hello world'
 

# capitalize string  : - captalize the first letter
print(s.capitalize())

# Make all uppercase :- 
print(s.upper())

#Make all lower:- 
print(s.lower())

# make swap case:- 
print(s.swapcase())

#get length:- 
print(len(s))

#Replace :- 
print(s.replace('world', 'everyone'))

#Count :- 
sub = 'h'
print(s.count(sub))

#starts with :-   returns true or false based on the string is starting with the argument give in the function here it start with hello so return true
print(s.startswith('hello'))

#ends with :- returns true or false based on the string is starting with the argument give in the function here it ends with d so return true
print(s.endswith('d'))

#split into list :- 
print(s.split())

#Find position :- 
print(s.find('r'))

#Is all alphanumeric:- 
print(s.isalnum())

# is all alphabetic :- 
print(s.isalpha())

#is all numeric :-
print(s.isnumeric())