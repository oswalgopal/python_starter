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

