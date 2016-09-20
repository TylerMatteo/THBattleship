from board import Board
from battleship import FLEET

class Player:

	board = Board()
	fleet = FLEET

	def __init__(self, name):
		self.name = name

	def place_ship(self, ship):
		print("{}, please place your {}. It is {} spaces long.".format(self.name, ship[0], ship[1]))

		# Prompt user for ship orientation
		while True:
			orientation = input("Would you like to place this ship (H)orizontally or (V)ertically? ").strip().upper()
			if (orientation == "H") or (orientation == "V"):
				break
			else:
				print('Invalid input. Please try again.')

		# Prompt user for ship column
		while True:
			row = input("Which column would you like the ship to start in? Please a letter A - {}. ".format(chr(64 + self.board.size))).strip().upper()
			if (row in [chr(l) for l in range(ord('A'), ord('A') + self.board.size)]) and (len(row) == 1):
				if orientation == "H":
					if (ord(row) + ship[1] > 65 + self.board.size):
						print("Your ship won't fit there, please try again.")
					else:
						break
				else:
					break
			else:
				print('Invalid input. Please try again.')

		# Prompt user for ship row




			

		
