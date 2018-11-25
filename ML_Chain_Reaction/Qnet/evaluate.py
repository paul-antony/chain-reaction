from DQN import *
from alpha_beta import *
from random_player import *
from board import *



network = QNetwork()


board = Board()
no_of_games = 50

#################################################################################################
def alpha1(depth = 2):

	games = no_of_games
	win = 0
	network.load(1)
	while games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			action = network.act(board)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				win = win+1
				break



			action = alpha_beta(board,depth)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				break

		board.reset()
		games = games -1
		print("alpha_",depth,":",games)
		
	return win

######################################################################################
def alpha2(depth = 2):

	games = no_of_games
	win = 0
	network.load(-1)
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

			
#############################################################################
def rand1():

	games = no_of_games
	win = 0
	network.load(1)
	while games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			action = network.act(board)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				win = win+1
				break


			action = random_move(board)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				break

		board.reset()
		games = games -1
		print("random:",games)
		
	return win
##############################################################################
def rand2():

	games = no_of_games
	win = 0
	network.load(-1)
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

##########################################################################################


