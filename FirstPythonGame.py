import pygame, sys
import random

#To Do list:
#Colllsion detection
#Add more beams
#Menu screen
#End screen
#Ui
#Music
#Sound effects, collision and score increase
#Scaling difficulty
#Save score and high score
#Leaderboard
#Universal leaderboard
#Changeable skins

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('0')

WINDOW_SIZE = (1400,1000)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)


player_image = pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/WorkerSprite3.png')
beam_image = pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/BeamSprite.png')

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
beam6_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam6_rect = pygame.Rect(beam6_location[0], beam6_location[1], beam_image.get_width(), beam_image.get_height())
beam7_location = [(random.randint(0,1000)), (random.randint(400,1000))]
beam7_rect = pygame.Rect(beam7_location[0], beam7_location[1], beam_image.get_width(), beam_image.get_height())

def collision():
    if player_location[0] in range((beam1_location[0])- 75, (beam1_location[0])+75) and player_location[1] in range((beam1_location[1])-5, (beam1_location[1]) + 5):
        pygame.quit()
    if player_location[0] in range((beam2_location[0])- 75, (beam2_location[0])+75) and player_location[1] in range((beam2_location[1])-5, (beam2_location[1]) + 5):
        pygame.quit()
    if player_location[0] in range((beam3_location[0])- 75, (beam3_location[0])+75) and player_location[1] in range((beam3_location[1])-5, (beam3_location[1]) + 5):
        pygame.quit()
    if player_location[0] in range((beam4_location[0])- 75, (beam4_location[0])+75) and player_location[1] in range((beam4_location[1])-5, (beam4_location[1]) + 5):
        pygame.quit()
    if player_location[0] in range((beam5_location[0])- 75, (beam5_location[0])+75) and player_location[1] in range((beam5_location[1])-5, (beam5_location[1]) + 5):
        pygame.quit()
    if player_location[0] in range((beam6_location[0])- 75, (beam6_location[0])+75) and player_location[1] in range((beam6_location[1])-5, (beam6_location[1]) + 5):
        pygame.quit()
    if player_location[0] in range((beam7_location[0])- 75, (beam7_location[0])+75) and player_location[1] in range((beam7_location[1])-5, (beam7_location[1]) + 5):
        pygame.quit()

def score_(score, level):
    if score == 7:
        level += 1
        score = 0


score = 0
level = 0


while True:
    screen.fill((146,244,255))

    screen.blit(player_image, player_location)
    screen.blit(beam_image, beam1_location)
    screen.blit(beam_image, beam2_location)
    screen.blit(beam_image, beam3_location)
    screen.blit(beam_image, beam4_location)
    screen.blit(beam_image, beam5_location)
    screen.blit(beam_image, beam6_location)
    screen.blit(beam_image, beam7_location)

    if player_location[1] == 300:
        if level <= 20:
            beam1_location[1] -= 10
            beam2_location[1] -= 10
            beam3_location[1] -= 10
            beam4_location[1] -= 10
            beam5_location[1] -= 10
            beam6_location[1] -= 10
            beam7_location[1] -= 10
        elif 20 < level <= 50:
            beam1_location[1] -= 15
            beam2_location[1] -= 15
            beam3_location[1] -= 15
            beam4_location[1] -= 15
            beam5_location[1] -= 15
            beam6_location[1] -= 15
            beam7_location[1] -= 15
        elif 50 < level <= 100:
            beam1_location[1] -= 20
            beam2_location[1] -= 20
            beam3_location[1] -= 20
            beam4_location[1] -= 20
            beam5_location[1] -= 20
            beam6_location[1] -= 20
            beam7_location[1] -= 20
        elif 100 < level <= 200:
            beam1_location[1] -= 30
            beam2_location[1] -= 30
            beam3_location[1] -= 30
            beam4_location[1] -= 30
            beam5_location[1] -= 30
            beam6_location[1] -= 30
            beam7_location[1] -= 30
        else:
            beam1_location[1] -= 100
            beam2_location[1] -= 100
            beam3_location[1] -= 100
            beam4_location[1] -= 100
            beam5_location[1] -= 100
            beam6_location[1] -= 100
            beam7_location[1] -= 100


    #make x value random by if randint > x: value = randint - x or if randint < x value = x - randint
    if player_location[1] < 300:
        player_location[1] += 5

    if beam1_location[1] < 1:
        score += 1
        beam1_location[1] += 1000
        x = random.randint(0,1000)
        if beam1_location[0] > x:
            beam1_location[0] -= x
        else:
            beam1_location[0] += x
    if beam2_location[1] < 1:
        score += 1
        beam2_location[1] += 1000
        x = random.randint(0,1000)
        if beam2_location[0] > x:
            beam2_location[0] -= x
        else:
            beam2_location[0] += x
    if beam3_location[1] < 1:
        score += 1
        beam3_location[1] += 1000
        x = random.randint(0,1000)
        if beam3_location[0] > x:
            beam3_location[0] -= x
        else:
            beam3_location[0] += x
    if beam4_location[1] < 1:
        score += 1
        beam4_location[1] += 1000
        x = random.randint(0,1000)
        if beam4_location[0] > x:
            beam4_location[0] -= x
        else:
            beam4_location[0] += x
    if beam5_location[1] < 1:
        score += 1
        beam5_location[1] += 1000
        x = random.randint(0,1000)
        if beam5_location[0] > x:
            beam5_location[0] -= x
        else:
            beam5_location[0] += x
    if beam6_location[1] < 1:
        score += 1
        beam6_location[1] += 1000
        x = random.randint(0,1000)
        if beam6_location[0] > x:
            beam6_location[0] -= x
        else:
            beam6_location[0] += x
    if beam7_location[1] < 1:
        score += 1
        beam7_location[1] += 1000
        x = random.randint(0,1000)
        if beam7_location[0] > x:
            beam7_location[0] -= x
        else:
            beam7_location[0] += x

    collision()

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

    if score == 7:
        level += 1
        score = 0
    
    pygame.display.set_caption(str(level))
