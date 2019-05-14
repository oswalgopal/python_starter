# A class is like a blueprint for creating objects. An object hsa properties and methods (functions)associated with it .
# Almost everything in python is an object.


# create class :- 
class User:
    # constructor:-
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'my name is {self.name} and I am {self.age}'


    def hasBirthday(self):
        self.age += 1


# Extend class:- 
class Costumer(User):
    # constructor:-
    def __init__(self,name,email,age,balance):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self,balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and  I am {self.age} and my balance is {self.balance}'

# intialize a user object:- 
brad = User('Gopal oswal','gploswal@gmail.com',18)


# initialize a contumer :- 
janet  = Costumer('ram', 'ram@gmail.com',25,5)
janet.set_balance(25)



print(type(brad))
print(brad.name)
print(brad.age)
print(brad.email)

brad.hasBirthday()


print(brad.greeting())

print(janet.balance)
print(janet.greeting())
