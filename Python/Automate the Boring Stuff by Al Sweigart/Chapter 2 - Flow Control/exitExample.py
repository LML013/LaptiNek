import sys

while True:
	print("Type exit to exit.")
	response = input()
	if response == "exit":
		print("Goodbye!")
		sys.exit()
	print("You typed " + response + ".")