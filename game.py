from player import Player

class Game:

	def __init__(self):
		print("Welcome to Battleship! Enjoy your match.")
		self.player1 = Player(input("Enter play 1's name: "))
		self.player2 = Player(input("Enter play 2's name: "))
