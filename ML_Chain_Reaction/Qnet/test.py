from alpha_beta import *
from board import *



board = Board()
no_of_games = 50

def alpha():

	games = no_of_games
	win = 0

	while games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			action = alpha_beta(board,3)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				break


			action = alpha_beta(board,1)
			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				game_over = True
				win = win+1
				break

		board.reset()
		games = games -1
		print("alpha:",games)
		
	return win

print(alpha())
