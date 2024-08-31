import pygame
import random
import math

from pygame import mixer

pygame.font.init()
pygame.init()

screen_height = 650
screen_width= 1250




score_value = 0
font = pygame.font.Font('Stabillo Medium.ttf', 50)
textX = 1100
textY = 20

mixer.music.load('Kitbg.mp3')
mixer.music.play(-1)


game_over_font = pygame.font.Font('Stabillo Medium.ttf', 100)
Quote_font = pygame.font.Font('Airborne 86.ttf',25)

       

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))
def game_over_text():
    game_over_text = game_over_font.render("GAME  OVER!", True, (0, 0, 0))
    screen.blit(game_over_text,(450,200))
def Quote_text():
   game_over_text = game_over_font.render("STAY HOME STAY SAFE",25, (0, 0, 0))
   screen.blit(game_over_text,(300,300))
#Game window
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (1250, 650))



playerX = 150
playerY = 500
playerX_change = 0

enemy_img = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change =[]
num_of_enemies = 9

for i in range(num_of_enemies):
    enemy_img.append (pygame.image.load('virus.png'))
    enemyX_change.append(1)
    enemyY_change.append(8)
    enemyX.append(random.randint(0,500))
    enemyY.append(random.randint(0,250))

bullet_img = pygame.image.load('mask.png')
bulletX=0
bulletY= 500
bullet_change=0
bulletY_change = 5
bullet_state = "ready"

def fire_bullet(X,Y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(pygame.image.load('mask.png'),(X+30, Y-40))

def enemy(X,Y,i):
    screen.blit(enemy_img[i],(X,Y,))
#Draw player img in screen blit
def player(X,Y):
    screen.blit(pygame.image.load('target1.png'),(X,Y))

#Title and icon ofwindow
pygame.display.set_caption('SHOOTING GAME')
icon = pygame.image.load('target.png')
pygame.display.set_icon(icon)



def iscollision(enemyX,enemyY, bulletX, bulletY):
    a = math.pow(enemyX - bulletX, 2)
    b = math.pow(enemyY - bulletY, 2)
    distance = math.sqrt( a+b )

    if distance < 25:
        return True
    else:
        return False
#Game loop         
running = True
while running:
    #Background color(R,G,B)
    screen.fill((204,255,255))
    screen.blit(background,(0,0))
    #Track the event while game is running
    for event in pygame.event.get():
          
        
        if event.type == pygame.QUIT:
           running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change =0

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('Cartoon.wav')
                    bullet_sound.play()
                    bulletX =playerX
                    fire_bullet(bulletX,bulletY)

        

    playerX+= playerX_change
    if playerX <= 0:
        playerX =0
    elif playerX >= 1100:
         playerX = 1100
    

    if bulletY <= 0:
        bulletY = 500
        bullet_state ='ready'
        
    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletY  -= bulletY_change

    for i in range(num_of_enemies):
        enemy(enemyX[i],enemyY[i],i) 
        if enemyY[i]>=450:
            for j in range(num_of_enemies):
                gameover_sound=mixer.Sound('Meme.wav')
                gameover_sound.play()
                enemyY[i]= 2500
                pygame.mixer.music.stop()
                mixer.music.load('Meme.wav')
                mixer.music.play()
                game_over_text()
                Quote_text()
                break

        enemyX[i]+= enemyX_change[i]
        if enemyX[i]<= 0:
            enemyX_change[i] =15
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1100:
                enemyX_change[i] =-15
                enemyY[i] += enemyY_change[i]
                
        collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_Sound = mixer.Sound('Hey.wav')
            explosion_Sound.play()
            bulletY = 500
            bullet_state = "ready"
            score_value +=1
            print(score_value)
            enemyX[i] = random.randint(0,500)
            enemyY[i] = random.randint(0,250)
        
                       
    player(playerX,playerY)
    show_score(textX,textY)


    #Updating te screen
    pygame.display.update()              
    
# click on the 'X' button and the game is quit
pygame.quit()
                
