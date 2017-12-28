#! python3
#
# Chapter 8 Project 2: Mad Libs
# Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
#
# For example, a text file may look like this:
# The ADJECTIVE panda walked to the NOUN and then VERB.
# A nearby NOUN was unaffected by these events.
#
# The program would find these occurrences and prompt the user to replace them.
# Enter an adjective:
# silly
# Enter a noun:
# chandelier
# Enter a verb:
# screamed
# Enter a noun:
# pickup truck
#
# The following text file would then be created:
#
# The silly panda walked to the chandelier and then screamed.
# A nearby pickup truck was unaffected by these events.
#
# The results should be printed to the screen and saved to a new text file.
# Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners (p. 196). No Starch Press. Kindle Edition.

import re

with open('C:\\Users\\Luis Miguel Luna\\Documents\\GitHub\\LaptiNek\\Python\\Automate the Boring Stuff by Al Sweigart\\Chapter 8 - Reading and Writing Files\\madLibs\\madLibsTemplate1.txt') as madLibsTemplate:
    madLibsTemplateContents = madLibsTemplate.read()
madLibsTemplateWords = list(madLibsTemplateContents.split())

adjectiveRegex = re.compile(r'ADJECTIVE*')
nounRegex = re.compile(r'NOUN*')
adverbRegex = re.compile(r'ADVERB*')
verbRegex = re.compile(r'VERB*')

for i in range(len(madLibsTemplateWords)):
    if adjectiveRegex.match(madLibsTemplateWords[i]):
        item = input('Enter an adjective: ')
    elif nounRegex.match(madLibsTemplateWords[i]):
        item = input('Enter a noun: ')
    elif adverbRegex.match(madLibsTemplateWords[i]):
        item = input('Enter an adverb: ')
    elif verbRegex.match(madLibsTemplateWords[i]):
        item = input('Enter a verb: ')
    else:
        continue
    madLibsTemplateWords.remove(madLibsTemplateWords[i])
    madLibsTemplateWords.insert(i, item)

joinWordsList = " "
newString = joinWordsList.join(madLibsTemplateWords)
with open('C:\\Users\\Luis Miguel Luna\\Documents\\GitHub\\LaptiNek\\Python\\Automate the Boring Stuff by Al Sweigart\\Chapter 8 - Reading and Writing Files\\madLibs\\madLibsFile1.txt', 'w') as newMadLibFile:
    newMadLibFile.write(newString)
print(newString)
