# This program says hello and asks for my name.

print ('Hello world!') #Prints "Hello world!"
print ('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName) # concatenates string

print('The length of your name is: ' + str(len(myName)) + ' letters.') # prints length of name

print('What is your age?') #asks for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
