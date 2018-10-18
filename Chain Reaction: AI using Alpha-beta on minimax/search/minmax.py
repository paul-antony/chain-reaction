#minmax function returns best move
import copy

def minmax(b,depth=2):
	return max_value(b,depth)[1]

def max_value(b,depth):
	moves = b.valid_move()
	if len(moves) == 0:
		return -1*b.cal_heuristics(),0
	if depth == 0:
		return -1*b.cal_heuristics(),0
			
	best_val = -300
	best_move = moves[0]
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = min_value(board,depth-1)[0]
	
		if best_val < b_score:
			best_val = b_score
			best_move = pos
	    
	return best_val,best_move
			
def min_value(b,depth):
	moves = b.valid_move()
	if len(moves) == 0:
		return -1*b.cal_heuristics(),0
	if depth == 0:
		return -1*b.cal_heuristics(),0
			
	best_val = 300
	best_move = moves[0]
	for pos in moves:
		board = copy.deepcopy(b)
		board.move(pos)
		b_score = max_value(board,depth-1)[0]
	
	if best_val > b_score:
		best_val = b_score
		best_move = pos
	    
	return best_val,best_move
