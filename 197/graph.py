import csv

reader = csv.reader(open("map.csv", "rb"),delimiter=',')

data = list(reader)

for record in data:
	print "data: " + str(record)


