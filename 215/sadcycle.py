from collections import Counter

# Read from file
base  = 11
start = 2

total = 0
num_list = []
current = start

while len(num_list) == 0 or Counter(num_list).most_common(1)[0][1] < 2:
	for c in str(current):
		i = int(c)
		total += pow(i, base)
	num_list.append(total)
	current = total
	total = 0

common = Counter(num_list).most_common(1)[0][0]
idx = [i for i, j in enumerate(num_list) if j == common]
print ", ".join(map(str, num_list[idx[0]:idx[1]]))
