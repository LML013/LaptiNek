#! python3
# practiceQuestionFormat.py - formats practice questions from Automate the Boring Stuff kindle version

import pyperclip
text = pyperclip.paste()

# Separate lines, removes first Q and add space.
lines = text.split(" Q:")
for i in range(len(lines)):		# loop through all indexes in the "lines" list
	if i == 0:
		continue
	lines[i] = "Q:" + lines[i]	# adds the Q back to each string in the "lines" list

text = "\n\n\n\n".join(lines)
pyperclip.copy(text)
print("Done!")