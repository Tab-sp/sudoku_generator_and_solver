import sudoku_solver as ss
import random

board_zero = [
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

def generate(clue_count):
    board = ss.solve_sudoku_random(board_zero)
    count = 0
    while True:
        col = random.randint(0,8)
        row = random.randint(0,8)
        if board[row][col] != 0:
            board[row][col] = 0
            count+=1
            if count > 9*9 - clue_count:
                break
    for row in board:
        print(row, end = "\n")
    return board

