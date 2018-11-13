

import copy

from DQN import *
from buffer import *
from board import *
from random_player import *
from alpha_beta import *

def train():
	network = QNetwork()
	#network.save()
	#exit(0)
	network.load()

	board = Board()

	filename = 'BUFFER.pickle'
	infile = open(filename,'rb')
	buffer = pickle.load(infile)
	infile.close()

	no_of_games = 100

	while no_of_games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			buffer_entry = []

			board_state = board.list()
			player = board.player

			action = alpha_beta(board,2)

			

			buffer_entry.append(board_state)
			buffer_entry.append(player)
			buffer_entry.append(action)

			board.move(action)
			next_board = board.list()
			buffer_entry.append(next_board)


			value = board.cal_heuristics()
			if value in (200,-200):
				buffer_entry.append(-1*board.player)
				buffer.push(copy.deepcopy(buffer_entry))
				game_over = True
				break
			buffer_entry.append(0)
			buffer.push(copy.deepcopy(buffer_entry))


			#network move
			buffer_entry = []


			action = network.action_training(board)
			board_state = board.list()
			player = board.player

			buffer_entry.append(board_state)
			buffer_entry.append(player)
			buffer_entry.append(action)

			board.move(action)

			next_board = board.list()
			buffer_entry.append(next_board)


			value = board.cal_heuristics()
			if value in (200,-200):
				buffer_entry.append(-1*board.player)
				buffer.push(copy.deepcopy(buffer_entry))
				game_over = True
				break
			
			buffer_entry.append(0)

			buffer.push(copy.deepcopy(buffer_entry))

		print("game remaining:",no_of_games)
		no_of_games = no_of_games - 1

		buffer.train(32)

		outfile = open(filename,'wb')
		pickle.dump(buffer,outfile)
		outfile.close()


		#reset environment
		board.reset()
		buffer.reset()
		network.eps_update()
		network.load()




if __name__ == "__main__":
	train()
