#
#  Adapted from https://github.com/aimacode/aima-python/blob/master/games.py
#
import time
from .game import Game
from sys import maxsize

infinity = float('inf')


class TimeoutReached(Exception):
    pass


def evalfn(board):
    score = 0
    vectors = board.rows + board.columns + board.diagonals

    maxes_turn = board.is_maxes_turn

    for v in vectors:

        even, odd = board.count_even_odd(v)

        if even == 2 and odd == 1:
            if maxes_turn:
                score += 10
            else:
                score -= 10

        if odd == 3 and even == 0:
            if maxes_turn:
                score += 10

        if even == 3 and odd == 0:
            if not maxes_turn:
                score -= 10

        if 0 < even < 3:
            score += 3

        if even == 1 and maxes_turn:
            score += 3

        if even == 1 and odd == 1 and maxes_turn:
            score -= 7

    return score


def iterative_deepening_alphabeta(state):
    game = Game
    start_time = time.time()

    best_action = None
    best_score = -infinity

    for depth in range(0, maxsize):
        try:
            best_action, best_score = alphabeta_cutoff_search(state, game, start_time, depth, eval_fn=evalfn)
        except TimeoutReached:
            print('Timeout reached')
            break

    print('Depth: {}, Best move: {}, Best score: {}'.format(depth-1, best_action, best_score))
    return best_action


def alphabeta_cutoff_search(state, game, start_time, d, reached_cutoff=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""
    TIMEOUT = 2  # seconds

    player = game.to_move(state)  # will return 'MAX' or 'MIN'

    def max_value(state, alpha, beta, depth):
        if (time.time() - start_time) >= TIMEOUT:
            raise TimeoutReached('Timeout reached')
        if game.is_terminal(state):
            return game.utility(state, player)
        elif reached_cutoff(depth):
            return eval_fn(state)

        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if (time.time() - start_time) >= TIMEOUT:
            raise TimeoutReached('Timeout reached')
        if game.is_terminal(state):
            return game.utility(state, player)
        elif reached_cutoff(depth):
            return eval_fn(state)

        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    reached_cutoff = (reached_cutoff or
                      (lambda depth: depth > d))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a

    return best_action, best_score
