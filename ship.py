class Ship:

	coords = {}

	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __str__(self):
		return self.coords