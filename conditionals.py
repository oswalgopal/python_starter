# If / else conditions are used to decide to do something based on something being true or false


x=10 
y=5

# comparison operator:- (==,!=,<,>,<=,>=)  these are used to compare values

#Simple if :- 
if x > y :
    print(f'{x} is greater than {y}')


# If else :-
if y > x :
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif:- 
if y > x :
    print(f'{x} is greater than {y}')
elif x==y: 
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

a=5
b=12

#nested if:- 
if a>2:
    if a<10:
        print(f"{x} is less than 10 but greater than 2")


#Logical Operations :- (and or not ) Use to combine conditional operators 


# and operator:-
if a>2 and a<10:
    print(f'{x} is less than 10 but greater than 2')


# or operator:-

if b>2 or b<10:
    print(f'{b} is greater than 2 or less than 10 ')

#not operator:- 
if not(a==b):
    print(f'{a} is not equal to {b}')


#Membership Operators (in , not in ) - Membership operators are used to test if a sequence is presented in an object 

c=3

# in
numbers =[1,2,3,4,5]

if c in numbers:
    print(c)
    print(c in numbers)   # returns true or false based on the conditions 

# not in 

d=6

if d not in numbers:
    print(d)
    print(d not in numbers)
    print(c not in numbers)  #this will return  the false value

e=4

if e not in numbers:
    print(e)
    print(e not in numbers)




# Identity Operator (is , is not):- compare the objects , not if they are equal , 
# but if they are actually the same object, with the same memory location 


#is 

x=y
if x is y:
    print(x is y) 

y=40
if x is not y:
    print(x is not y) 
