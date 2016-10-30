from player import Player
from battleship import PIECES
from battleship import BOARD_SIZE
import pdb

class Game:

	def place_ships(self):
		print("Welcome to Battleship! Enjoy your match.")
		self.player1 = Player(input("Enter play 1's name: "))
		self.player2 = Player(input("Enter play 2's name: "))

		# for player in self.player1, self.player2:
		# 	player.place_ships()
		# 	player.draw_board()

		self.player1.place_ships()
		self.player1.draw_board()
		self.player2.place_ships()
		self.player2.draw_board()


	def start_turns(self):
		this_player = self.player1
		other_player = self.player2
		while True:

			# Prompt the user for coordinates to fire at until they enter ones that exist in the other player's 
			# board and that they haven't already fired at.
			while True:
				print("{}, what coordinate would you like to fire at?".format(this_player.name))
				column = input('Column: ').strip().upper()
				row = input('Row: ')

				if (column not in [chr(i+65) for i in range(0, BOARD_SIZE)]):
						print('Input not within choices of column. Please try again.')
						continue
				elif (row not in [str(i) for i in range(1, BOARD_SIZE+1)]):
						print('Input not within choices of rows. Please try again.')
						continue
				elif (column, row) in this_player.shots_taken.keys():
					print("You've already shot there, please try again.")
					continue
				else:
					break


			# See if the given coordinate exists in the any of the other player's ship's coordinates
			for ship in other_player.fleet:
				if (column, row) in ship.coords.keys():
					print("Hit!")
					pdb.set_trace()
					this_player.shots_taken[(column, row)] = PIECES['hit']
					ship.coords[(column, row)] = PIECES['hit']
					if all(space == PIECES['hit'] for space in ship.coords.values()):
						print("You sank {}'s {}!".format(other_player.name, ship.name))
						ship.is_sunk = True;
					break
			else:
				print("Miss!")
				print(other_player.shots_taken, this_player.shots_taken)
				pdb.set_trace()
				#this_player.shots_taken[(column, row)] = PIECES['miss']
				self.player1.shots_taken[(column, row)] = PIECES['miss']
				print(other_player.shots_taken, this_player.shots_taken)
				this_player, other_player = other_player, this_player

			if all(ship.is_sunk == True for ship in other_player.fleet):
				print("Congratulations {}, you sank all of {}'s ships! You win!".format(this_player.name, other_player.name))
				break


