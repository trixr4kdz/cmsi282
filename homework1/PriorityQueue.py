#Python translation of Ruby code from Dr. Toal's online notes

class PriorityQueue:

	def __init__ (self):
		self.data = []

	def add (self, item):
		if self.is_empty():
			self.data.append (item)
		else:
			self.data.append (item)
			self.sift_up (len(self.data) - 1)

	def getitem (self, index):
		return self.data [index]

	def sift_up (self, index):
		parentIndex = (index - 1) / 2
		if parentIndex >= 0 and (self.data [parentIndex] > self.data [index]):
			self.data [parentIndex], self.data [index] = self.data [index], self.data [parentIndex]
			self.sift_up (parentIndex)

	def peek (self):
		return self.data [0]

	def remove (self):
		if self.is_empty():
			raise ValueError, "Empty PriorityQueue!"
		elif len (self.data) == 1:
			self.data = []
		else:
			self.data.pop (0)
			self.sift_down (0)

	def sift_down (self, index):
		childIndex = (index * 2) + 1
		if childIndex >= len(self.data):
			return
		if (childIndex + 1 < len(self.data)) and (self.data [childIndex] > self.data [childIndex + 1]):
			childIndex += 1
		if self.data [index] > self.data [childIndex]:
			self.data [childIndex], self.data [index] = self.data [index], self.data [childIndex]
			self.sift_down (childIndex)

	def is_empty (self):
		return len (self.data) == 0

	def clear (self):
		self.data = []

	def __len__ (self):
		return len (self.data)

	def __str__ (self):
		return str (self.data)