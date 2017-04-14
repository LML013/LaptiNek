# This program asks you to type 'your name' until you do so, then it thanks you.

name = ""
while True:
	print("Please type your name.")
	name = input()
	if name == 'your name':
		break
print("Thank you!")