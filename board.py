from battleship import BOARD_SIZE


class Board:
	
	size = BOARD_SIZE

	def __init__(self):
		self.grid = [['0' for col in range(self.size)] for row in range(self.size)]

	def print_heading(self):
		print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + 10)]))

	def print_grid(self):
		row_num = 1
		for row in self.grid:
			print(str(row_num).rjust(2) + " " + (" ".join(row)))
			row_num += 1


