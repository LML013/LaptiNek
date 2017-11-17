# Regex Version of strip()

# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

# Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners (p. 172). No Starch Press. Kindle Edition.

import re

def regexStrip(string, remove = None):
	if remove == None:
		whiteSpaceRegex = re.compile(r'^\s*|\s*$')
		result = whiteSpaceRegex.sub('', string)
	else:
		removeRegex = re.compile(" " + remove, re.I | re.DOTALL)
		result = removeRegex.sub("", string)
	print(result)

# Setting test string variables as teStr
teStr1 = "Testing 1 2 3."
teStr2 = "Testing 1 2 3. Red Leather, Yellow Leather."
teStr3 = "        Testing 1 2 3.          "
teStr4 = "Testing 1 2 3."
	
print("Initial strings")						# Showing initial strings
print(teStr1 + "\n" + teStr2 + "\n" + teStr3 + "\n" + teStr4 + "\n")
	
print("regexStrip strings")						# Showing strings after regexStrip is done with them
regexStrip(teStr1)
regexStrip(teStr2, "Leather")
regexStrip(teStr3)
regexStrip(teStr4, "2")


# Admittedly I looked up some solutions to this one and found a few things that I could use to make it as short as I could.