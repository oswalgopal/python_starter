# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

#create a tuple :- 

fruits = ('apple', 'oranges','grapes')

# using a constructor:- 
fruits2 = tuple(('apple ', 'oranges', 'grapes'))
fruits3 = ('apple')
fruits4 = ('apple',)
# ====================================================== VERY IMPORTANT =================================================================


# single value need a trailing comma :-
print(fruits3, type(fruits3))   #see the difference at the value of the type function if we don't use any , then it will be treated as a string .
print(fruits4, type(fruits4))   # here if we use a , over there it will be treated as a tuple otherwise as a string 

# get value :- 
print(fruits, fruits2, type(fruits2))

# we can't change the value of the tuple:- 
# fruits[0]= 'mangos'   # see the error while uncommenting it


# delete a tuple:- 
  # del fruits2   uncomment this to get the error which is fruits2  not defined
  # print(fruits2)   uncomment this to get the error which is fruits2  not defined

# length of tuple:- 
print(len(fruits))






# ================================================================ SET STARTED ============================================================
# A set is a collection of unordered and unindexed. No duplicate allowed

# create a set  :-  created with curly braces

fruits_set = {'apple', 'mango', 'Oranges'}

# check if in set:-  return true if exist else return false
print('apple' in fruits_set)


# Add to set :- 
fruits_set.add('Grapes') 
print(fruits_set)

#add duplicate to the set:-   # donot give any error but it won't add it twice
fruits_set.add('apple')
print(fruits_set)

# remove :- 
fruits_set.remove('Grapes')
print(fruits_set)

# clear set:-
fruits_set.clear()
print(fruits_set)

# delete the set :- 
del fruits_set
# print(fruits_set)  # generates an error that fruits_set not defines 
