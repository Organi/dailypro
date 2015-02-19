class Priority:
	queue = []

	def Enqueue(self, string, pA, pB):
		self.queue.append((string, pA, pB))
		
	def DequeueA(self):
		return self.Dequeue(1)

	def DequeueB(self):
		return self.Dequeue(2)

	def DequeueFirst(self):
		return self.queue.pop(0)[0]

	def Dequeue(self, index):
		current = ('', 0, 0)
		for item in self.queue:
			if float(item[index]) > float(current[index]):
				current = item
		self.queue.remove(current)
		return current[0]

	def Count(self):
		return len(self.queue)

	def Clear(self):
		self.queue = []


pQueue = Priority()

pQueue.Enqueue('test', 1, 2)
pQueue.Enqueue('test2', 2, 3)
pQueue.Enqueue('test3', 3, 4)
pQueue.Enqueue('test4', 3, 5)

print pQueue.Count()
print pQueue.queue
pQueue.DequeueB()
print pQueue.queue
print pQueue.DequeueFirst()
