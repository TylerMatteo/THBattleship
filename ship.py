class Ship:

	coords = {}

	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.is_sunk = False

