import pygame, sys
from pygame.locals import *
import pygame_menu
from pygame import mixer
import random
import csv
import pandas as pd
from pathlib import Path

clock = pygame.time.Clock()

pygame.init()
mixer.init()

pygame.display.set_caption('Descending Dude')

WINDOW_SIZE = (1400,1000)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

mixer.music.set_volume(0.2)

ROOT_DIR = Path(__file__).parent
Art_DIR = ROOT_DIR / "Art"
Leaderboard_DIR = ROOT_DIR / "Leaderboard"
Music_DIR = ROOT_DIR / "Music"
SoundEffects_DIR = ROOT_DIR / "SoundEffects"

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
    return pygame.font.Font(Art_DIR/'04B_30__.TTF', size)

BG = pygame.image.load(Art_DIR/'Backgroundimage.png')
BG_location = [0,0]

DeathScreenBG = pygame.image.load(Art_DIR/'DeathScreenBG.png')
DeathScreenBG_location = [0,0]

username = 'User'

def menu():
    mixer.music.load(Music_DIR/'GameSong.mp3')
    mixer.music.play()
    while True:
        screen.blit(BG, BG_location)
        MENU_TEXT = get_font(80).render("Descending Dude", True, "#ff6600")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))

        PLAYBUTTON_TEXT = get_font(90).render('PLAY', True, '#ff6600')
        PLAYBUTTON_RECT = PLAYBUTTON_TEXT.get_rect(center=(640,275))
        PLAYBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(640, 275), 
            text_input="PLAY", font=get_font(75), base_color="#ff6600", hovering_color="White")

        LEADERBOARD_TEXT = get_font(90).render('LEADERBOARD', True, '#ff6600')
        LEADERBOARD_RECT = LEADERBOARD_TEXT.get_rect(center=(640,450))
        LEADERBOARDBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(640, 450), 
            text_input="LEADERBOARD", font=get_font(75), base_color="#ff6600", hovering_color="White")
        
        SKINSMENU_TEXT = get_font(90).render('SKINS', True, '#ff6600')
        SKINSMENU_RECT = SKINSMENU_TEXT.get_rect(center=(640,650))
        SKINSMENUBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(640, 650), 
            text_input="SKINS", font=get_font(75), base_color="#ff6600", hovering_color="White")
        
        MENUQUIT_TEXT = get_font(90).render('QUIT', True, '#ff6600')
        MENUQUIT_RECT = MENUQUIT_TEXT.get_rect(center=(640,825))
        MENUQUITBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(640, 825), 
            text_input="QUIT", font=get_font(75), base_color="#ff6600", hovering_color="White")
        
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(PLAYBUTTON_TEXT, PLAYBUTTON_RECT)
        screen.blit(LEADERBOARD_TEXT, LEADERBOARD_RECT)
        screen.blit(SKINSMENU_TEXT, SKINSMENU_RECT)
        screen.blit(MENUQUIT_TEXT,MENUQUIT_RECT)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if PLAYBUTTON.checkForInput(pygame.mouse.get_pos()):
                    run_game()
                if LEADERBOARDBUTTON.checkForInput(pygame.mouse.get_pos()):
                    leaderboard_screen()
                if SKINSMENUBUTTON.checkForInput(pygame.mouse.get_pos()):
                    skins_menu()
                if MENUQUITBUTTON.checkForInput(pygame.mouse.get_pos()):
                    quit_game()
            if event.type == QUIT:
                quit_game()
            if event.type == KEYUP:
                if event.key == K_LALT and K_F4:
                    quit_game()

        pygame.display.update()

def get_leaderboard():
    dataFrame = pd.read_csv(Leaderboard_DIR/'Userscores.csv')
    dataFrame.sort_values('ScoresMe', axis = 0, ascending=False, inplace=True, na_position ='first')
    
    dataFrame['ScoresMe'] = dataFrame.apply(lambda row: (row['User'], row['ScoresMe']), axis=1)

    sorted_list = []
    for i in range(len(dataFrame)):
        sorted_list.append((dataFrame['ScoresMe'])[i])
    
    sorted_list.sort(key = lambda x: x[1], reverse=True)
    return (sorted_list)

WorkerSprite = pygame.image.load(Art_DIR/'WorkerSprite3.png')
NinjaSprite = pygame.image.load(Art_DIR/'NinjaSprite.png')
ZombieSprite = pygame.image.load(Art_DIR/'ZombieSprite.png')
AstronautSprite = pygame.image.load(Art_DIR/'AstronautSprite.png')
SaakuSprite = pygame.image.load(Art_DIR/'SaakuSprite.png')
beam_image = pygame.image.load(Art_DIR/'BeamSprite.png')

player_image = WorkerSprite

player_location = [500,0]
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
    if player_location[0] in range((beam1_location[0])- 75, (beam1_location[0])+75) and player_location[1] in range((beam1_location[1])-30, (beam1_location[1]) + 30):
        return True
    if player_location[0] in range((beam2_location[0])- 75, (beam2_location[0])+75) and player_location[1] in range((beam2_location[1])-30, (beam2_location[1]) + 30):
        return True
    if player_location[0] in range((beam3_location[0])- 75, (beam3_location[0])+75) and player_location[1] in range((beam3_location[1])-30, (beam3_location[1]) + 30):
        return True
    if player_location[0] in range((beam4_location[0])- 75, (beam4_location[0])+75) and player_location[1] in range((beam4_location[1])-30, (beam4_location[1]) + 30):
        return True
    if player_location[0] in range((beam5_location[0])- 75, (beam5_location[0])+75) and player_location[1] in range((beam5_location[1])-30, (beam5_location[1]) + 30):
        return True
    if player_location[0] in range((beam6_location[0])- 75, (beam6_location[0])+75) and player_location[1] in range((beam6_location[1])-30, (beam6_location[1]) + 30):
        return True
    if player_location[0] in range((beam7_location[0])- 75, (beam7_location[0])+75) and player_location[1] in range((beam7_location[1])-30, (beam7_location[1]) + 30):
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
    player_location[1] = 0
    player_location[0] = 500
    beam1_location[1] += 400
    beam2_location[1] += 400
    beam3_location[1] += 400
    beam4_location[1] += 400
    beam5_location[1] += 400
    beam6_location[1] += 400
    beam7_location[1] += 400
    pygame.mixer.music.unload()

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
                beam1_location[1] -= 14
                beam2_location[1] -= 14
                beam3_location[1] -= 14
                beam4_location[1] -= 14
                beam5_location[1] -= 14
                beam6_location[1] -= 14
                beam7_location[1] -= 14
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
            mixer.music.load(SoundEffects_DIR/'DeathSound.mp3')
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
                mixer.music.load(SoundEffects_DIR/'Level10Sound.mp3')
                mixer.music.play()
            else:
                mixer.music.load(SoundEffects_DIR/'LevelSound.mp3')
                mixer.music.play()
                    
        pygame.display.update()
        clock.tick(60)

    with open(Leaderboard_DIR/'Userscores.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([username, level])

    
    while True:
        screen.blit(DeathScreenBG, DeathScreenBG_location)

        DEATH_TEXT = get_font(150).render("You Died", True, "#ff0000")
        DEATHTEXT_RECT = DEATH_TEXT.get_rect(center=(700, 100))

        SCORE_TEXT = get_font(100).render('Score:' + str(level), True, '#ff6600')
        SCORETEXT_RECT = SCORE_TEXT.get_rect(center=(640,300))

        RETURNMAINMENU_TEXT = get_font(100).render('Main Menu', True, '#ff6600')
        RETURNMAINMENUTEXT_RECT = RETURNMAINMENU_TEXT.get_rect(center=(640,500))
        RETURNMAINMENUBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(640, 500), 
            text_input="Main Menu", font=get_font(75), base_color="#ff6600", hovering_color="White")

        MENUQUIT_TEXT = get_font(100).render('QUIT', True, '#ff6600')
        MENUQUIT_RECT = MENUQUIT_TEXT.get_rect(center=(640,700))
        MENUQUITBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(640, 700), 
            text_input="QUIT", font=get_font(75), base_color="#ff6600", hovering_color="White")
            
        screen.blit(DEATH_TEXT, DEATHTEXT_RECT)
        screen.blit(SCORE_TEXT,SCORETEXT_RECT)
        screen.blit(RETURNMAINMENU_TEXT, RETURNMAINMENUTEXT_RECT)
        screen.blit(MENUQUIT_TEXT, MENUQUIT_RECT)
        

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if MENUQUITBUTTON.checkForInput(pygame.mouse.get_pos()):
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
    global username
    while True:
        screen.blit(BG, BG_location)
        text_screen = get_font(80).render('Username:',True,(255, 102, 0))
        user_text = get_font(80).render(username,True,(225,102, 0))
        input_rect = pygame.Rect(740,40,650,96)
        pygame.draw.rect(screen, (0, 0, 0), input_rect,2)
        inputrect_button = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(750, 50), 
            text_input="Main Menu", font=get_font(75), base_color="#ff6600", hovering_color="White")

        RETURNMAINMENU_TEXT = get_font(80).render('Main Menu', True, '#ff6600')
        RETURNMAINMENUTEXT_RECT = RETURNMAINMENU_TEXT.get_rect(center=(700,800))
        RETURNMAINMENUBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(700,800), 
            text_input="Main Menu", font=get_font(75), base_color="#ff6600", hovering_color="White")

        if len(get_leaderboard()) > 0:
            FirstScoreText = get_font(100).render('1.' + str(((get_leaderboard())[0])[0]) + ':' + str(((get_leaderboard())[0])[1]),True,(255, 102, 0))
        else:
            FirstScoreText = get_font(100).render('1.N/A',True,(255, 102, 0))
        if len(get_leaderboard()) > 1:
            SecondScoreText = get_font(100).render('2.' + str(((get_leaderboard())[1])[0]) + ':' + str(((get_leaderboard())[1])[1]),True,(255, 102, 0))
        else:
            SecondScoreText = get_font(100).render('2.N/A',True,(255, 102, 0))
        if len(get_leaderboard()) > 2:
            ThirdScoreText = get_font(100).render('3.' + str(((get_leaderboard())[2])[0]) + ':' + str(((get_leaderboard())[2])[1]),True,(255, 102, 0))
        else:
            ThirdScoreText = get_font(100).render('3.N/A',True,(255, 102, 0))
        if len(get_leaderboard()) > 3:
            FourthScoreText = get_font(100).render('4.' + str(((get_leaderboard())[3])[0]) + ':' + str(((get_leaderboard())[3])[1]),True,(255, 102, 0))
        else:
            FourthScoreText = get_font(100).render('4.N/A',True,(255, 102, 0))
        if len(get_leaderboard()) > 4:
            FifthScoreText = get_font(100).render('5.' + str(((get_leaderboard())[4])[0]) + ':' + str(((get_leaderboard())[4])[1]),True,(255, 102, 0))
        else:
            FifthScoreText = get_font(100).render('5.N/A',True,(255, 102, 0))
        
        screen.blit(text_screen, (50, 50))
        screen.blit(user_text,(750,50))
        screen.blit(RETURNMAINMENU_TEXT, RETURNMAINMENUTEXT_RECT)
        screen.blit(FirstScoreText, (200, 200))
        screen.blit(SecondScoreText, (200, 300))
        screen.blit(ThirdScoreText, (200,400))
        screen.blit(FourthScoreText, (200,500))
        screen.blit(FifthScoreText, (200,600))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if RETURNMAINMENUBUTTON.checkForInput(pygame.mouse.get_pos()):
                    menu()
                if inputrect_button.checkForInput(pygame.mouse.get_pos()):
                    active = True
                else:
                    active = False 
            if event.type == KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
                if len(username) > 9:
                    username = username[:-1]

def skins_menu():
    global player_image
    while True:
        AstronautSized = pygame.image.load(Art_DIR/'AstronautSpriteSized.png')
        ZombieSized = pygame.image.load(Art_DIR/'ZombieSpriteSized.png')
        WorkerSized = pygame.image.load(Art_DIR/'WorkerSpriteSized.png')
        SaakuSized = pygame.image.load(Art_DIR/'SaakuSpriteSized.png')
        NinjaSized = pygame.image.load(Art_DIR/'NinjaSpriteSized.png')
        mixer.music.load(Music_DIR/'GameSong.mp3')
        mixer.music.play()
        screen.blit(BG, BG_location)
        RETURNMAINMENU_TEXT = get_font(80).render('Main Menu', True, '#ff6600')
        RETURNMAINMENUTEXT_RECT = RETURNMAINMENU_TEXT.get_rect(center=(700,800))
        RETURNMAINMENUBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(700,800), 
            text_input="Main Menu", font=get_font(75), base_color="#ff6600", hovering_color="White")
        ASTRONAUTBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(150,450), 
            text_input="", font=get_font(75), base_color="#ff6600", hovering_color="White")
        ZOMBIEBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(350,450), 
            text_input="", font=get_font(75), base_color="#ff6600", hovering_color="White")
        WORKERBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(650,450), 
            text_input="", font=get_font(75), base_color="#ff6600", hovering_color="White")
        SAAKUBUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(950,450), 
            text_input="", font=get_font(75), base_color="#ff6600", hovering_color="White")
        NINJABUTTON = Button(image=pygame.image.load(Art_DIR/'Play_Rect.png'), pos=(1200,450), 
            text_input="", font=get_font(75), base_color="#ff6600", hovering_color="White")
        

        screen.blit(RETURNMAINMENU_TEXT, RETURNMAINMENUTEXT_RECT)
        screen.blit(AstronautSized, [50,300])
        screen.blit(ZombieSized, [300,300])
        screen.blit(WorkerSized, [600,300])
        screen.blit(SaakuSized, [900,300])
        screen.blit(NinjaSized, [1150, 300])
        #Show what skin is chosen by glowing aura
        if player_image == AstronautSprite:
            screen.blit(pygame.image.load(Art_DIR/'Arrow.png'), [37,100])
        elif player_image == ZombieSprite:
            screen.blit(pygame.image.load(Art_DIR/'Arrow.png'), [287.5,100])
        elif player_image == WorkerSprite:
            screen.blit(pygame.image.load(Art_DIR/'Arrow.png'), [586.5,100])
        elif player_image == SaakuSprite:
            screen.blit(pygame.image.load(Art_DIR/'Arrow.png'), [887,100])
        elif player_image == NinjaSprite:
            screen.blit(pygame.image.load(Art_DIR/'Arrow.png'), [1138,100])
            
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if RETURNMAINMENUBUTTON.checkForInput(pygame.mouse.get_pos()):
                    menu()
                if ASTRONAUTBUTTON.checkForInput(pygame.mouse.get_pos()):
                    player_image = AstronautSprite
                if ZOMBIEBUTTON.checkForInput(pygame.mouse.get_pos()):
                    player_image = ZombieSprite
                if WORKERBUTTON.checkForInput(pygame.mouse.get_pos()):
                    player_image = WorkerSprite
                if SAAKUBUTTON.checkForInput(pygame.mouse.get_pos()):
                    player_image = SaakuSprite
                if NINJABUTTON.checkForInput(pygame.mouse.get_pos()):
                    player_image = NinjaSprite        

menu()