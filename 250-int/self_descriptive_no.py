def checkSum(num):
	total = sum([int(i) for i in str(num)])
	return total == len(str(num))

base = int(input())

minimum = 10 ** (base - 1)
maximum = 10 ** base

self_descriptives = []
for i in range(minimum-1, maximum+1):
	if not(checkSum(i)):
		continue

	is_descriptive = 0
	for idx, val in enumerate(str(i)):
		if int(str(i).count(str(idx))) == int(val):
			is_descriptive += 1
		else:
			continue
	if is_descriptive == len(str(minimum)):
		self_descriptives.append(i)

for s in self_descriptives:
	print(s)
