from player import Player

class Game:

	def __init__(self):
		print("Welcome to Battleship! Enjoy your match.")
		self.players = []
		self.players.append(Player(input("Enter play 1's name: ")))
		self.players.append(Player(input("Enter play 2's name: ")))

		for player in self.players:
			player.board.print_heading()
			player.board.print_grid()
			print()

		for player in self.players:
			"{}, please place your fleet. Ships are laid out to the right when horizontal and downward when vertical.".format(player.name)
			for ship in player.fleet:
				player.place_ship(ship)

			# player.board.print_heading()
			# player.board.print_grid()


