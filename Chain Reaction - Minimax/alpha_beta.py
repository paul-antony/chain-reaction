#alpha-beta pruning function returns best move
import copy

def alpha_beta(b,depth = 3):
	return max_value(b,depth,-300,300)[1]

def max_value(b,depth,alpha,beta):
	moves = b.valid_move()
	if len(moves) == 0:
		return -1*b.cal_heuristics(),(0,0)
	if depth == 0:
		return -1*b.cal_heuristics(),(0,0)

	b_score = -300
	best_move = moves[0]
	
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = max(b_score,min_value(board,depth-1,alpha,beta)[0])

	
		if alpha < b_score:
			alpha = b_score
			best_move = pos

		if alpha >= beta:
			break

	return b_score,best_move



def min_value(b,depth,alpha,beta):
	moves = b.valid_move()
	if len(moves) == 0:
		return -1*b.cal_heuristics(),(0,0)
	if depth == 0:
		return -1*b.cal_heuristics(),(0,0)

	b_score = 300
	best_move = moves[0]
	
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = min(b_score,max_value(board,depth-1,alpha,beta)[0])
	
		if beta > b_score:
			beta = b_score
			best_move = pos

		if alpha >= beta:
			break

	return b_score,best_move
