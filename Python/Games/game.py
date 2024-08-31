import pygame
import random

from pygame import mixer

pygame.font.init()
mixer.init()

s_height = 620
s_width = 580
play_width = 300
play_height = 600

block_size = 30

top_left_x =(s_width - play_width) //2
top_left_y = s_height -play_height

score = 0

I=[['..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
   ['.....',
    '0000.',
    '.....',
    '.....',
    '.....']]

O=[['.....',
    '.....',
    '.00..',
    '.00..',
    '.....']]

J=[['.....',
    '.0...',
    '.000.',
    '.....'],
   ['.....',
    '..00.',
    '..0..',
    '..0..',
    '.....'],
   ['.....',
    '.....',
    '.000.',
    '...0.',
    '.....'],
   ['.....',
    '..0..',
    '..0..',
    '.00..']]

S=[['.....',
    '.....',
    '..00.',
    '.00..',
    '.....'],
   ['.....',
    '..0..',
    '..00.',
    '...0.',
    '.....']]

Z=[['.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
   ['.....',
    '..0..',
    '.00..',
    '.0...',
    '.....']]

L=[['.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
   ['.....',
    '..0.',
    '..0..',
    '..00.',
    '.....'],
   ['.....',
    '.....',
    '.000.',
    '.0...',
    '.....'],
   ['.....',
    '.00..',
    '..0..',
    '..0..',
    '.....']]

T=[['.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
   ['.....',
    '..0.',
    '..00.',
    '..0..',
    '.....'],
   ['.....',
    '.....',
    '.000.',
    '..0..',
    '.....'],
   ['.....',
    '..0..',
    '.00..',
    '..0..',
    '.....']]



shapes = [S, Z, I, O, J, L, T]
shape_colors =[(0,255,0), (255, 0, 0), (0,255,255),(255,255,0),(255,165,0),(0,0,255),(128,0,128)]


Tetris= pygame.mixer.music.load('Tetris.mp3')
pygame.mixer.music.play(-1)

class Piece:
    x=20
    y=10
    shape=0
    color=()
    rotation=0
    def __init__(self, column, row, shape):
        self.x=column
        self.y=row
        self.shape=shape
        self.color=shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_positions ={}):
    grid =[[(0,0,0)for x in range (10)] for x in range (20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j ,i) in locked_positions:
                c= locked_positions[(j ,i)]
                grid[i][j] = c

    return grid



def draw_window(surface,grid, ):
    surface.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris',1,(255,255,255))

    surface.blit(label,(top_left_x + play_width/2 -(label.get_width()/2),top_left_y + play_height/2 - label.get_height()/2))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface,grid[i][j],(top_left_x + j*30, top_left_y + i*30,block_size,block_size),0)

    draw_grid(surface,grid)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width,play_height), 5)

    #pygame.display.update()
    

def update_score(surface):
       text = "score:" +str(score)

       font = pygame.font.SysFont('comicsans',40)
       label = font.render(text,1,(255,255,255))

       sx = top_left_x+play_width+10
       sy = top_left_y + play_height/2-100

       surface.blit(label,(sx+10,sy+150)) 
     
def draw_grid(surface ,grid):
    sx = top_left_x
    sy = top_left_y
    
    
    for i in range (len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy+ i*30), (sx + play_width, sy+ i*30))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx +j*30, sy), (sx +j*30, sy+play_height))
           

def get_shape():
    return Piece(5,0, random.choice(shapes))

def convert_shape_format(shape):

    
    positions =[]
    format = shape.shape[shape.rotation%len(shape.shape)]

   
    for i, line in enumerate(format):
           row = list(line)

           for j, column in enumerate(row):
               if column=='0':
                   positions.append((shape.x + j, shape.y + i))
                   
   
    for i, pos in enumerate(positions):
        positions[i] = (pos[0]-2,pos[1]-4)
       

    return positions

def valid_space(shape,grid):
    accepted_pos = [[(j, i) for j in range (10) if grid[i][j] == (0,0,0)] for i in range(20)]
    #narrow down the martix for easier handling
    accepted_pos = [ j for sub in accepted_pos for j in sub ]
    #convert_shape_format returns a list of string 
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y<1:
            return True

    return False

def draw_next_shape(shape, surface):
    #font and render it,print it
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))
    # Where to display the piece? These are the coordinates
    sx = top_left_x + play_width + 10
    sy = top_left_y + play_height/2 - 100
    #List of strings depicting the orientation of piece
    format = shape.shape[shape.rotation % len(shape.shape)]

    for  i, line in enumerate(format):
        row = list(line)
        
        for j,column in enumerate(row):
            if column == '0':
                #Draw the next_piece
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30,30, 30), 0)
                
                
    
    surface.blit(label, (sx + 10, sy - 30))
    update_score(surface)


def clear_rows(grid, locked):
    global score
    inc = 0

    for i in range(len(grid)-1,-1 , -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc +=1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[ (j,i)]
                except:
                    continue
    if inc>0:
        temp = sorted(list(locked),key=lambda x:x[1])
        for key in temp[::-1]:
            x,y = key
            if y < ind:
                newkey =(x,y + inc)
                locked[newkey]= locked.pop(key)
    score+= 10
    

def update_score(surface):
    text = "score:" +str(score)

    font = pygame.font.SysFont('comicsans',40)
    label = font.render(text,1,(255,255,255))

    sx = top_left_x+play_width+2
    sy = top_left_y + play_height/2-100

    surface.blit(label,(sx+10,sy+150))   

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans',size ,bold=True)
    
    # Render the font on the text
    label=font.render(text, 1, color)
    
    # print the text using label
    surface.blit(label,(top_left_x + play_width/2-(label.get_width()/2),top_left_y + play_height/2-label.get_height()/2))

   
    
def play(win):
    locked_positions= {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.20
    
   

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        
        clock.tick()

        

        if fall_time/1000 >fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y >0:
                current_piece.y -= 1
                change_piece = True


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -=1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y += 1
                    
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y += 1

                if event.key == pygame.K_DOWN:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation +=1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color

            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)

            
            
        
        draw_window(win,grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()
                                    
        if check_lost(locked_positions):
            pygame.mixer.music.stop()
            mixer.music.load('tetrisover.wav')
            mixer.music.play()
            draw_text_middle(win, "YOU LOST!",80,(255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            gameover_sound=mixer.Sound('tetrisover.wav')
            gameover_sound.play()
        

    

    
    
def game(win):
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win,"Press Any Key To Play", 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                play(win)

    pygame.display.quit()
    
    
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")
game(win)


                    
                    


                
