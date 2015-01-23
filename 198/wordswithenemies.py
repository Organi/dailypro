words = raw_input()
words = words.split(' ')

for char in words[0]:
	if char in words[1]:
		words[0] = words[0].replace(char, "", 1)
		words[1] = words[1].replace(char, "", 1)

print "Player one has: '%s' remaining." % words[0]
print "Player two has: '%s' remaining." % words[1]
if len(words[0]) > len(words[1]):
	print "Player one wins!"
elif len(words[1]) > len(words[0]):
	print "Player two wins!"
else:
	print "It's a tie!"
