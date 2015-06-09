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

while no_of_logs > 0:
	buckets[buckets.index(min(buckets))] += 1
	no_of_logs -= 1

for i in range(size):
	for j in range(size):
		print (buckets.pop(0), end=" ")
	print()
