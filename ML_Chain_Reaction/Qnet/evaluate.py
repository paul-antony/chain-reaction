from DQN import *
from alpha_beta import *
from random_player import *
from board import *



network = QNetwork()
network.load()

board = Board()
no_of_games = 100

def alpha(depth = 2):

	games = no_of_games
	win = 0

	while games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			action = alpha_beta(board,depth)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				break


			action = network.act(board)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				win = win+1
				break

		board.reset()
		games = games -1
		print("alpha_",depth,":",games)
		
	return win

			


def rand():

	games = no_of_games
	win = 0

	while games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			action = random_move(board)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				break


			action = network.act(board)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				win = win+1
				break
		board.reset()
		games = games -1
		print("random:",games)
		
	return win
