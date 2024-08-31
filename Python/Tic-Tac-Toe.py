import pygame,sys
import numpy as np

pygame.init()

#constant
WIDTH= 600
HEIGHT=WIDTH
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLS=3

#rgb color
RED = (255,0,0)
BG_COLOR= (28, 170,156)
LINE_COLOR= (23,145,135)

screen= pygame.display.set_mode( (WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)

#pygame.draw.line(screen, RED, (10,10),(300,300), 10 )

def draw_lines():
    # 1 Horizontal line
    pygame.draw.line(screen, LINE_COLOR,(0,200),(600,200), LINE_WIDTH)
    # 2 horizontal line
    pygame.draw.line(screen, LINE_COLOR,(0,400),(600,400), LINE_WIDTH)
    #1 vertical line
    pygame.draw.line(screen, LINE_COLOR,(200,0),(200,600), LINE_WIDTH)
    #2 vertical line
    pygame.draw.line(screen, LINE_COLOR,(400,0),(400,600), LINE_WIDTH)

draw_lines()
    

#mainloop
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()

    pygame.display.update()
            
    
