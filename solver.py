'''
A program that solves a Sudoku using a backtracking algorithm.
Written by Oscar Strachan.
Started 29/04/2022.
'''
from random import shuffle, randint

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def solve_board(board):
    '''
    Backtracking algorithm that solves the Sudoku.

    Inputs:
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
    Output:
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


def generate_solution(board):
    '''
    A backtracking algorithm that generates a complete solution to the Sudoku.

    Input:
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
    Output:
        boolean - true if solved, false if not.
    '''

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    locate = locate_empty(board)
    if not locate:
        return True
    else:
        row, col = locate

    shuffle(number_list)
    for number in number_list:
        if check_valid(board, number, (row, col)):
            board[row][col] = number

            if solve_board(board):
                return True

            board[row][col] = 0

    return False


def remove_numbers(board, difficulty):
    '''
    Removes a certain number of cells from the Sudoku depending on difficulty.

    Inputs:
        board - a list of lists containing digits correlating to integers or empty spaces on the board.
        difficulty - the desired Sudoku difficulty    
    '''
    
    non_empty_cells = 81
    removed_cells = []
    number = 0

    if difficulty == 'Easy':
        number = 17 * 3
    elif difficulty == 'Medium':
        number = 17 * 2
    elif difficulty == 'Hard':
        number = 17 * 1

    while non_empty_cells > number:
        row = randint(0, 8)
        column = randint(0, 8)
        if (row, column) not in removed_cells:
            board[row][column] = 0
            removed_cells.append((row, column))

            non_empty_cells -= 1

    return


