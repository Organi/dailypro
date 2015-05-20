import math
import sys
import timeit

start = timeit.default_timer()

def calcDistance(c1, c2):
	return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def getClosestTreat(coords, curr_pos):
	if len(coords) > 0:
		closest = [(0,0), 999]
		for c in coords:
			dist = calcDistance(c, curr_pos)
			if dist < closest[1]:
				closest = [c, dist]
		return closest
	else:
		return 0

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = 'coords'

coords = [line.strip() for line in open(filename)]
no_of_treats = int(coords.pop(0))
coords = [tuple(map(float, x.split(' '))) for x in coords]


curr_pos = (0.5, 0.5)
distance_travelled = 0

while no_of_treats > 0:
	closest_treat = getClosestTreat(coords, curr_pos)
	distance_travelled += closest_treat[1]
	# Eat Treat
	no_of_treats -= 1
	coords.remove(closest_treat[0])
	curr_pos = closest_treat[0]

print distance_travelled
print timeit.default_timer() - start
