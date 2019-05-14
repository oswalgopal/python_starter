# Python has functions for creating ,reading ,updating, and deleting files.

# open a file :-

myfile = open('myfile.txt', 'w')   # first arg as a file name and second as the read or write mode 


# getting some info of the file:- 

print('Name of the file :- ', myfile.name)  # myfile is an object for the files 
print('Is closed :-', myfile.closed)
print('Opening mode:- ' , myfile.mode)

# write a file:- 
myfile.write("I love python")
myfile.write(" I love js")
myfile.close()

# append to the file :-

myfile = open('myfile.txt','a')
myfile.write(' I love angular')
myfile.close()


# read from the file :-

myfile = open('myfile.txt','r+')
text= myfile.read(100)   # argument is no of charcters that is 100 here 
print(text)
