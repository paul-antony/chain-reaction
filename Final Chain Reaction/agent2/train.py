
import copy

from DQN import *
from buffer import *
from board import *
from random_player import *
from alpha_beta import *

def train(player):
	network = QNetwork()
	#network.save()
	#buffer.reset()
	#exit(0)
	network.load(player)
	if player == 1:
		filename = 'Buffer_Player1.pickle'
	else:
		filename = 'Buffer_Player2.pickle'

	infile = open(filename,'rb')
	buffer = pickle.load(infile)
	infile.close()

	board = Board()
	

	no_of_games = 50

	while no_of_games> 0:#no of games to run
		game_over = False

		if player != 1:
			action = alpha_beta(board,2)
			board.move(action)

		while game_over == False:#game loop

			#network move

			buffer_entry = []


			action = network.action_training(board)

			valid_moves = board.valid_move()
			
			if action not in valid_moves:
				board_state = board.list()
				player = board.player

				buffer_entry.append(board_state)
				buffer_entry.append(player)
				buffer_entry.append(action)
				buffer_entry.append(board_state)								
				buffer_entry.append(-0.5)
				buffer.push(copy.deepcopy(buffer_entry))
				buffer_entry = []

				
				action = valid_moves[random.randrange(len(valid_moves))]

			
			board_state = board.list()
			player = board.player

			buffer_entry.append(board_state)
			buffer_entry.append(player)
			buffer_entry.append(action)

			board.move(action)

			value = board.cal_heuristics()
			if value in (200,-200):
				next_board = board.list()
				buffer_entry.append(next_board)
				buffer_entry.append(1)
				buffer.push(copy.deepcopy(buffer_entry))
				game_over = True
				break



			action = alpha_beta(board,2)

			board.move(action)
			next_board = board.list()
			buffer_entry.append(next_board)


			value = board.cal_heuristics()
			if value in (200,-200):
				buffer_entry.append(-1)
				buffer.push(copy.deepcopy(buffer_entry))
				game_over = True
				break


			buffer_entry.append(0)
			buffer.push(copy.deepcopy(buffer_entry))



			


		print("player ",player," game remaining:",no_of_games)
		no_of_games = no_of_games - 1

		buffer.train(400,player)

		outfile = open(filename,'wb')
		pickle.dump(buffer,outfile)
		outfile.close()

		#reset environment
		board.reset()

		network.eps_update()
		network.load(player)



if __name__ == "__main__":
	network = QNetwork()
	network.save()
