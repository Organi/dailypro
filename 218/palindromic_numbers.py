
num = input();

palinnumber = num

counter = 0
while (palinnumber != palinnumber[::-1]):
	palinnumber = str(int(palinnumber) + int(palinnumber[::-1]))
	counter += 1

print(num + " gets palindromic after " + str(counter) + " steps: " + palinnumber)
