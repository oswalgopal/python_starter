# A dictionary is a collection which is unordered and changeable and indexed . N duplicate members are allowed 

# create a dictionary :- 
person = {
    'firstname': 'john',
    'lastname':'Doe ',
    'age':30
}

print(person , type(person))

# using constructor :- 
person2= dict(firstname='John', lastname='Doe',age=30)
print(person2, type(person2))

# getname :-

print(person['firstname'])  # print john 
print(person.get('firstname'))  # print john


# adding key value:- 
person['phone'] ='555-555-5555'
print(person)

#getting all keys:- 
print(person.keys())

# get dict items:- 
print(person.items())

# copy dictionary :- 
person3 = person.copy()
person3['city'] = 'indore'
print(person3)

# Remove an item:- 
del(person['age'])

print(person)

# using pop :- 
person.pop('phone')
print(person)


# clear :- 
person.clear()
print(person)

# get the length:- return no of key value pairs 
print(len(person2))

# list of dictionary :- 
people = [
    {'name':'Gopal','age':'18'},
    {'name':'Gaurav','age':'22'}
]

print(people)
print(people[0]['name'])    # return gopal