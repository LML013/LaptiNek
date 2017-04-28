#Comma Code Say you have a list value like this:

#spam = ['apples', 'bananas', 'tofu', 'cats']

#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any list value passed to it.

#Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners (p. 102). No Starch Press. Kindle Edition.

spam = ['apples', 'bananas', 'tofu', 'cats', "dogs", "oranges", "mushrooms"]

def commas(x):
	commaList = ""
	for i in range(len(x)-1):
		commaList += (str(x[i]) + ", ")
	commaList += ("and " + x[-1] + ".")
	print(commaList)
		
commas(spam)