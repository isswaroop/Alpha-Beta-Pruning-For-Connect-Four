import copy

# Board tokens
RED = 1
BLUE = 2

# A few helper functions to manage board initialisation
def new_empty_board(height, width):
    return [([0] * height) for k in range(width)]

def valid_board(board):
    # Checks that the board is a rectangle. If it isn't, this function raises
    # an exception which interupts the program.
    if len(board) == 0:
        raise InvalidBoard('The board has no space')
    else:
        l = len(board[0])
        if any(len(col) != l for col in board):
            raise InvalidBoard('Not all columns have the same heights')
        elif l == 0:
            raise InvalidBoard('The board has no space')


class Board():

    def __init__(self, board=None, rewards=None, winscore=100):
        if board == None:
            # If no board is passed explicitely, just create one
            board = new_empty_board(8, 9)
        self.field = board
        # This next line will crash the program if the provided board is wrong
        valid_board(self.field)
        self.width = len(self.field)
        self.height = len(self.field[0])
        if rewards == None:
            # The default rewards: [0, 1, 2, 4, 8, 16, 32, etc. ]
            rewards = [0] + [ 2 ** (n - 1) for n in range(1, max(self.width, self.height)) ]
        self.rewards = rewards
        self.winscore = winscore

    def col_height(self, col):
        l = 0
        for space in self.field[col]:
            if space != 0:
                l += 1
        return l

    def not_full_columns(self):
        # This method collects all the columns that are not full. This gives a
        # list of playable columns. It is useful for AIs.
        cs = []
        for col in range(self.width):
            if self.col_height(col) < self.height:
                cs.append(col)
        return cs

    def attempt_insert(self, col, token):
        # is it possible to insert into this column?
        if self.col_height(col) < self.height:

            # add a token in the selected column
            self.field[col][self.col_height(col)] = token
            # return True for success
            return True

        else:
            # return False for Failure
            return False

    def scoreGeneral(self, dirX, dirY, token):
        used_ls=[]
        score = 0 
        for row in range(self.height):
            inRun = False
            run_length = 0 
            for col in range(self.width):
                colcol = col
                rowrow = row
                if (colcol, rowrow) not in used_ls:
                    while colcol >= 0 and rowrow < self.height and colcol < self.width:
                        used_ls.append((colcol,rowrow))
                        if self.field[colcol][rowrow] is token and not inRun:
                            inRun = True
                        if self.field[colcol][rowrow] is token:
                            run_length += 1
                        else:
                            inRun = False
                            if run_length > 1:
                                score += self.rewards[run_length - 1]
                            run_length = 0 
                        colcol += dirX
                        rowrow += dirY
                    if inRun and run_length > 1:
                        score += self.rewards[run_length - 1]
                    inRun = False 
                    run_length = 0
        return score

    def score (self):
        red1 = (self.scoreGeneral(-1,1, 1))
        red2 = (self.scoreGeneral(1,0, 1))
        red3 = (self.scoreGeneral(1,1, 1))
        red4 = (self.scoreGeneral(0,1, 1))
        blue1 = (self.scoreGeneral(-1,1, 2))
        blue2 = (self.scoreGeneral(1,0, 2))
        blue3 = (self.scoreGeneral(1,1, 2))
        blue4 = (self.scoreGeneral(0,1, 2))

        red = red1 + red2 + red3 + red4
        blue = blue1 + blue2 + blue3 + blue4

        return(red, blue)

    def refresh_scores(self):
        (red, blue) = self.score(self.field_state)
            
    def is_full(self):
        full_board = all([self.col_height(n) == self.height for n in range(self.width)])
        return full_board

# This additional class simply creates an empty board of a given size.
# Note the `Board` between brackets (`(` and `)`). This means that the methods
# from the class `Board` are available in the class `EmptyBoard`. In other
# words, `EmptyBoard` is just a special case of the general case `Board`.
class EmptyBoard(Board):

    # Function to set up the objects of this class
    def __init__(self, height=8, width=9, rewards=None, winscore=100):
        # Create a simple empty board with the right height and width
        fresh_board = new_empty_board(height, width)
        # Then, proceed to set-up as in `Board`. The `super()` part refers to
        # the class `Board`.
        Board.__init__(self, fresh_board, rewards, winscore)