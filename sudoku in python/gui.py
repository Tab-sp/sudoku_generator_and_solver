import pygame
import map_generator as mg
import sudoku_solver as ss

pygame.init()
pygame.display.set_caption('Sudoku Map & Solution Generator')

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (122, 122, 122)
RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 360
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
FONT = pygame.font.Font('freesansbold.ttf', 20)

clock = pygame.time.Clock()

def print_text(word, x, y, color = BLACK):
    TEXT = FONT.render(word, True, color)
    text_rect = TEXT.get_rect()
    text_rect.center = (x, y)
    return SCREEN.blit(TEXT, text_rect)

def generate_board(x = 0, y = 0):
    board = mg.generate(60)
    draw_board(board, x, y)
    ss.solve_sudoku(board)
    draw_board(board, x+300, y)

def draw_board(board, x = 0, y = 0):
    block_size = 20
    row_index = y
    col_index = x
    for row in board:
        col_index = x
        row_index += block_size
        for item in row:
            col_index += block_size
            rect = pygame.Rect(col_index - 11, row_index - 11, 20, 20)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            if item != 0:
                print_text(str(item), col_index, row_index)

SCREEN.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SCREEN.fill(WHITE)
                generate_board(20, 20)
                clock.tick(20)
    clock.tick(100)
    pygame.display.update()