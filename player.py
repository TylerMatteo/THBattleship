#from board import Board
from battleship import FLEET
from battleship import PIECES
from battleship import BOARD_SIZE
from ship import Ship
import pdb

class Player:

	board = {()}

	def __init__(self, name):
		self.name = name
		self.board = {(col, row): "0" for row in range (1, BOARD_SIZE+1) for col in [chr(64+l) for l in range(1, BOARD_SIZE+1)]}
		self.fleet = [Ship(ship[0], ship[1]) for ship in FLEET]

	def place_ships(self):
		for ship in self.fleet:
			while True:
				print("{}, please place your {}. It is {} spaces long.".format(self.name, ship.name, ship.size))

				# Prompt user for ship orientation
				while True:
					orientation = input("Would you like to place this ship (H)orizontally or (V)ertically? ").strip().upper()
					if (orientation == "H") or (orientation == "V"):
						break
					else:
						print('Invalid input. Please try again.')

				# Prompt user for ship column
				while True:
					
					column = input("Which column would you like the ship to start in? Please enter a letter A - {}. ".format(chr(64 + BOARD_SIZE))).strip().upper()

					# Validate input
					if (column not in [chr(i+65) for i in range(0, BOARD_SIZE)]):
						print('Input not within choices of column. Please try again.')
						continue
					# If this ship is horizontal, make sure it will fit
					elif orientation == "H":
						if (ord(column) - 65 + ship.size > BOARD_SIZE):
							print("Your ship won't fit there horizontally, it's too long! Please try again.")
							continue
					
					break

				# Prompt user for ship row
				while True:
					row = input("Which row would you like the ship to start in? Please enter a number 1 - {}. ".format(BOARD_SIZE)).strip()
					# Validate input
					if (row not in [str(i) for i in range(1, BOARD_SIZE+1)]):
						print('Input not within choices of rows. Please try again.')
						continue
					# If this ship is vertical, make sure it will fit
					elif orientation == "V":
						if (int(row) + ship.size - 1 > BOARD_SIZE):
							print("Your ship won't fit there vertically, it's too long! Please try again.")
							continue
					break

				overlap = False
				for placed_ship in self.fleet:
					if (column, row) in placed_ship.coords.keys():
						overlap = True
						print("Sorry, you can't place your {} there because it overlaps with your {}".format(ship.name, placed_ship.name))

				if overlap is not True:
					break

			if orientation == "H":
				ship.coords = {(chr(ord(column)+i), row): "0" for i in range(0, ship.size)}
			elif orientation == "v":
				ship.coords = {(column, str(int(row)+i)): "0" for i in range(0, ship.size)}






			

		
