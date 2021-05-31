# This is a python program which solves the sudoku puzzle by using backtracking algorithm
# The example solved is one of the hardest sudoku puzzles on GOOGLE and takes about 2 seconds for this to solve

# Draw a random emty sudoku puzzle
board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0],
]

def print_my_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == len(board) - 1:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")

# Take the board and return the first empty position on sudoku puzzle
def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # return the row and column
                return (i, j)
    return None

# check if the number added is valid by checking row, then column and then each block
def is_valid(board, num, pos):
    # check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check the block
    box_x = pos[1] // 3
    box_y = pos[0] // 3

#  Each new block starts at position 0 and 3 and 6
    for i in range(box_y * 3, box_y*3 + 3): 
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

# the main backtracking algo
def solver(board):

    # the base case
    found = find_empty_square(board)
    if not found:
        return True
    else:
        row, column = found
        
# check for each number if its valid or not
        for i in range(1,10):
            if is_valid(board, i, (row, column)):
                board[row][column] = i
                
                if solver(board):
                    return True
            
                # set the value to be 0 if the board isnt solved and all values tried so now we go back
                board[row][column] = 0

    return False

# ------------PRINT THE SUDOKU PUZZZLE THEN SOLUTION---------------------
print("The Problem----->\n")
print_my_board(board)
print('\n\n')
solver(board)
print("Solved Board----->\n\n\n")
print_my_board(board)
