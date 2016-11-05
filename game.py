from player import Player
from battleship import PIECES
from battleship import BOARD_SIZE
import pdb
from battleship import clear_screen


class Game:

	def __init__(self):
		print("Welcome to Battleship! Enjoy your match.")
		self.player1 = Player(input("Enter play 1's name: "))
		self.player2 = Player(input("Enter play 2's name: "))

		for player in self.player1, self.player2:
			player.draw_board()

		for player in self.player1, self.player2:
			player.place_ships()

	def start_turns(self):
		this_player = self.player1
		other_player = self.player2
		while True:
			print("{}'s board:".format(other_player.name))
			this_player.draw_opponent_board()
			this_player.draw_board()

			# Prompt the user for coordinates to fire at until they enter ones that exist in the other player's 
			# board and that they haven't already fired at.
			while True:
				print("{}, what coordinate would you like to fire at?".format(this_player.name))
				column = input('Column: ').strip().upper()
				row = input('Row: ')

				if (column not in [chr(i+65) for i in range(0, BOARD_SIZE)]):
						print('Input not within choices of columns. Please try again.')
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
					this_player.shots_taken[(column, row)] = PIECES['hit']
					ship.coords[(column, row)] = PIECES['hit']
					# If all of this ship's coordinates are hits, it is sunk
					# When that is the case, change it's pieces to sunk, set it to sunk, and update the 
					# coordinates in shots_taken
					if all(space == PIECES['hit'] for space in ship.coords.values()):
						print("You sank {}'s {}!".format(other_player.name, ship.name))
						ship.is_sunk = True;
						for (column, row) in ship.coords.keys():
							ship.coords[(column, row)] = PIECES['sunk']
							this_player.shots_taken[(column, row)] = PIECES['sunk']
					break
			else:
				clear_screen()
				input("Sorry {}, you missed! Please press enter and then hand off to {}.".format(this_player.name, other_player.name))
				clear_screen()
				this_player.shots_taken[(column, row)] = PIECES['miss']
				other_player.misses[(column, row)] = PIECES['miss']
				this_player, other_player = other_player, this_player
				clear_screen()
				input("{}, it's your turn. Press enter to continue.".format(this_player.name))
				clear_screen()

			if all(ship.is_sunk == True for ship in other_player.fleet):
				clear_screen()
				print("Congratulations {}, you sank all of {}'s ships! You win!".format(this_player.name, other_player.name))
				for player in self.player1, self.player2:
					player.draw_board()
				break


