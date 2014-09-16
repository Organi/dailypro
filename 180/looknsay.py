def looknsay(number):
	result = ''
	noofrepeats = 1
	repeatnumber = number[0]
	number = number[1:]+" "

	for i in number:
		if i != repeatnumber:
			result += str(noofrepeats)+repeatnumber
			noofrepeats = 1
			repeatnumber = i
		else:
			noofrepeats += 1
	
	return result

print "Please input a number: "
a = raw_input();
print "Choose seed number (press return to use seed 1): "
seed = raw_input();
if seed == '':
	seed = "1"
print "Show All?"
s = raw_input()
if a.isdigit() == False or seed.isdigit() == False:
	print "Please choose a number"
	quit()
else:
	for i in range(int(a)):
		if (i == int(a)-1) or s.lower() == "y":
			print seed
		seed = looknsay(seed)
