import copy



def minmax(b,depth=3):

        moves = b.valid_move()
        if len(moves) == 0:
                return b.cal_heuristics(),0
        if depth == 1:
                return b.cal_heuristics(),0

    
        if b.player == 1:
                best_val = -300
                best_move = moves[0]
                for pos in moves:
                        board = copy.deepcopy(b)
                        board.move(pos)
                        b_score = minmax(board,depth-1)[0]
                        if best_val < b_score:
                                best_val = b_score
                                best_move = pos
                return best_val,best_move
    
        if b.player == -1:
                best_val = 300
                best_move = moves[0]
                for pos in moves:
                        board = copy.deepcopy(b)
                        board.move(pos)
                        b_score = minmax(board,depth-1)[0]
                        if best_val > b_score:
                                best_val = b_score
                                best_move = pos
                return best_val,best_move 
