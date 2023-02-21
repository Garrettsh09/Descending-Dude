import pygame, sys
import random

#To Do list:
#Randomize beam spawns
#Colllsion detection
#Menu screen
#End screen
#Ui
#Music
#Sound effects, collision and score increase
#Save score and high score
#Leaderboard
#Universal leaderboard

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Game Name Here')

WINDOW_SIZE = (1000,1000)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)


player_image = pygame.image.load('/Users/garrettsharpe/Documents/Code/Python/Projects/FirstPythonGame/Art/WorkerSprite3.png')
beam_image = pygame.image.load('/Users/garrettsharpe/Documents/Code/Python/Projects/FirstPythonGame/Art/BeamSprite.png')

moving_right = False
moving_left = False
moving_up = False
moving_down = False

player_location = [500,0]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(),player_image.get_height())

beam1_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam1_rect = pygame.Rect(beam1_location[0], beam1_location[1], beam_image.get_width(), beam_image.get_height())
beam2_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam2_rect = pygame.Rect(beam2_location[0], beam2_location[1], beam_image.get_width(), beam_image.get_height())
beam3_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam3_rect = pygame.Rect(beam3_location[0], beam3_location[1], beam_image.get_width(), beam_image.get_height())
beam4_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam4_rect = pygame.Rect(beam4_location[0], beam4_location[1], beam_image.get_width(), beam_image.get_height())
beam5_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam5_rect = pygame.Rect(beam5_location[0], beam5_location[1], beam_image.get_width(), beam_image.get_height())

def collision():
    #play sound effect
    #game over menu
    return pygame.quit()
    #temporary



while True:
    screen.fill((146,244,255))
    score = 0

    screen.blit(player_image, player_location)
    screen.blit(beam_image, beam1_location)
    screen.blit(beam_image, beam2_location)
    screen.blit(beam_image, beam3_location)
    screen.blit(beam_image, beam4_location)
    screen.blit(beam_image, beam5_location)

    if player_location[1] == 300:
        beam1_location[1] -= 10
        beam2_location[1] -= 10
        beam3_location[1] -= 10
        beam4_location[1] -= 10
        beam5_location[1] -= 10


    #make x value random by if randint > x: value = randint - x or if randint < x value = x - randint
    if player_location[1] < 300:
        player_location[1] += 5

    if beam1_location[1] < 1:
        score += 1
        beam1_location[1] += 1000
    if beam2_location[1] < 1:
        score += 1
        beam2_location[1] += 1000
    if beam3_location[1] < 1:
        score += 1
        beam3_location[1] += 1000
    if beam4_location[1] < 1:
        score += 1
        beam4_location[1] += 1000
    if beam5_location[1] < 1:
        score += 1
        beam5_location[1] += 1000

    if player_location == beam1_location or player_image == beam2_location or player_image == beam3_location\
    or player_location == beam4_location or player_location == beam5_location:
        collision()
        #make in range of 50ish pixels

    if moving_right == True:
        player_location[0] += 10
    if moving_left == True:
        player_location[0] -= 10

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LALT and K_F4:
                pygame.quit()
            if event.key == K_d:
                moving_right = True 
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_a:
                moving_left = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_a:
                moving_left = False
            if event.key == K_LEFT:
                moving_left = False 

    

    pygame.display.update()
    clock.tick(60)

    best_score = 0
    if score > best_score:
        best_score = score