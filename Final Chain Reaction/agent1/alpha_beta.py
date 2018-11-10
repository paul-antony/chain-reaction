import copy
import random
from agent1.board import *

def alpha_beta(board, player):
	depth = 5
	alpha = -300
	beta = 300
	moves = valid_moves(board, player)
	random.shuffle(moves)
	b_score = -300
	best_move = moves[0]
	for pos in moves:
		old_board = copy.deepcopy(board)
		move(board, player, pos)
		b_score = max(b_score, min_value(board, depth-1, alpha, beta, player))
		if alpha < b_score:
			alpha = b_score
			best_move = pos
		if alpha >= beta:
			break
	return best_move

def max_value(board, depth, alpha, beta, player):
	moves = valid_moves(board, player)
	if len(moves) == 0:
		return cal_heuristics(board, player)
	if depth == 0:
		return cal_heuristics(board, player)
	b_score = -300
	for pos in moves:
		old_board = copy.deepcopy(board)
		move(board, player, pos)
		b_score = max(b_score, min_value(board, depth-1, alpha, beta, player))
		alpha = max(alpha, b_score)
		if alpha >= beta:
			break
	return b_score

def min_value(board, depth, alpha, beta, player):
	moves = valid_moves(board, player)
	if len(moves) == 0:
		return cal_heuristics(board, player)
	if depth == 0:
		return cal_heuristics(board, player)
	b_score = 300
	for pos in moves:
		old_board = copy.deepcopy(board)
		move(board, player, pos)
		b_score = min(b_score, max_value(board, depth-1, alpha, beta, player))
		beta = min(beta, b_score)
		if alpha >= beta:
			break
	return b_score
