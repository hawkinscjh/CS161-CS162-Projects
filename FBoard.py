# Name: Casey Hawkins
# Date: 03/09/2020
# Description: A game called FBoard, where, on an 8x8 board, one player, Player X, has a goal to get their x piece from the top left corner (0,0) to the bottom right corner (7,7)
# without getting trapped by Player O's four o pieces. Each player takes turns, starting with Player X, who can only move their piece in diagonal directions. Player O goes next, and
# can only move one of their four o pieces at a time in a diagonal, but cannot move any of their pieces diagonally down and right (the direction Player X is moving).

class FBoard:
    """
    This class represents a game called FBoard.
    """

    def __init__(self):
        """
        This function initializes the 8x8 board, game state, and starting positions of both Player X and Player O's pieces on the board.
        """
        self._board = [['-' for x in range(8)] for y in range(8)]

        # Places initial four o pieces on the board.
        self._board[5][7] = 'o'
        self._board[6][6] = 'o'
        self._board[7][5] = 'o'
        self._board[7][7] = 'o'

        # Sets the beginning game state to unfinished.
        self._game_state = "UNFINISHED"

        # Places the initial x piece on the board.
        self._x_Row = 0
        self._x_Column = 0
        self._board[0][0] = 'x'

    def get_game_state(self):
        """
        Returns the current state of the game
        """
        return self._game_state

    def move_x(self, row, column):
        """
        Function moves Player X's piece in diagonal directions.
        """
        if self._game_state == "UNFINISHED":

            if 0 <= row < 8 and 0 <= column < 8:  # If the row and column are within the bounds of the board, then do this:

                # If the row and column are diagonal/valid moves, then do this:
                if (((self._x_Row - 1) == row and (self._x_Column - 1 == column)) or (
                        (self._x_Row + 1) == row and (self._x_Column - 1) == column) or
                        ((self._x_Row - 1) == row and (self._x_Column + 1) == column) or (
                                (self._x_Row + 1) == row and (self._x_Column + 1) == column)):

                    # If the desired position on the board is empty,  move x to that position.
                    if self._board[row][column] == '-':

                        self._board[row][column] = 'x'  # Input [row][column] now = 'x'
                        self._board[self._x_Row][self._x_Column] = '-'  # Replace where x moved from with '-'

                        self._x_Row = row
                        self._x_Column = column

                        # Checks if x reached [7][7] and won the game.
                        if self._x_Row == 7 and self._x_Column == 7:
                            self._game_state = "X_WON"

                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def move_o(self, fromRow, fromCol, toRow, toCol):
        """
        Function moves Player O's pieces in diagonal directions, but never in the down-right direction (increase in both row and column position)
        """
        if self._game_state == "UNFINISHED":

            # If fromRow, fromCol, toRow, toCol are within the bounds of the board, then do this:
            if 0 <= fromRow < 8 and 0 <= fromCol < 8 and 0 <= toRow < 8 and 0 <= toCol < 8:

                # If the position at [fromRow][fromCol] contains an 'o' piece, then do this:
                if self._board[fromRow][fromCol] == 'o':

                    # If the position at [toRow][toCol] is empty, then do this:
                    if self._board[toRow][toCol] == '-':

                        # Make sure that both toRow and toCol do not increase.
                        if (fromRow - 1 == toRow and fromCol - 1 == toCol) or (
                                fromRow - 1 == toRow and fromCol + 1 == toCol) or (
                                fromRow + 1 == toRow and fromCol - 1 == toCol):

                            self._board[fromRow][fromCol] = '-'
                            self._board[toRow][toCol] = 'o'

                            # Check if game is won by Player O
                            # Begin check at the first row:
                            if self._x_Row == 0:

                                if self._x_Column == 0:

                                    # If x is at 0,0 and o is at 1,1, then Player O wins.
                                    if self._board[self._x_Row + 1][self._x_Column + 1] == 'o':
                                        self._game_state = 'O_WON'

                                elif self._x_Column == 7:

                                    # If x is at 0,7 and o is at 1, 6, then Player O wins.
                                    if self._board[self._x_Row + 1][self._x_Column - 1] == 'o':
                                        self._game_state = 'O_WON'

                                else:

                                    # If x's moving down and left and down and right is blocked by an o, then Player O wins.
                                    if self._board[self._x_Row + 1][self._x_Column - 1] == 'o' and \
                                            self._board[self._x_Row + 1][self._x_Column + 1] == 'o':
                                        self._game_state = 'O_WON'
                            else:

                                if self._x_Column == 0:

                                    # If x's moving up and right and down and right is blocked by an o, then Player O wins.
                                    if self._board[self._x_Row - 1][self._x_Column + 1] == 'o' and \
                                            self._board[self._x_Row + 1][self._x_Column + 1] == 'o':
                                        self._game_state = 'O_WON'

                                elif self._x_Column == 7:

                                    # If x's moving up and left and down and left is blocked by an o, then Player O wins.
                                    if self._board[self._x_Row - 1][self._x_Column - 1] == 'o' and \
                                            self._board[self._x_Row + 1][self._x_Column - 1] == 'o':
                                        self._game_state = 'O_WON'

                                else:

                                    # If x is blocked on all sides by o pieces, then Player O wins.
                                    if (self._board[self._x_Row - 1][self._x_Column - 1] == 'o') and (
                                            self._board[self._x_Row - 1][self._x_Column + 1] == 'o') and (
                                            self._board[self._x_Row + 1][self._x_Column - 1] == 'o') and (
                                            self._board[self._x_Row + 1][self._x_Column + 1] == 'o'):
                                        self._game_state = 'O_WON'

                            return True
                        else:
                            return False
                    else:
                        return False

                else:
                    return False
            else:
                return False
        else:
            return False

    def print_Board(self):
        """
        Function prints the game board
        """
        for x in range(len(self._board)):
            print(self._board[x])
        print('')


game = FBoard()
game.print_Board()

turn = 0  # Start at zero turns

while game.get_game_state() == "UNFINISHED":  # While the game is UNFINISHED, do this:

    if turn % 2 == 0:  # If the turn is even, then it's Player X's turn

        print("Player X's turn.")

        row = input("Choose your row (0-7): ")

        column = input("Choose your column (0-7): ")

        token = game.move_x(int(row), int(column))  # Assign token 'x' to the [row][column]

        if token is False:  # If the [row][column] are not between 0 and 8 or if the spot is already occupied by a token, it's an invalid move.

            print("Invalid move. Try again.")

            turn -= 1  # Give Player X another try.

        game.print_Board()

        turn += 1

    else:

        print("Player O's turn. Choose the piece you want to move.")

        fromRow = input("Choose the piece's current row (0-7): ")

        fromCol = input("Choose the piece's current column (0-7): ")

        toRow = input("Choose the row to move your piece (0-7): ")

        toCol = input("Choose the column to move your piece (0-7): ")

        token = game.move_o(int(fromRow), int(fromCol), int(toRow), int(toCol))  # Assign token 'o' to the [row][column]

        if token is False:  # If the [row][column] are not between 0 and 8 or if the spot is already occupied by a token, it's an invalid move.

            print("Invalid move. Try again.")

            turn -= 1  # Give Player O another try.

        game.print_Board()

        turn += 1

if game.get_game_state() == "X_WON":  # If Player X wins, then:

    print("Player X Wins!")

else:  # If game does not end in Draw or Player X does not win, then:

    print("Player O Wins!")