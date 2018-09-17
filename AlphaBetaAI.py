import copy
import ConnectFourEngine
import ConnectFourBoard
import math
import random

p_inf = float("inf")
n_inf = float("-inf")

def other(token):
    if token == ConnectFourBoard.RED:
        return ConnectFourBoard.BLUE
    elif token == ConnectFourBoard.BLUE:
        return ConnectFourBoard.RED 
    else:
        return None

def state_score(board, red_turn):
    (score_red, score_blue) = board.score()
    if red_turn:
        return score_red - score_blue
    else:
        return score_blue - score_red
def max_play(board, token, ply_remaining, red_turn, alpha, beta):
    (best_move, value) = (None, n_inf)
    available_moves = board.not_full_columns()
    random.shuffle(available_moves)
    for n in available_moves:
        newboard = copy.deepcopy(board)
        if (newboard.col_height(n) < newboard.height):
            newboard.attempt_insert(n, token)
            if ply_remaining <= 0 or newboard.is_full():
                value_child = state_score(newboard, red_turn)
            else: 
                (min_move, value_child) = min_play(newboard, other(token), ply_remaining-1, red_turn, alpha, beta)
            if value < value_child: 
                (best_move, value) = (n, value_child)
            alpha = max(alpha, value_child)
            if alpha >= beta: return (best_move, alpha)
    return (best_move, alpha)

def min_play(board, token, ply_remaining, red_turn, alpha, beta):
    (best_move, value) = (None, p_inf)
    available_moves = board.not_full_columns()
    random.shuffle(available_moves)
    for n in available_moves:
        newboard = copy.deepcopy(board)
        if (newboard.col_height(n) < newboard.height):
            newboard.attempt_insert(n, token)
            if ply_remaining <= 0 or newboard.is_full():
                value_child = state_score(newboard, red_turn)
            else: 
                (max_move, value_child) = max_play(newboard, other(token), ply_remaining-1, red_turn, alpha, beta) # the highest possible move you can get for this column
            if value > value_child: 
                 (best_move, value) = (n, value_child)
            beta = min(beta, value_child)
            if alpha >= beta: return (best_move, beta)
    return (best_move, beta)

def AIcheck(board, token, red_turn):
    ply_remaining = 4
    (move, value) = max_play(board, token, ply_remaining, red_turn, alpha=n_inf, beta=p_inf,) #change not red_turn to not human_turn
    return move
