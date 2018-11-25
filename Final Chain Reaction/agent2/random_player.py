import random


def random_move(board):
	valid_moves = board.valid_move()
	action = valid_moves[random.randrange(len(valid_moves))]
	return action