def is_valid(board, row, col, num):
    """Checks if placing a number in a cell is valid.

    Args:
        board: The 9x9 Sudoku board.
        row: The row index of the cell.
        col: The column index of the cell.
        num: The number to be placed.

    Returns:
        True if the placement is valid, False otherwise.
    """

    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def   
 solve_sudoku(board):
    """Solves   
 a Sudoku puzzle using backtracking.

    Args:
        board: The 9x9 Sudoku board.

    Returns:
        True if the puzzle is solved, False otherwise.
    """

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col]   
 = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0   

                return False
    return True

def print_board(board):
    """Prints the Sudoku board in a formatted way.

    Args:
        board: The 9x9 Sudoku board.
    """

    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

if __name__ == '__main__':
    # Example Sudoku puzzle
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists.")  
