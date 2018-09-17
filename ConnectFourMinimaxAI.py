import copy
import ConnectFourEngine
import ConnectFourBoard
import random

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

def max_play(board, token, ply_remaining, red_turn):
    moves = []
    available_moves = board.not_full_columns()
    random.shuffle(available_moves)
    for n in available_moves:
        newboard = copy.deepcopy(board)
        if (newboard.col_height(n) < newboard.height):
            newboard.attempt_insert(n, token)
            if ply_remaining <= 0 or newboard.is_full():
                value = state_score(newboard, token==ConnectFourBoard.RED)
            else: 
                (min_move, value) = min_play(newboard, other(token), ply_remaining -1, red_turn )
            moves.append((n, value))
    best_move = max(moves, key = lambda x: x[1])
    return best_move

def min_play(board, token, ply_remaining, red_turn):
    moves = []
    available_moves = board.not_full_columns()
    random.shuffle(available_moves)
    for n in available_moves:
        newboard = copy.deepcopy(board)
        if (newboard.col_height(n) < newboard.height):
            newboard.attempt_insert(n, token)
            if ply_remaining <= 0 or newboard.is_full():
                value = state_score(newboard, token==ConnectFourBoard.RED)
            else: 
                (max_move, value) = max_play(newboard, other(token), ply_remaining-1, red_turn ) # the highest possible move you can get for this column
            moves.append((n, value))
    best_move = min(moves, key = lambda x: x[1])
    return best_move

def AIcheck(board, token, red_turn):
    ply_remaining = 4
    (move, value) = max_play(board, token, ply_remaining, red_turn)
    return move

