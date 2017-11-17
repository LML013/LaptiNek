# Strong Password Detection

# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is

# at least eight characters long,
# contains both uppercase and lowercase characters,
# and has at least one digit.

# You may need to test the string against multiple regex patterns to validate its strength.

# Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners (p. 172). No Starch Press. Kindle Edition. 

import re

def strongPass(password):
	lowerRegex = re.compile(r'[a-z]')
	upperRegex = re.compile(r'[A-Z]')
	numRegex = re.compile(r'[0-9]')
	molower = lowerRegex.search(password)
	moupper = upperRegex.search(password)
	monum = numRegex.search(password)
	if len(password) < 8:
		print('Your password is less than 8 characters which is too short.')
	elif not molower:
		print('You need at least one lower case letter.')
	elif not moupper:
		print('You need at least one upper case letter.')
	elif not monum:
		print('You need at least one number.')
	else:
		print('Your password is strong!')

print('What is your password?')
passW = input()
strongPass(passW)

# looked up lotspaih's answer