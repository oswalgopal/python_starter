# list is a collection which is ordered and changeable. Allows duplicate members.


#create a list :- 
numbers = [1,2,3,4,5]
fruits =['apples','oranges','grapes','pears']

#using a constructor :- 
numbers2 = list((1,2,3,4,5))


print(numbers , numbers2)


#getting a value from the list :-
print(fruits[0])

#getting the length of the list:- 
print(len(fruits))   #return the length of the list 

#append to the list :- 
fruits.append('mangoes')

print(fruits)


#remove :- 
fruits.remove('grapes')
print(fruits)

#insert into position:- 
fruits.insert(2,'Strawberries')
print(fruits)

#remove from specific postion:- 
fruits.pop(3)

print(fruits)

#reverse a list :- 
fruits.reverse()
print(fruits)

#sort :-  sort the list in alphabetical order 
fruits.sort()

print(fruits)

#reverse sort :- sort the list in reverse in order 
fruits.sort(reverse=True)

#change value :- 

fruits[0] = 'Blueberries'