import math

def standard_dev(values):
	mean = sum(map(int, values)) / len(values)
	squared_differences = [pow(val-mean, 2) for val in map(int, values)]
	sum_of_squares = sum(squared_differences)
	variance = sum_of_squares / len(values)
	sd = math.sqrt(variance)
	return sd

values = [
	"5 6 11 13 19 20 25 26 28 37",
	"37 81 86 91 97 108 109 112 112 114 115 117 121 123 141",
	"266 344 375 399 409 433 436 440 449 476 502 504 530 584 587",
	"809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373"
]

for val in values:
	print "%.4f" % standard_dev(val.split(' '))
