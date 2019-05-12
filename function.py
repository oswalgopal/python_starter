#  A function is a block of code which only runs when it is called . In python we donot use curly braces we use indentation with tabs or spacess


# create a function :- 

def sayHello(name):
    print(f'hello {name}')


sayHello('Gopal Oswal')

# with default parameter:- 
def Hey(name='Sam'):
    print(f'hello {name}')

Hey()           # observe the differnce in the output.          
Hey('Gopal')  # observe the differnce in the output.



# return values :- 
def getSum(num1,num2):
    total = num1 + num2
    return total

getSum(5,8)        # see the differnce in the output
print(getSum(5,8)) # see the differnce in the output



# A lambda function is a small anonymus function
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions .
 

sum = lambda num1, num2 : num1 + num2

print(sum(10,20))
