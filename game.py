from player import Player

class Game:

	def __init__(self):
		print("Welcome to Battleship! Enjoy your match.")
		self.player1 = Player(input("Enter play 1's name: "))
		self.player2 = Player(input("Enter play 2's name: "))


		for player in self.player1, self.player2:
			#player.board.print_heading()
			#player.board.print_grid()
			print()

			# for ship in player.fleet:
			# 	print(ship.name)

			player.place_ships()


		# for player in self.player1, self.player2:
		# 	"{}, please place your fleet. Ships are laid out to the right when horizontal and downward when vertical.".format(player.name)
		# 	for ship in player.fleet:
		# 		player.place_ship(ship)

			# player.board.print_heading()
			# player.board.print_grid()


