from DQN import *
from alpha_beta import *
from random_player import *
from board import *



network = QNetwork(input_dim, output_dim, lr, epsilon, epsilon_min, epsilon_decay)
network.load('weight_data.h5')

board = Board()


def alpha():

	no_of_games = 1
	win = 0

	while no_of_games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			action = alpha_beta(board)
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
		no_of_games = no_of_games -1
		print("alpha:",no_of_games)
		
	return win

			


def rand():

	no_of_games = 100
	win = 0

	while no_of_games> 0:#no of games to run
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
		no_of_games = no_of_games -1
		print("random:",no_of_games)
		
	return win