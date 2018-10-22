import random
import copy

from DQN import *
from buffer import *
from board import *


network = QNetwork(input_dim, output_dim, lr, epsilon, epsilon_min, epsilon_decay)
#network.save('weight_data.h5')
network.load('weight_data.h5')

board = Board()
buffer = replay_byffer(alpha,gama)

no_of_games = 100
win = 0
while no_of_games > 0:#no of games to run
	over = 0
	depth = 0
	while over == 0:#game loop

		#random player part
		buffer_entry = []

		board_state = board.list()
		player = board.player

		valid = board.valid_move()
		action = valid[random.randrange(len(valid))]

		Q_value = network.qvalue(board)
		

		buffer_entry.append(board_state)
		buffer_entry.append(replay_byffer.index_1d(action))
		buffer_entry.append(Q_value)
		buffer_entry.append(player)

		board.move(action)
		value = board.cal_heuristics()
		if value in (200,-200):
			buffer_entry.append(-200)
			buffer.push(copy.deepcopy(buffer_entry))
			over = 1
			break
		buffer_entry.append(0)
		buffer.push(copy.deepcopy(buffer_entry))

		depth = depth +1
		#network move
		buffer_entry = []


		action,Q_value = network.act_train(board)
		board_state = board.list()
		player = board.player

		buffer_entry.append(board_state)
		buffer_entry.append(replay_byffer.index_1d(action))
		buffer_entry.append(Q_value)
		buffer_entry.append(player)

		board.move(action)
		value = board.cal_heuristics()
		if value in (200,-200):
			buffer_entry.append(200)
			buffer.push(copy.deepcopy(buffer_entry))
			over = 1
			win = win +1
			break
		buffer_entry.append(0)
		buffer.push(copy.deepcopy(buffer_entry))

		depth = depth +1
	print("game remaining:",no_of_games)
	no_of_games = no_of_games - 1
	x, y = buffer.generate_data()
	board.reset()
	network.train(x,y)
	network.save('weight_data.h5')
	network.eps_update()
	buffer.reset()

print("wins:",win)

