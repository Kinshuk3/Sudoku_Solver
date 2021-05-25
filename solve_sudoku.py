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

def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # return the row and column
                return (i, j)
    return None


def is_valid(board, num, pos):
    # check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check the column
    box_x = pos[1] // 3
    box_y = pos[0] // 3

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

        for i in range(1,10):
            if is_valid(board, i, (row, column)):
                board[row][column] = i

                if solver(board):
                    return True
            
                # rest the value
                board[row][column] = 0

    return False

print("The Problem----->\n")
print_my_board(board)
print('\n\n')
solver(board)
print("Solved Board----->\n\n\n")
print_my_board(board)