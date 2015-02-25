import csv

reader = csv.reader(open("map.csv", "rb"),delimiter=',')
data = list(reader)

graph = {}
distances = {}
routes = {}

for record in data:
	# Initialise distances and routes
	distances[record[0]] = 0
	routes[record[0]] = ''
	distances[record[1]] = 0
	routes[record[1]] = ''

	# Setup Graph data
	record[3] = int(record[3])
	record[4] = int(record[4])
	record[5] = int(record[5])
	record[6] = int(record[6])
	node = record[0]
	graph.setdefault(node, []).append(record)
	node = record[1]
	r = record
	graph.setdefault(node, []).append((r[1],r[0],r[2],r[3],r[4],r[5],r[6]))

# Using Input
route = raw_input().split(' ');
startNode = route[0]
destNode = route[1]
startTime = int(route[2])

# Hardcoded Test
#startNode = 'A'
#destNode = 'M'
#startTime = int('0800')
#timeIndex = 3

if 600 < startTime and startTime <= 1000:
	timeIndex = 3
elif 1001 < startTime and startTime <= 1500:
	timeIndex = 4
elif 1501 < startTime and startTime <= 1900:
	timeIndex = 5
else:
	timeIndex = 6

visited = []
currentNode = startNode
time = 0
done = False

# Print Route
print startNode+" "+destNode+" "+route[2]

# Begin Route
routes[currentNode] = currentNode

while not done:
	# Mark current node as visited
	visited.append(currentNode)

	# Check each path connected to this node
	for path in graph[currentNode]:
		# Only check unvisited nodes
		if path[1] not in visited:
			# The distance to the next node along this path
			testDistance = distances[currentNode] + path[timeIndex]

			# If the next node hasn't been assigned a distance yet
			# OR the distance calculated is smaller, then assign it
			if distances[path[1]] == 0 or testDistance < distances[path[1]]:
				# Set the distance for this node
				distances[path[1]] = testDistance

				# Build the route to this node through the graph
				if routes[path[0]] == '':
					routes[path[1]] = path[1]
				else:
					routes[path[1]] = routes[path[0]] + ", " + path[1]

	# Work out which unvisited node to go to next in the graph
	lowestDistance = 0
	nextNode = False
	for node, paths in graph.items():
		if node not in visited:
			# The next node to visit will be the one with the lowest distance
			if (lowestDistance == 0 or (distances[node] > 0 and distances[node] < lowestDistance)):
				lowestDistance = distances[node]
				nextNode = node

	# This likely means we've visited all nodes and not found the destination node
	if nextNode == False:
		print "No Solution Found."
		done = True
	elif nextNode == destNode:
		print "Solution Found."
		print "Route: " + routes[nextNode]
		print "Distance: " + str(distances[nextNode])
		done = True
	else:
		currentNode = nextNode
