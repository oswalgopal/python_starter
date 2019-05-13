# a loop is used for iterating over a sequence (that is either a list , a tuple , a dictionary , a set , or a string )

people=['john','paul','sara','susan']

# simple for loop:- 

for person in people:
    print(f"current person {person}")


# break
for person in people:
    if person =='sara':
        break
    print(person)


#continue:- 
for person in people:
    if person =='sara':
        break
    print(person)

# range:- 

for i in range(len(people)):
    print(people[i])


for i in range(0,11):
    print(i)

# while loops execuate set of statements as long as condition is true  

count =0
while count<=10:
    print(count)
    count+=1