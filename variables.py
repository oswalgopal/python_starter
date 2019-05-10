# A variable is a container for a value , which can be of various types 

'''
This is a multi 
line comment 
or docstring (used to specify specific functions)
can be single or double quotes
'''

"""
VARIABES RULES :- 

    ==>  Varibles names are case sensitive (name and NAME are different variables)
    ==>  Must start with a letter or a underscore
    ==>  Can have number but cannot start with numbers

"""

x = 1             #int 
y= 2.5            #float
z = "Gopal "      # str
a = 'Gopal '      # str
b = True          #boolean



# multiple assigment 
c,d,e,f = (1,2.,'gopal',True)


print(c)
print (c,d,e,f)

# Basic maths 

g = c+d

print (g)


# type checking 

print (type(c))


# type casting 


c = str(c)

print(type(c))

# casting to int    

print(type(d))

d= int(d)
print(type(d))
