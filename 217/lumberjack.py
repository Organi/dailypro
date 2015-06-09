import sys

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = 'inputfile'

data = [' '.join(line.split()) for line in open(filename)]

size = int(data.pop(0))
no_of_logs = int(data.pop(0))

buckets = []
for s in data:
	[buckets.append(int(el)) for el in s.split(' ')]

minimum = min(buckets)
while no_of_logs > 0:
	for i, v in enumerate(buckets):
		if v == minimum:
			buckets[i] += 1
			no_of_logs -= 1
			if no_of_logs <= 0:
				break
	minimum = min(buckets)

for i in range(size):
	for j in range(size):
		print (buckets.pop(0), end=" ")
	print()
