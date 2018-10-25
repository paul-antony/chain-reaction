
import copy

from DQN import *
from buffer import *
from board import *
from random_player import *
from alpha_beta import *

def train():
	network = QNetwork(input_dim, output_dim, lr, epsilon, epsilon_min, epsilon_decay)
	#network.save('weight_data.h5')
	network.load('weight_data.h5')

	board = Board()
	buffer = replay_byffer(alpha,gama)

	no_of_games = 1500

	while no_of_games> 0:#no of games to run
		game_over = False

		while game_over == False:#game loop

			#random player part
			buffer_entry = []

			board_state = board.list()
			player = board.player

			action = alpha_beta(board)

			Q_value = network.qvalue(board)
			

			buffer_entry.append(board_state)
			buffer_entry.append(replay_byffer.index_1d(action))
			buffer_entry.append(Q_value)
			buffer_entry.append(player)

			board.move(action)
			value = board.cal_heuristics()
			if value in (200,-200):
				buffer_entry.append(-1*board.player*value)
				buffer.push(copy.deepcopy(buffer_entry))
				game_over = True
				break
			buffer_entry.append(0)
			buffer.push(copy.deepcopy(buffer_entry))


			#network move
			buffer_entry = []


			action,Q_value = network.action_training(board)
			board_state = board.list()
			player = board.player

			buffer_entry.append(board_state)
			buffer_entry.append(replay_byffer.index_1d(action))
			buffer_entry.append(Q_value)
			buffer_entry.append(player)

			board.move(action)
			value = board.cal_heuristics()
			if value in (200,-200):
				buffer_entry.append(-1*board.player*value)
				buffer.push(copy.deepcopy(buffer_entry))
				game_over = True
				break
			
			buffer_entry.append(0)

			buffer.push(copy.deepcopy(buffer_entry))

		print("game remaining:",no_of_games)
		no_of_games = no_of_games - 1

		x, y = buffer.generate_data()
		network.train(x,y)
		network.save('weight_data.h5')

		board.reset()
		network.eps_update()
		buffer.reset()


if __name__ == "__main__":
	train()
