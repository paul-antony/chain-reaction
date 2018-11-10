import copy
import random
from agent1.board import *

def alpha_beta(board, player):
	depth = 3
	alpha = -300
	beta = 300
	b = Board(board, player)
	moves = b.valid_moves()
	random.shuffle(moves)
	b_score = -300
	best_move = moves[0]
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = max(b_score, min_value(board, depth-1, alpha, beta, player))
		if alpha < b_score:
			alpha = b_score
			best_move = pos
		if alpha >= beta:
			break
	return best_move

def max_value(b, depth, alpha, beta, player):
	moves = b.valid_moves()
	if len(moves) == 0:
		return b.cal_heuristics()
	if depth == 0:
		return b.cal_heuristics()
	b_score = -300
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = max(b_score, min_value(board, depth-1, alpha, beta, player))
		alpha = max(alpha, b_score)
		if alpha >= beta:
			break
	return b_score

def min_value(b, depth, alpha, beta, player):
	moves = b.valid_moves()
	if len(moves) == 0:
		return b.cal_heuristics()
	if depth == 0:
		return b.cal_heuristics()
	b_score = 300
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = min(b_score, max_value(board, depth-1, alpha, beta, player))
		beta = min(beta, b_score)
		if alpha >= beta:
			break
	return b_score
