# Name: Casey Hawkins
# Date: 06/03/2020
# Description: Gess, an abstract board game combining Go and Chess. Black and White each have 43 stones on their
# respective halves of an 18x18 board. Each player takes turns moving a 3x3 "piece", consisting of at least one of their
# stones and none of their opponent's stones, utilizing rules laid out in the GessGame class' check functions, with a
# goal to remove any and all of their opponent's rings, a 3x3 piece consisting of 8 stones surrounding an empty center.
# First to remove their opponent's rings wins.


class GessGame:
    """
    Gess, an abstract board game combining Go and Chess. Black and White each have 43 stones on their
    respective halves of an 18x18 board. Each player takes turns moving a 3x3 "piece", consisting of at least one of
    their stones and none of their opponent's stones, utilizing rules laid out in the GessGame class' check functions,
    with a goal to remove any and all of their opponent's rings, a 3x3 piece consisting of 8 stones surrounding an empty
    center. First to remove their opponent's rings wins.
    """

    def __init__(self):
        """
        Game initializes in UNFINISHED state, begins on BLACK's turn, and creates labelled 22x22 game area with all
        43 of each player's pieces in place on the 18x18 board.
        """

        # Game starts in UNFINISHED state
        self._game_state = 'UNFINISHED'

        # BLACK takes the first turn.
        self._game_turn = 'BLACK'

        # Create a 20x20 board
        self._board = [['-' for x in range(21)] for y in range(20)]

        # Add a row to label each column with a letter
        self._board.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', '-'])

        # Add a column to label each row with a number
        self._board[0][20] = '20'
        self._board[1][20] = '19'
        self._board[2][20] = '18'
        self._board[3][20] = '17'
        self._board[4][20] = '16'
        self._board[5][20] = '15'
        self._board[6][20] = '14'
        self._board[7][20] = '13'
        self._board[8][20] = '12'
        self._board[9][20] = '11'
        self._board[10][20] = '10'
        self._board[11][20] = '9'
        self._board[12][20] = '8'
        self._board[13][20] = '7'
        self._board[14][20] = '6'
        self._board[15][20] = '5'
        self._board[16][20] = '4'
        self._board[17][20] = '3'
        self._board[18][20] = '2'
        self._board[19][20] = '1'

        # Place all 43 of WHITE's pieces
        self._board[1][2] = 'w'
        self._board[1][4] = 'w'
        self._board[1][6] = 'w'
        self._board[1][7] = 'w'
        self._board[1][8] = 'w'
        self._board[1][9] = 'w'
        self._board[1][10] = 'w'
        self._board[1][11] = 'w'
        self._board[1][12] = 'w'
        self._board[1][13] = 'w'
        self._board[1][15] = 'w'
        self._board[1][17] = 'w'
        self._board[2][1] = 'w'
        self._board[2][2] = 'w'
        self._board[2][3] = 'w'
        self._board[2][5] = 'w'
        self._board[2][7] = 'w'
        self._board[2][8] = 'w'
        self._board[2][9] = 'w'
        self._board[2][10] = 'w'
        self._board[2][12] = 'w'
        self._board[2][14] = 'w'
        self._board[2][16] = 'w'
        self._board[2][17] = 'w'
        self._board[2][18] = 'w'
        self._board[3][2] = 'w'
        self._board[3][4] = 'w'
        self._board[3][6] = 'w'
        self._board[3][7] = 'w'
        self._board[3][8] = 'w'
        self._board[3][9] = 'w'
        self._board[3][10] = 'w'
        self._board[3][11] = 'w'
        self._board[3][12] = 'w'
        self._board[3][13] = 'w'
        self._board[3][15] = 'w'
        self._board[3][17] = 'w'
        self._board[6][2] = 'w'
        self._board[6][5] = 'w'
        self._board[6][8] = 'w'
        self._board[6][11] = 'w'
        self._board[6][14] = 'w'
        self._board[6][17] = 'w'

        # Place all 43 of BLACK's pieces
        self._board[18][17] = 'b'
        self._board[18][15] = 'b'
        self._board[18][13] = 'b'
        self._board[18][12] = 'b'
        self._board[18][11] = 'b'
        self._board[18][10] = 'b'
        self._board[18][9] = 'b'
        self._board[18][8] = 'b'
        self._board[18][7] = 'b'
        self._board[18][6] = 'b'
        self._board[18][4] = 'b'
        self._board[18][2] = 'b'
        self._board[17][18] = 'b'
        self._board[17][17] = 'b'
        self._board[17][16] = 'b'
        self._board[17][14] = 'b'
        self._board[17][12] = 'b'
        self._board[17][10] = 'b'
        self._board[17][9] = 'b'
        self._board[17][8] = 'b'
        self._board[17][7] = 'b'
        self._board[17][5] = 'b'
        self._board[17][3] = 'b'
        self._board[17][2] = 'b'
        self._board[17][1] = 'b'
        self._board[16][17] = 'b'
        self._board[16][15] = 'b'
        self._board[16][13] = 'b'
        self._board[16][12] = 'b'
        self._board[16][11] = 'b'
        self._board[16][10] = 'b'
        self._board[16][9] = 'b'
        self._board[16][8] = 'b'
        self._board[16][7] = 'b'
        self._board[16][6] = 'b'
        self._board[16][4] = 'b'
        self._board[16][2] = 'b'
        self._board[13][17] = 'b'
        self._board[13][14] = 'b'
        self._board[13][11] = 'b'
        self._board[13][8] = 'b'
        self._board[13][5] = 'b'
        self._board[13][2] = 'b'

    def print_Board(self):
        """
        Print the game board
        """

        for x in range(len(self._board)):
            print(self._board[x])

    def get_game_state(self):
        """
        Returns current state of the game. Can be UNFINISHED, BLACK_WON, or WHITE_WON.
        """

        return self._game_state

    def get_player_turn(self):
        """
        Get method for player's turn.
        """

        return self._game_turn

    def next_player_turn(self):
        """
        Changes the turn to the next player.
        """

        if self._game_turn == 'BLACK':
            self._game_turn = 'WHITE'
        else:
            self._game_turn = 'BLACK'

    def resign_game(self):
        """
        Allows current players to concede the game, giving the other player the win
        """

        if self._game_turn == 'BLACK':
            print("BLACK resigns. WHITE wins!")
            self._game_state = 'WHITE_WON'
        else:
            print("WHITE resigns. BLACK wins!")
            self._game_state = 'BLACK_WON'

    def convert_column(self, column):
        """
        Converts a column from a letter to its corresponding number.
        """

        if column.lower() == 'a':
            column = 1
        elif column.lower() == 'b':
            column = 2
        elif column.lower() == 'c':
            column = 3
        elif column.lower() == 'd':
            column = 4
        elif column.lower() == 'e':
            column = 5
        elif column.lower() == 'f':
            column = 6
        elif column.lower() == 'g':
            column = 7
        elif column.lower() == 'h':
            column = 8
        elif column.lower() == 'i':
            column = 9
        elif column.lower() == 'j':
            column = 10
        elif column.lower() == 'k':
            column = 11
        elif column.lower() == 'l':
            column = 12
        elif column.lower() == 'm':
            column = 13
        elif column.lower() == 'n':
            column = 14
        elif column.lower() == 'o':
            column = 15
        elif column.lower() == 'p':
            column = 16
        elif column.lower() == 'q':
            column = 17
        elif column.lower() == 'r':
            column = 18
        elif column.lower() == 's':
            column = 19
        elif column.lower() == 't':
            column = 20

        return column

    def convert_row(self, row):
        """
        Converts a row's labelled row position to its actual position on the board.
        """

        row = int(row)

        if row == 20:
            row = 1
        elif row == 19:
            row = 2
        elif row == 18:
            row = 3
        elif row == 17:
            row = 4
        elif row == 16:
            row = 5
        elif row == 15:
            row = 6
        elif row == 14:
            row = 7
        elif row == 13:
            row = 8
        elif row == 12:
            row = 9
        elif row == 11:
            row = 10
        elif row == 10:
            row = 11
        elif row == 9:
            row = 12
        elif row == 8:
            row = 13
        elif row == 7:
            row = 14
        elif row == 6:
            row = 15
        elif row == 5:
            row = 16
        elif row == 4:
            row = 17
        elif row == 3:
            row = 18
        elif row == 2:
            row = 19
        elif row == 1:
            row = 20

        return row

    def check_current_piece(self, cp_row, cp_col):
        """
        Check if selected 3x3 is legal.
        Current piece cannot include any opponent's stones in its 3x3 grid.
        """

        center = self._board[cp_row][cp_col]
        north = self._board[cp_row - 1][cp_col]
        south = self._board[cp_row + 1][cp_col]
        east = self._board[cp_row][cp_col + 1]
        west = self._board[cp_row][cp_col - 1]
        north_east = self._board[cp_row - 1][cp_col + 1]
        north_west = self._board[cp_row - 1][cp_col - 1]
        south_east = self._board[cp_row + 1][cp_col + 1]
        south_west = self._board[cp_row + 1][cp_col - 1]

        if self._game_turn == 'BLACK':

            if center == 'w' or north == 'w' or south == 'w' or east == 'w' or west == 'w' or north_east == 'w' or \
                    north_west == 'w' or south_east == 'w' or south_west == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if center == 'b' or north == 'b' or south == 'b' or east == 'b' or west == 'b' or north_east == 'b' or \
                    north_west == 'b' or south_east == 'b' or south_west == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if center == north == south == east == west == north_east == north_west == south_east == south_west == '-':
            print("Invalid move: 3x3 piece must contain at least one of your stones.")

            return False

        if center == ('b' or 'w') and north == south == east == west == north_east == north_west == south_east == \
                south_west == '-':
            print("Invalid move: 3x3 piece cannot only contain one stone located in the center.")

            return False

        for x in range(0, 21):

            if (cp_row == 0 and cp_col == x) or (cp_row == 19 and cp_col == x) or (cp_row == 20 and cp_col == x) or \
                    (cp_row == x and cp_col == 0) or (cp_row == x and cp_col == 19) or (cp_row == x and cp_col == 20):
                print("Invalid move: center cannot be out of bounds.")

                return False

        return True

    def check_move_amount(self, cp_row, cp_col, tp_row, tp_col):
        """
        Calculates amount being moved.
        Pieces must move; they cannot be "moved" to their current location.
        If center stone is present, piece can move until it encounters another piece or goes over 18x18 board bounds.
        If center stone is not present, piece can move up to 3 spaces, unless it encounters another piece or goes over
        18x18 board bounds.
        """

        # Calculate row_moves
        row_moves = abs(tp_row - cp_row)

        # Calculates col_moves
        col_moves = abs(tp_col - cp_col)

        # If [cp_row][cp_col] doesn't move, return False
        if cp_row == tp_row and cp_col == tp_col:
            print("Invalid move: center must move.")

            return False

        # If the center is empty, can only move a max of 3 spaces
        if self._board[cp_row][cp_col] == '-':

            if row_moves > 3 or col_moves > 3:
                print("Invalid move: center is empty, so max movement is only 3 spaces.")

                return False

        return True

    def check_move_direction(self, cp_row, cp_col, tp_row, tp_col):
        """
        Check if center moves out of bounds.
        Check if the attempted direction of movement is allowed: pieces can only be moved in a direction if a stone is
        located in that direction in the perimeter of 3x3 piece.
        """

        center = self._board[cp_row][cp_col]
        north = self._board[cp_row - 1][cp_col]
        south = self._board[cp_row + 1][cp_col]
        east = self._board[cp_row][cp_col + 1]
        west = self._board[cp_row][cp_col - 1]
        north_east = self._board[cp_row - 1][cp_col + 1]
        north_west = self._board[cp_row - 1][cp_col - 1]
        south_east = self._board[cp_row + 1][cp_col + 1]
        south_west = self._board[cp_row + 1][cp_col - 1]

        row_moves = abs(tp_row - cp_row)
        col_moves = abs(tp_col - cp_col)

        # Check if center moves out of bounds
        for x in range(0, 21):

            if (tp_row == 0 and tp_col == x) or (tp_row == 19 and tp_col == x) or (tp_row == 20 and tp_col == x) or \
                    (tp_row == x and tp_col == 0) or (tp_row == x and tp_col == 19) or (tp_row == x and tp_col == 20):
                print("Invalid move: center cannot move out of bounds.")

                return False

        # Check if, when moving diagonally, the row and col moves are equivalent (move in straight, diagonal lines)
        if row_moves != col_moves and row_moves != 0 and col_moves != 0:
            print("If moving diagonally, row and column advances must be the same number.")

            return False

        # Check movement north
        if (tp_col == cp_col) and (tp_row < cp_row) and north == '-':
            print("Invalid move: cannot move north without a stone located north in 3x3 piece.")

            return False

        # Check movement south
        if (tp_col == cp_col) and (tp_row > cp_row) and south == '-':
            print("Invalid move: cannot move south without a stone located south in 3x3 piece.")

            return False

        # Check movement east
        if (tp_col > cp_col) and (tp_row == cp_row) and east == '-':
            print("Invalid move: cannot move east without a stone located east in 3x3 piece.")

            return False

        # Check movement west
        if (tp_col < cp_col) and (tp_row == cp_row) and west == '-':
            print("Invalid move: cannot move west without a stone located west in 3x3 piece.")

            return False

        # Check movement northeast
        if (tp_col > cp_col) and (tp_row < cp_row) and north_east == '-':
            print("Invalid move: cannot move northeast without a stone located northeast in 3x3 piece.")

            return False

        # Check movement northwest
        if (tp_col < cp_col) and (tp_row < cp_row) and north_west == '-':
            print("Invalid move: cannot move northwest without a stone located northwest in 3x3 piece.")

            return False

        # Check movement southeast
        if (tp_col > cp_col) and (tp_row > cp_row) and south_east == '-':
            print("Invalid move: cannot move southeast without a stone located southeast in 3x3 piece.")

            return False

        # Check movement southwest
        if (tp_col < cp_col) and (tp_row > cp_row) and south_west == '-':
            print("Invalid move: cannot move southwest without a stone located southwest in 3x3 piece.")

            return False

        return True

    def check_obstructions(self, cp_row, cp_col, tp_row, tp_col):
        """
        Check if attempted move stops when an obstruction is encountered.
        Obstructions include any of the current player's stones, the opponent's stones, or the boundaries of the
        18x18 board.
        Obstructions can be overlapped by 3x3 piece, but must stop there, and cannot overlap more than one row or column
        of the 3x3 piece.
        """

        row_moves = int(tp_row - cp_row)

        col_moves = int(tp_col - cp_col)

        # Create a temporary board mirroring the actual board
        temp_board = []

        for i in self._board:
            temp_board.append(list(i))

        # Check movement South
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        if tp_row > cp_row and tp_col == cp_col:

            for x in range(0, abs(row_moves)):

                for y in range(-1, 2):

                    if temp_board[cp_row + 2 + x][cp_col + y] == 'b' or temp_board[cp_row + 2 + x][cp_col + y] == 'w':
                        temp_board[cp_row + 2 + x][cp_col + y] = 'X'

                    if temp_board[cp_row + 1 + x][cp_col + y] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement North
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row < cp_row and tp_col == cp_col:

            for x in range(0, abs(row_moves)):

                for y in range(-1, 2):

                    if temp_board[cp_row - 2 - x][cp_col + y] == 'b' or temp_board[cp_row - 2 - x][cp_col + y] == 'w':
                        temp_board[cp_row - 2 - x][cp_col + y] = 'X'

                    if temp_board[cp_row - 1 - x][cp_col + y] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement West
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row == cp_row and tp_col < cp_col:

            for x in range(0, abs(col_moves)):

                for y in range(-1, 2):

                    if temp_board[cp_row + y][cp_col - 2 - x] == 'b' or temp_board[cp_row + y][cp_col - 2 - x] == 'w':
                        temp_board[cp_row + y][cp_col - 2 - x] = 'X'

                    if temp_board[cp_row + y][cp_col - 1 - x] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement East
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row == cp_row and tp_col > cp_col:

            for x in range(0, abs(col_moves)):

                for y in range(-1, 2):

                    if temp_board[cp_row + y][cp_col + 2 + x] == 'b' or temp_board[cp_row + y][cp_col + 2 + x] == 'w':
                        temp_board[cp_row + y][cp_col + 2 + x] = 'X'

                    if temp_board[cp_row + y][cp_col + 2 + x] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement Northwest
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row < cp_row and tp_col < cp_col:

            for x in range(0, abs(col_moves)):

                for y in range(0, 3):

                    if temp_board[cp_row - 2 - x][cp_col - 2 - x] == 'b' or temp_board[cp_row - 2 - x][
                        cp_col - 2 - x] == 'w' or temp_board[cp_row - y][cp_col - 2 - x] == 'b' or \
                            temp_board[cp_row - y][
                                cp_col - 2 - x] == 'w':
                        temp_board[cp_row - 2 - x][cp_col - 2 - x] = 'X'

                    if temp_board[cp_row - 1 - x][cp_col - 1 - x] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement Northeast
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row < cp_row and tp_col > cp_col:

            for x in range(0, abs(col_moves)):

                for y in range(0, 3):

                    if temp_board[cp_row - 2 - x][cp_col + 2 + x] == 'b' or temp_board[cp_row - 2 - x][
                        cp_col + 2 + x] == 'w' or temp_board[cp_row - y][cp_col + 2 + x] == 'b' or \
                            temp_board[cp_row - y][
                                cp_col + 2 + x] == 'w':
                        temp_board[cp_row - 2 - x][cp_col + 2 + x] = 'X'

                    if temp_board[cp_row - 1 - x][cp_col + 1 + x] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement Southwest
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row > cp_row and tp_col < cp_col:

            for x in range(0, abs(col_moves)):

                for y in range(0, 3):

                    if temp_board[cp_row + 2 + x][cp_col - 2 - x] == 'b' or temp_board[cp_row + 2 + x][
                        cp_col - 2 - x] == 'w' or temp_board[cp_row + y][cp_col - 2 - x] == 'b' or \
                            temp_board[cp_row + y][
                                cp_col - 2 - x] == 'w':
                        temp_board[cp_row + 2 + x][cp_col - 2 - x] = 'X'

                    if temp_board[cp_row + 1 + x][cp_col - 1 - x] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

        # Check movement Southeast
        # Check the area being moved to: if there is a stone in the way of movement, and overlap occurs over more than
        # one row or column of the piece being moved, return False
        elif tp_row > cp_row and tp_col > cp_col:

            for x in range(0, abs(col_moves)):

                for y in range(0, 3):

                    if temp_board[cp_row + 2 + x][cp_col + 2 + x] == 'b' or temp_board[cp_row + 2 + x][
                        cp_col + 2 + x] == 'w' or temp_board[cp_row + y][cp_col + 2 + x] == 'b' or \
                            temp_board[cp_row + y][
                                cp_col + 2 + x] == 'w':
                        temp_board[cp_row + 2 + x][cp_col + 2 + x] = 'X'

                    if temp_board[cp_row + 1 + x][cp_col + 1 + x] == 'X':
                        print("Invalid move: there's an obstruction in the way of movement.")

                        return False

    def check_rings(self, cp_row, cp_col, tp_row, tp_col):
        """
        Check if a player's move leaves themselves without a ring: players are not allowed to make a move that
        leaves themselves without a ring.
        """

        # Create a temporary board, mirroring the current board
        temp_board = []

        for i in self._board:
            temp_board.append(list(i))

        # Start each player at 0 rings
        black_rings = 0
        white_rings = 0

        # Make the move using the temp_board instead of the actual board
        GessGame.move_piece(self, cp_row, cp_col, tp_row, tp_col, temp_board)

        # If there exists a 3x3 grid on the game board that consists of 8 stones belonging to BLACK,
        # surrounding an empty center, then increase ring count by 1.
        if self._game_turn == 'BLACK':

            for x in range(2, 18):

                for y in range(2, 18):

                    if temp_board[x][y] == '-' and \
                            temp_board[x + 1][y - 1] == temp_board[x + 1][y] == temp_board[x + 1][y + 1] == \
                            temp_board[x][y - 1] == temp_board[x][y + 1] == \
                            temp_board[x - 1][y - 1] == temp_board[x - 1][y] == temp_board[x - 1][y + 1] == 'b':
                        black_rings += 1

        # If there exists a 3x3 grid on the game board that consists of 8 stones belonging to WHITE,
        # surrounding an empty center, then increase ring count by 1.
        if self._game_turn == 'WHITE':

            for x in range(2, 18):

                for y in range(2, 18):

                    if temp_board[x][y] == '-' and \
                            temp_board[x + 1][y - 1] == temp_board[x + 1][y] == temp_board[x + 1][y + 1] == \
                            temp_board[x][y - 1] == temp_board[x][y + 1] == \
                            temp_board[x - 1][y - 1] == temp_board[x - 1][y] == temp_board[x - 1][y + 1] == 'w':
                        white_rings += 1

        # If it's BLACK's turn and their move left themselves without a ring, return False
        if self._game_turn == 'BLACK' and black_rings == 0:

            print("Invalid move: players cannot make a move that leaves themselves without a ring.")

            return False

        # If it's WHITE's turn and their move left themselves without a ring, return False
        elif self._game_turn == 'WHITE' and white_rings == 0:

            print("Invalid move: players cannot make a move that leaves themselves without a ring.")

            return False

        else:

            return True

    def move_piece(self, cp_row, cp_col, tp_row, tp_col, board):
        """
        Move the 3x3 piece on the board.
        Remove any stones covered by piece's footprint.
        Remove any stones left outside of 18x18 board
        """

        cp_center = board[cp_row][cp_col]
        cp_north = board[cp_row - 1][cp_col]
        cp_south = board[cp_row + 1][cp_col]
        cp_east = board[cp_row][cp_col + 1]
        cp_west = board[cp_row][cp_col - 1]
        cp_north_east = board[cp_row - 1][cp_col + 1]
        cp_north_west = board[cp_row - 1][cp_col - 1]
        cp_south_east = board[cp_row + 1][cp_col + 1]
        cp_south_west = board[cp_row + 1][cp_col - 1]

        board[cp_row][cp_col] = '-'
        board[cp_row - 1][cp_col] = '-'
        board[cp_row + 1][cp_col] = '-'
        board[cp_row][cp_col + 1] = '-'
        board[cp_row][cp_col - 1] = '-'
        board[cp_row - 1][cp_col + 1] = '-'
        board[cp_row - 1][cp_col - 1] = '-'
        board[cp_row + 1][cp_col + 1] = '-'
        board[cp_row + 1][cp_col - 1] = '-'

        board[tp_row][tp_col] = cp_center
        board[tp_row - 1][tp_col] = cp_north
        board[tp_row + 1][tp_col] = cp_south
        board[tp_row][tp_col + 1] = cp_east
        board[tp_row][tp_col - 1] = cp_west
        board[tp_row - 1][tp_col + 1] = cp_north_east
        board[tp_row - 1][tp_col - 1] = cp_north_west
        board[tp_row + 1][tp_col + 1] = cp_south_east
        board[tp_row + 1][tp_col - 1] = cp_south_west

        # Remove any stones left outside of 18x18 board
        for x in range(0, 20):
            board[0][x] = '-'

            board[x][0] = '-'

            board[19][x] = '-'

            board[x][19] = '-'

    def check_winner(self):
        """
        Function called after all check functions.
        Checks, after making a move, if opposing player has any rings: if not, current players wins.
        """

        # Each player begins with 0 rings
        black_rings = 0
        white_rings = 0

        # If there exists a 3x3 grid on the game board that consists of 8 stones belonging to BLACK,
        # surrounding an empty center, then increase ring count by 1.
        for x in range(2, 18):

            for y in range(2, 18):

                if self._board[x][y] == '-' and \
                        self._board[x + 1][y - 1] == self._board[x + 1][y] == self._board[x + 1][y + 1] == \
                        self._board[x][y - 1] == self._board[x][y + 1] == \
                        self._board[x - 1][y - 1] == self._board[x - 1][y] == self._board[x - 1][y + 1] == 'b':
                    black_rings += 1

        # If there exists a 3x3 grid on the game board that consists of 8 stones belonging to WHITE,
        # surrounding an empty center, then increase ring count by 1.
        for x in range(2, 18):

            for y in range(2, 18):

                if self._board[x][y] == '-' and \
                        self._board[x + 1][y - 1] == self._board[x + 1][y] == self._board[x + 1][y + 1] == \
                        self._board[x][y - 1] == self._board[x][y + 1] == \
                        self._board[x - 1][y - 1] == self._board[x - 1][y] == self._board[x - 1][y + 1] == 'w':
                    white_rings += 1

        # If it's the end of BLACK's turn and WHITE has no rings, BLACK wins.
        if self._game_turn == 'BLACK' and white_rings == 0:

            print("Black wins!")

            self._game_state = 'BLACK_WON'

            return

        # If it's the end of WHITE's turn and BLACK has no rings, BLACK wins.
        elif self._game_turn == 'WHITE' and black_rings == 0:

            print("White wins!")

            self._game_state = 'WHITE_WON'

            return

        else:

            return True

    def make_move(self, current_position, target_position):
        """
        A 'piece' is selected by the center of its 3x3 grid. current_position and target_position define the 3x3 area
        being selected and being moved to, respectively. Row and column values are calculated from the user's input,
        these values create the centers of the current and target pieces.
        Next, check functions are called to check that the piece selected is a valid piece to move, if the movement
        amount is allowed, if the direction of movement is allowed, if there are any obstructions in the way of
        movement, and if moving the selected piece breaks the player's own rings, which is not allowed.
        Finally, if all of these functions do not return False, the piece gets moved on the board, any stones captured
        or left out of bounds are removed, and the check_winner function is called to check whether the move resulted
        in a player's winning the game. If no winners, then the player's turn is updated to the next player.
        """

        if self._game_state == 'UNFINISHED':

            # Get column and row values of the current position
            cp_col = int(GessGame.convert_column(self, current_position[0])) - 1
            cp_row = int(GessGame.convert_row(self, current_position[1:])) - 1

            # Get column and row values of the target position
            tp_col = int(GessGame.convert_column(self, target_position[0])) - 1
            tp_row = int(GessGame.convert_row(self, target_position[1:])) - 1

            if GessGame.check_current_piece(self, cp_row, cp_col) is False:
                return False

            if GessGame.check_move_amount(self, cp_row, cp_col, tp_row, tp_col) is False:
                return False

            if GessGame.check_move_direction(self, cp_row, cp_col, tp_row, tp_col) is False:
                return False

            if GessGame.check_obstructions(self, cp_row, cp_col, tp_row, tp_col) is False:
                return False

            if GessGame.check_rings(self, cp_row, cp_col, tp_row, tp_col) is False:
                return False

            GessGame.move_piece(self, cp_row, cp_col, tp_row, tp_col, self._board)

            GessGame.check_winner(self)

            # Next player's turn
            GessGame.next_player_turn(self)

            return True

        return True
