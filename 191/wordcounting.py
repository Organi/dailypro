import string

# Open text file and read all contents
contents = open('pg47498.txt').read()

# Replace all punctuation with the empty string
contents = contents.translate(string.maketrans("",""), string.punctuation)

# Split string by whitespace
contents = contents.split()

# Count word occurances and store in a dictionary
words = {}
for word in contents:
	if word.lower() in words:
		words[word.lower()] += 1
	else:
		words[word.lower()] = 1

print words
