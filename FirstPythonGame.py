import pygame, sys
from pygame.locals import *
import pygame_menu
from pygame import mixer
import random

#To Do list:
#Out of bands glitch
#Music
#Save score and high score
#Leaderboard
#Universal leaderboard
#Changeable skins

clock = pygame.time.Clock()

pygame.init()
mixer.init()

pygame.display.set_caption('Descending Dude')

WINDOW_SIZE = (1400,1000)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

mixer.music.set_volume(0.2)

def quit_game():
    pygame.quit()
    sys.exit()

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size):
    return pygame.font.Font('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/font.ttf', size)

BG = pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Backgroundimage.png')
BG_location = [0,0]

DeathScreenBG = pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/DeathScreenBG.png')
DeathScreenBG_location = [0,0]

leaderboard = {'User1': 1, 'User2': 2, 'User3' : 3, 'User4' :4, 'User5': 5, 'User6': 6, 'User7': 7, 'User8': 8, 'User9': 9, 'User10': 10 }
user_name = ''

def menu():
    while True:
        screen.blit(BG, BG_location)
        MENU_TEXT = get_font(80).render("Descending Dude", True, "#ff6600")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))

        PLAYBUTTON_TEXT = get_font(90).render('PLAY', True, '#ff6600')
        PLAYBUTTON_RECT = PLAYBUTTON_TEXT.get_rect(center=(640,275))
        PLAYBUTTON = Button(image=pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Play_Rect.png'), pos=(640, 275), 
            text_input="PLAY", font=get_font(75), base_color="#ff6600", hovering_color="White")

        LEADERBOARD_TEXT = get_font(90).render('LEADERBOARD', True, '#ff6600')
        LEADERBOARD_RECT = LEADERBOARD_TEXT.get_rect(center=(640,450))
        LEADERBOARDBUTTON = Button(image=pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Play_Rect.png'), pos=(640, 450), 
            text_input="LEADERBOARD", font=get_font(75), base_color="#ff6600", hovering_color="White")
        
        SKINS_TEXT = get_font(90).render('SKINS', True, '#ff6600')
        SKINSTEXT_RECT = SKINS_TEXT.get_rect(center=(640,650))
        SKINSTEXTBUTTON = Button(image=pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Play_Rect.png'), pos=(640, 650), 
            text_input="LEADERBOARD", font=get_font(75), base_color="#ff6600", hovering_color="White")
    
        MENUQUIT_TEXT = get_font(90).render('QUIT', True, '#ff6600')
        MENUQUIT_RECT = MENUQUIT_TEXT.get_rect(center=(640,850))
        MENUQUITBUTTON = Button(image=pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Play_Rect.png'), pos=(640, 850), 
            text_input="QUIT", font=get_font(75), base_color="#ff6600", hovering_color="White")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(PLAYBUTTON_TEXT, PLAYBUTTON_RECT)
        screen.blit(LEADERBOARD_TEXT, LEADERBOARD_RECT)
        screen.blit(SKINS_TEXT, SKINSTEXT_RECT)
        screen.blit(MENUQUIT_TEXT,MENUQUIT_RECT)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if PLAYBUTTON.checkForInput(pygame.mouse.get_pos()):
                    run_game()
                if LEADERBOARDBUTTON.checkForInput(pygame.mouse.get_pos()):
                    leaderboard_screen()
                if MENUQUITBUTTON.checkForInput(pygame.mouse.get_pos()):
                    #Sad sound?
                    quit_game()
            if event.type == QUIT:
                quit_game()
            if event.type == KEYUP:
                if event.key == K_LALT and K_F4:
                    quit_game()

        pygame.display.update()


            
player_image = pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/WorkerSprite3.png')
beam_image = pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/BeamSprite.png')

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
        return True
    if player_location[0] in range((beam2_location[0])- 75, (beam2_location[0])+75) and player_location[1] in range((beam2_location[1])-5, (beam2_location[1]) + 5):
        return True
    if player_location[0] in range((beam3_location[0])- 75, (beam3_location[0])+75) and player_location[1] in range((beam3_location[1])-5, (beam3_location[1]) + 5):
        return True
    if player_location[0] in range((beam4_location[0])- 75, (beam4_location[0])+75) and player_location[1] in range((beam4_location[1])-5, (beam4_location[1]) + 5):
        return True
    if player_location[0] in range((beam5_location[0])- 75, (beam5_location[0])+75) and player_location[1] in range((beam5_location[1])-5, (beam5_location[1]) + 5):
        return True
    if player_location[0] in range((beam6_location[0])- 75, (beam6_location[0])+75) and player_location[1] in range((beam6_location[1])-5, (beam6_location[1]) + 5):
        return True
    if player_location[0] in range((beam7_location[0])- 75, (beam7_location[0])+75) and player_location[1] in range((beam7_location[1])-5, (beam7_location[1]) + 5):
        return True

def score_(score, level):
    if score == 7:
        level += 1
        score = 0

for event in pygame.event.get():
    if event.type == QUIT:
        quit_game()
    if event.type == KEYDOWN:
        if event.key == K_LALT and K_F4:
                quit_game()
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

def run_game():
    score = 0
    level = 0
    moving_right = False
    moving_left = False
    while True:
        screen.fill((146,244,255))

        LIVESCORE_TEXT = get_font(50).render("SCORE:" + str(level), True, "#000000")
        LIVESCORETEXT_RECT = LIVESCORE_TEXT.get_rect(center=(700, 50))  
        screen.blit(LIVESCORE_TEXT,LIVESCORETEXT_RECT)

        screen.blit(player_image, player_location)
        screen.blit(beam_image, beam1_location)
        screen.blit(beam_image, beam2_location)
        screen.blit(beam_image, beam3_location)
        screen.blit(beam_image, beam4_location)
        screen.blit(beam_image, beam5_location)
        screen.blit(beam_image, beam6_location)
        screen.blit(beam_image, beam7_location)

        if player_location[1] == 300:
            if level < 20:
                beam1_location[1] -= 10
                beam2_location[1] -= 10
                beam3_location[1] -= 10
                beam4_location[1] -= 10
                beam5_location[1] -= 10
                beam6_location[1] -= 10
                beam7_location[1] -= 10
            elif 20 <= level < 50:
                beam1_location[1] -= 12
                beam2_location[1] -= 12
                beam3_location[1] -= 12
                beam4_location[1] -= 12
                beam5_location[1] -= 12
                beam6_location[1] -= 12
                beam7_location[1] -= 12
            elif 50 <= level < 100:
                beam1_location[1] -= 15
                beam2_location[1] -= 15
                beam3_location[1] -= 15
                beam4_location[1] -= 15
                beam5_location[1] -= 15
                beam6_location[1] -= 15
                beam7_location[1] -= 15
            elif 100 <= level < 200:
                beam1_location[1] -= 20
                beam2_location[1] -= 20
                beam3_location[1] -= 20
                beam4_location[1] -= 20
                beam5_location[1] -= 20
                beam6_location[1] -= 20
                beam7_location[1] -= 20
            else:
                beam1_location[1] -= 30
                beam2_location[1] -= 30
                beam3_location[1] -= 30
                beam4_location[1] -= 30
                beam5_location[1] -= 30
                beam6_location[1] -= 30
                beam7_location[1] -= 30

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

        if moving_right == True:
            player_location[0] += 10
        if moving_left == True:
            player_location[0] -= 10

        player_rect.x = player_location[0]
        player_rect.y = player_location[1]

        if collision() == True:
            mixer.music.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Sound Effects/DeathSound.mp3')
            mixer.music.play()
            break           

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

        if player_location[0] < 0:
            player_location[0] = 1400
        if player_location[0] > 1400:
            player_location[0] = 0

        if score == 7:
            level += 1
            score = 0
            if level % 10 == 0:
                mixer.music.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Sound Effects/Level10Sound.mp3')
                mixer.music.play()
            else:
                mixer.music.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Sound Effects/LevelSound.mp3')
                mixer.music.play()
                    
        pygame.display.update()
        clock.tick(60)
    
    while True:
        screen.blit(DeathScreenBG, DeathScreenBG_location)

        DEATH_TEXT = get_font(150).render("You Died", True, "#ff0000")
        DEATHTEXT_RECT = DEATH_TEXT.get_rect(center=(700, 100))

        SCORE_TEXT = get_font(100).render('Score:' + str(level), True, '#ff6600')
        SCORETEXT_RECT = SCORE_TEXT.get_rect(center=(640,300))

        RETURNMAINMENU_TEXT = get_font(100).render('Main Menu', True, '#ff6600')
        RETURNMAINMENUTEXT_RECT = RETURNMAINMENU_TEXT.get_rect(center=(640,500))
        RETURNMAINMENUBUTTON = Button(image=pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Play_Rect.png'), pos=(640, 500), 
            text_input="Main Menu", font=get_font(75), base_color="#ff6600", hovering_color="White")

        MENUQUIT_TEXT = get_font(100).render('QUIT', True, '#ff6600')
        MENUQUIT_RECT = MENUQUIT_TEXT.get_rect(center=(640,700))
        MENUQUITBUTTON = Button(image=pygame.image.load('/Users/garrettsharpe/Documents/Code/Github/First-Python-Game/Art/Play_Rect.png'), pos=(640, 700), 
            text_input="QUIT", font=get_font(75), base_color="#ff6600", hovering_color="White")
            
        screen.blit(DEATH_TEXT, DEATHTEXT_RECT)
        screen.blit(SCORE_TEXT,SCORETEXT_RECT)
        screen.blit(RETURNMAINMENU_TEXT, RETURNMAINMENUTEXT_RECT)
        screen.blit(MENUQUIT_TEXT, MENUQUIT_RECT)
        

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if MENUQUITBUTTON.checkForInput(pygame.mouse.get_pos()):
                    #Sad sound?
                    quit_game()
                if RETURNMAINMENUBUTTON.checkForInput(pygame.mouse.get_pos()):
                    menu()
            if event.type == QUIT:
                quit_game()
            if event.type == KEYUP:
                if event.key == K_LALT and K_F4:
                    quit_game()

        pygame.display.update()
    
def leaderboard_screen():
    while True:
        screen.blit(BG, BG_location)
        #Get username 
        #disp leaderboard
        #back button
        
def update_leaderboard(user_name, user_score):
    leaderboard[user_name] = user_score
    return dict(sorted(leaderboard.items(), key=lambda x:x[1],reverse=True))

menu()