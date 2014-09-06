import re
import math

class Transformer:
	x, y = 0, 0

	def setX(self, x):
		self.x = float(x)

	def setY(self, y):
		self.y = float(y)

	def translate(self, x, y):
		self.x = self.x + x
		self.y = self.y + y
		print "Translate by (%f,%f)" % (x, y)

	def rotate(self, x, y, theta):
		self.x = self.x - x
		self.y = self.y - y
		theta = theta
		tmpX = math.cos(theta)*self.x + math.sin(theta)*self.y
		tmpY = math.sin(theta)*self.x + math.cos(theta)*self.y
		self.x = tmpX + x
		self.y = tmpY + y
		print "Rotation at (%f, %f) by %f" % (x, y, theta)

	def scale(self, x, y, factor):
		dx = self.x - x
		dy = self.y - y
		self.x = x + (dx * factor)
		self.y = y + (dy * factor)
		print "Scale at (%f, %f) by factor %f" % (x, y, factor)

	def reflect(self, axis):
		if axis.lower() == 'y':
			self.y = self.y * -1
		elif axis.lower() == 'x':
			self.x = self.x * -1
		print "Reflect in the %s axis" % (axis.lower())

	def getCoords(self, user_input, args):
		if args == 1:
			coords = re.search('[a-zA-Z]*\(([a-zA-Z])\)', user_input.replace(" ",""))
			if coords:
				return {0:coords.group(1)}
		elif args == 2:
			coords = re.search('[a-zA-Z]*\((-?[0-9]+\.?[0-9]*),(-?[0-9]+\.?[0-9]*)\)', user_input.replace(" ",""))
			if coords:
				return {0:coords.group(1), 1:coords.group(2)}
		elif args == 3:
			coords = re.search('[a-zA-Z]*\((-?[0-9]+\.?[0-9]*),(-?[0-9]+\.?[0-9]*),(-?[0-9]+\.?[0-9]*)\)', user_input.replace(" ",""))
			if coords:
				return [coords.group(1), coords.group(2), coords.group(3)]
		else:
			print "Invalid Argument Number"
			quit()
		if not coords:
			print "Formatting Error"
			quit()

line = ""
cmd_buffer = []
while line != "finish()":
	line = raw_input()
	cmd_buffer.append(line.replace(" ",""))

optimus = Transformer()
coordinates = optimus.getCoords(cmd_buffer.pop(0), 2)
optimus.setX(coordinates[0])
optimus.setY(coordinates[1])

for cmd in cmd_buffer:
	if cmd.find("translate(") != -1:
		tmp = optimus.getCoords(cmd, 2)
		optimus.translate(float(tmp[0]), float(tmp[1]))
	elif cmd.find("reflect(") != -1:
		tmp = optimus.getCoords(cmd, 1)
		optimus.reflect(tmp[0])
	elif cmd.find("scale(") != -1:
		tmp = optimus.getCoords(cmd, 3)
		optimus.scale(float(tmp[0]), float(tmp[1]), float(tmp[2]))
	elif cmd.find("rotate(") != -1:
		tmp = optimus.getCoords(cmd, 3)
		optimus.rotate(float(tmp[0]), float(tmp[1]), float(tmp[2]))
	elif cmd == "finish()":
		print "Final Position: ("+str(optimus.x)+", "+str(optimus.y)+")"
		quit()
	else:
		print "No Command Matched"
