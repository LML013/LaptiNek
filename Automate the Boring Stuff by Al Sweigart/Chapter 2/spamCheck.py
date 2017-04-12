# Write code that prints Hello if 1 is stored in spam,
# prints Howdy if 2 is stored in spam,
# and prints Greetings! if anything else is stored in spam.
# Sweigart, Al. Automate the Boring Stuff with Python:
# Practical Programming for Total Beginners (p. 60). No Starch Press.
# Kindle Edition. 

while True:
	print("Please input a number between 0 and 2.")
	spam = input()
	if spam == "1":
		print("Hello")
#		break
	elif spam == "2":
		print ("Howdy")
#		break
	elif spam < "0" or spam > "2":
		print("Try again!")
	else:
		print("Greetings!")
#		break