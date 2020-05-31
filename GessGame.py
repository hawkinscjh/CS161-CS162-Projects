# Name: Casey Hawkins
# Date: 05/27/2020
# Description: Gess, an abstract board game pitting two players, Player X and Player O, against each other in a
# combination of Go and Chess. Players' start on an 18x18 board, each with 43 stones. Players take turns moving
# a 3x3 'piece', utilizing rules listed in the make_move function, in an attempt to remove all ring pieces from their
# opponent. Rules for ring pieces are in the ring_check function. First player to lose all ring pieces loses


class GessGame:
    """
    Class for Gess, an abstract board game pitting two players, Player X and Player O, against each other in a
    combination of Go and Chess. Players' start on an 18x18 board, each with 43 stones. Players take turns moving
    a 3x3 'piece', utilizing rules listed in the make_move function, in an attempt to remove all ring pieces from their
    opponent. Rules for ring pieces are in the ring_check function. First player to lose all ring pieces loses.
    """

    def __init__(self):
        """
        Game initializes in UNFINISHED state, begins on Player X's turn, and creates labelled 20x20 game board with all
        43 of each player's pieces in place
        """

        # Game starts in UNFINISHED state
        self._game_state = 'UNFINISHED'

        # BLACK takes the first turn.
        self._game_turn = 'BLACK'

        # Create a 20x20 board
        self._board = [['-' for x in range(21)] for y in range(20)]

        # Add a row to label each column with a letter
        self._board.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T'])

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

        # Place all 43 of Player O's pieces
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

        # Place all 43 of Player X's pieces
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
        Returns current state of the game. Can be UNFINISHED, X_WON, or O_WON.
        """

        return self._game_state

    def get_player_turn(self):
        """
        Get method for player's turn
        """

        return self._game_turn


    def update_player_turn(self):
        """
        Changes the turn to the next player
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
        Converts a column from a letter to its corresponding number. Utilized in make_move function.
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
        Converts a row's labelled row position to its actual position on the board. Utilized in make_move function.
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


    def move_amount(self, center):
        """
        If center stone is present, piece can move until it encounters another piece or goes over 18x18 board bounds.
        If center stone is not present, piece can move up to 3 spaces, unless it encounters another piece or goes over
        18x18 board bounds.
        """

        if self._game_turn == 'BLACK':

            if center == 'b':

                return 20

            else:

                return 3

        if self._game_turn == 'WHITE':

            if center == 'w':

                return 20

            else:

                return 3

    def current_piece(self, cp_row, cp_col):
        """
        Make the 3x3 piece that is going to be moved. Check if 3x3 is legal.
        Start piece cannot include any enemy pieces in its 3x3 grid.
        """

        center = self._board[cp_row][cp_col]

        print("Center:", center)

        if self._game_turn == 'BLACK':

            if center == 'w':

                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if center == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        north = self._board[cp_row - 1][cp_col]

        print("North:", north)

        if self._game_turn == 'BLACK':

            if north == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if north == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        south = self._board[cp_row + 1][cp_col]

        print("South:", south)

        if self._game_turn == 'BLACK':

            if south == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if south == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        east = self._board[cp_row][cp_col + 1]

        print("East:", east)

        if self._game_turn == 'BLACK':

            if east == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if east == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        west = self._board[cp_row][cp_col - 1]

        print("West:", west)

        if self._game_turn == 'BLACK':

            if west == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if west == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        north_east = self._board[cp_row - 1][cp_col + 1]

        print("North_east:", north_east)

        if self._game_turn == 'BLACK':

            if north_east == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if north_east == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        north_west = self._board[cp_row - 1][cp_col - 1]

        print("North_west:", north_west)

        if self._game_turn == 'BLACK':

            if north_west == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if north_west == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        south_east = self._board[cp_row + 1][cp_col + 1]

        print("South_east:", south_east)

        if self._game_turn == 'BLACK':

            if south_east == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if south_east == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        south_west = self._board[cp_row + 1][cp_col - 1]

        print("South_west:", south_west)

        if self._game_turn == 'BLACK':

            if south_west == 'w':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if self._game_turn == 'WHITE':

            if south_west == 'b':
                print("Invalid move: 3x3 piece cannot include opponent's stones.")

                return False

        if center == north == south == east == west == north_east == north_west == south_east == south_west == '-':

            print("Invalid move: 3x3 piece must contain at least one of your stones.")

            return False

        if center == ('b' or 'w') and north == south == east == west == north_east == north_west == south_east == south_west == '-':

            print("Invalid move: 3x3 piece cannot only contain one stone located in the center.")

            return False

        for x in range(0, 20):

            if center == self._board[0][x] or center == self._board[20][x]:

                print("Invalid move: center cannot be out of bounds.")

                return False

    def target_piece(self, tp_row, tp_col):
        """
        Checks the 3x3 area where start_piece is being moved to.
        Check if center square is being moved off of 18x18 grid, which is not allowed.
        Player cannot make a move that leaves themselves without a ring.
        """

        print(tp_row, tp_col)

        center = self._board[tp_row][tp_col]

        for x in range(0, 20):

            if center == self._board[0][x] or center == self._board[20][x]:

                print("Invalid move: center cannot move out of bounds.")

                return False

        north = self._board[tp_row - 1][tp_col]

        south = self._board[tp_row + 1][tp_col]

        east = self._board[tp_row][tp_col + 1]

        west = self._board[tp_row][tp_col - 1]

        north_east = self._board[tp_row - 1][tp_col + 1]

        north_west = self._board[tp_row - 1][tp_col - 1]

        south_east = self._board[tp_row + 1][tp_col + 1]

        south_west = self._board[tp_row + 1][tp_col - 1]


    def ring_check(self):
        """
        Function checks if current player has any rings on their board. If none are found, player loses.
        """

        # Need to scan board and check that there are any rings.
        # Could be helpful to print out how many rings are found.
        # As soon as no rings are detected, player with no rings loses.

        pass


    def make_move(self, current_position, target_position):
        """
        A 'piece' is selected by the center of its 3x3 grid. current_position and target_position are passed off to
        their respective functions to create their 3x3 pieces and checked if they are legal.
        Next, function checks if the piece's move is legal. Pieces cannot move in directions without a stone located in
        that direction in the perimeter of the 3x3 piece. Pieces without stones in their center cannot move more than
        3 spaces in a direction. Pieces with or without stones in their center cannot move once they have encountered
        another stone in their area of movement.
        Function removes stones that are overlapped by the piece and removes stones that are left outside of the 18x18
        board.
        Function then calls ring_check to check that either side still has at least one ring structure, updating the
        game_state if necessary.
        Finally, if all moves and pieces made are valid, function calls update_player_turn()
        """

        if self._game_state == 'UNFINISHED':

            # Get column and row values of the current position
            cp_col = int(GessGame.convert_column(self, current_position[0])) - 1
            cp_row = int(GessGame.convert_row(self, current_position[1:])) - 1

            # Get column and row values of the target position
            tp_col = int(GessGame.convert_column(self, target_position[0])) - 1
            tp_row = int(GessGame.convert_row(self, target_position[1:])) - 1

            print("Current position's row:", cp_row)
            print("Current position's column:", cp_col)

            print("Target position's row:", tp_row)
            print("Target position's column:", tp_col)

            if cp_row == tp_row and cp_col == tp_col:
                print("Invalid move: center must move.")
                print("Try again")
                return

            if game.current_piece(cp_row, cp_col) is False:
                print("Try again.")
                return

            if game.target_piece(tp_row, tp_col) is False:
                print("Try again.")
                return

            game.update_player_turn()



game = GessGame()
game.print_Board()
print(game.get_player_turn())
game.make_move('c2', 'c3')
game.print_Board()
print(game.get_player_turn())
game.make_move('s18', 't18')


