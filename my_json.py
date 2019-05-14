# JSON is commonly used with data APIS . Here how we can parse JSON into a python dictionary.

import json

#sample json:- 
userJSON = '{"firstname":"John","lastname":"Doe","age":30}'


# parse to dictionary :- 

user = json.loads(userJSON)

print(user)
print(user['firstname'])
print(type(user))



# dict to json

car = {'make':'ford','model':'Mustang','year':1970}

carJSON = json.dumps(car)

print(carJSON)    # see this is a json format 
print(type(carJSON))