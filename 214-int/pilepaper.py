import itertools
import timeit
import sys
from itertools import product

start = timeit.default_timer()

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = 'file_input'

sheets = [line.strip() for line in open(filename)]
canvas = sheets.pop(0).split(' ')

#canvas = "20 10".split(' ')
#sheets = [
#	"1 5 5 10 3",
#	"2 0 0 7 7"
#]

totalTiles = int(canvas[0]) * int(canvas[1])
totals = {}
usedSheets = []

# Returns true if the two rectangles have any overlap
def overlap(s1, s2):
	hoverlap = (s1[1] <= s2[1]+s2[3]) and (s1[1]+s1[3] >= s2[1])
	voverlap = (s1[2] < s2[2]+s2[4]) and (s1[2]+s1[4] > s2[2])
	return hoverlap and voverlap

# Returns the amount of colour for the given sheet to add to the total for that colour
def getNoOfColour(sheet):
	# Calculate the maximum number of coordinates that could be coloured this colour
	num = sheet[3] * sheet[4]
	if len(usedSheets) > 0:
		# Make coordinate list for the current sheet
		coords = list(product(xrange(sheet[1], sheet[1]+sheet[3]), xrange(sheet[2], sheet[2]+sheet[4])))
		# Check each used sheet (these are higher priority sheets)
		for s in usedSheets:
			# Only perform extra calculations if there's an overlap
			if (overlap(sheet, s)):
				# Make a coordinate list
				sCoords = list(product(xrange(s[1], s[1]+s[3]), xrange(s[2], s[2]+s[4])))
				# Calculate the intersection of the coordinate list
				# and modify the main coords list
				intersection = list(set(sCoords).intersection(coords))
				[coords.remove(x) for x in intersection]
		# Override the max number of coords for this colour with the reduced number
		num = len(coords)
	return num

# Loop over the sheets in reverse order
# because the last sheet has highest priority.
# This way once a coordinate has had a colour assigned
# it will never change and doesn't need to be checked
for sheet in reversed(sheets):
	data = map(int, sheet.split(' '))
	noOfColour = getNoOfColour(data)
	try:
		totals[data[0]] += noOfColour
	except KeyError:
		totals[data[0]] = noOfColour
	usedSheets.append(data)

stop = timeit.default_timer()

# Calculate the amount remaining of the original colour 0
totals[0] = totalTiles - (sum(totals.itervalues()) - totals[0])
print totals
print sum(totals.values())
print "Running Time: " + str(stop-start)
