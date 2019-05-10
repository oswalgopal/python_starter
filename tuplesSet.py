# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

#create a tuple :- 

fruits = ('apple', 'oranges','grapes')

# using a constructor:- 
fruits2 = tuple(('apple ', 'oranges', 'grapes'))
fruits3 = ('apple')
fruits4 = ('apple',)
# ==================================== VERY IMPORTANT==================================================
print(fruits3, type(fruits3))   #see the difference at the value of the type function if we don't use any , then it will be treated as a string .
print(fruits4, type(fruits4))   # here if we use a , over there it will be treated as a tuple otherwise as a string 

print(fruits, fruits2, type(fruits2))


# A set is a collection of unordered and unindexed. No duplicate allowed