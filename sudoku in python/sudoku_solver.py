import random

class Solution:
    def __init__(self, board):
        self.board = board

    def solve(self):
        row, col = self.find_unassigned()
        if (row, col) == (-1, -1):
            return True
        for num in range(1,10):
            if self.safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def random_solve(self):
        row, col = self.find_unassigned()

        random_lst = [x for x in range(1,10)]
        random.shuffle(random_lst)

        if (row, col) == (-1, -1):
            return True
        for num in random_lst:
            if self.safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
                random.shuffle(random_lst)
        return False

    def find_unassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return -1, -1

    def safe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row,ch) and self.checkcol(col,ch
        ) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True
    
    def print_board(self):
        for row in self.board:
            print(row, end = "\n")

def solve_sudoku(board):
    solution = Solution(board)
    solution.solve()
    solution.print_board()
    return(solution.board)

def solve_sudoku_random(board):
    solution = Solution(board)
    solution.random_solve()
    return(solution.board)