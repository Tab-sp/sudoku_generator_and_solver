import map_generator as mg
import sudoku_solver as ss

board = mg.generate(60)

print("\n")

ss.solve_sudoku(board)