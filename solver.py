'''
A program that solves a Sudoku using a backtracking algorithm.
Written by Oscar Strachan.
Started 29/04/2022.
'''

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve_board(board):
    '''
    Backtracking algorithm that solves the Sudoku.

    Inputs:
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
    Outputs:
        boolean - true if solved, false if not.
    '''

    locate = locate_empty(board)
    if not locate:
        return True
    else:
        row, col = locate

    for i in range(1, 10):
        if check_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False


def check_valid(board, number, position):
    '''
    Verifiers whether the number placed is a valid move.

    Input:
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
        number - the number placed.
        position (tuple) - the position in which the number was placed.
    Output:
        boolean - true if placement is valid and false if it is not.    
    '''

    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and position != (i, j):
                return False

    return True
    


def display_board(board):
    '''
    Prints the board as standard output to the terminal. 

    Input: 
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
    Output:
        none.
    '''

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end="")


def locate_empty(board):
    '''
    Finds an empty space on the board.

    Input:
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
    Output:
        (i, j) or None - the position of the empty space on the board.    
    '''

    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:
                return (i, j)

    return None

