# This is a game of space invaders.

import pygame
import random
import math
import time

pygame.init()

# SETS ALL THE BASIC COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SILVER = (192, 192, 192)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)

# SETS COLOURS IN MY PURPLE COLOUR SCHEME
COLOUR1 = (168, 165, 204)   #DIRTY MAUVE
COLOUR2 = (97, 93, 153)     #DARKER MAUVE
COLOUR3 = (205, 201, 255)   #LIGHTEST COLOUR
COLOUR4 = (47, 42, 102)     #DARKER RICH MAUVE
COLOUR5 = (13, 11, 51)      #DARKEST COLOUR

# Sets screen size
size = (800, 600)
screen = pygame.display.set_mode(size)

# Sets name of game
pygame.display.set_caption("Space Invaders")

# Variable used to end game
done = False

# Sets clock for PyGame
clock = pygame.time.Clock()

# Sets the 2 variables needed for scoring
lostBullets = 0
score = 0

# Sets the function which allows me to display the score in the corner
font = pygame.font.SysFont("Palatino", 40)
def text(x, y, txt, txtcolor):
    display_text = font.render(txt, True, txtcolor)
    screen.blit(display_text, (x, y))

# INVADER CLASS #
# Sets colour, size and speed
class Invader(pygame.sprite.Sprite):

    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(COLOUR2)
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(-300, 0)
    #end def

    def update(self):
        # Checks if the invader goes beyond the bottom of the screen
        if self.rect.y > 600:
            global lostBullets
            lostBullets += 1
            print("You are a failure.")
            # Tells the user he is a failure in the terminal for frequent harrassment
            self.kill()
        elif self.rect.x < 0:
            self.rect.x += 800
        elif self.rect.x > 800:
            self.rect.x -= 800
        else:
            self.rect.y = self.rect.y + self.speed
    #end def
#end class

# PLAYER CLASS #
class Player(pygame.sprite.Sprite):

    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(COLOUR5)
        self.speed = 0
        self.rect = self.image.get_rect()
        self.rect.x = size[0] / 2 - s_width
        self.rect.y = 500

    def update(self):
        if self.rect.y > 600:
            self.rect.y -= 600
        elif self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 800:
            self.rect.x = 800
        else:
            self.rect.x = self.rect.x + self.speed
    #end def

    def player_set_speed(self, speed):
        self.speed = speed
    #end def
#end class

# BULLETS CLASS #
class Bullets(pygame.sprite.Sprite):
    def __init__(self, b_width, b_length):
        super().__init__()

        self.image = pygame.Surface([b_width, b_length])
        self.image.fill(COLOUR2)
        self.speed = -10
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 25/2
        self.rect.y = player.rect.y

    def update(self):
        if self.rect.y > 600:
            self.rect.y -= 600
        elif self.rect.x < 0:
            self.rect.x += 800
        elif self.rect.x > 800:
            self.rect.x -= 800
        else:
            self.rect.y = self.rect.y + self.speed
    #end def
#end class

# Creates groups to refer to all the different types of sprites
sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
invaders = pygame.sprite.Group()

# Sets number of invaders and adds to groups
number_of_invaders = 200
for i in range(0, number_of_invaders):
    invader = Invader(10, 10)
    invaders.add(invader)
#end for

# Adds player
player = Player(25, 25)
sprites.add(player)

 
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-6)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(6)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            myBullet = Bullets(5, 5)
            bullets.add(myBullet)
            # Creates bullet and adds to class
        #end if
    #end for
  
    # Clear the screen and set the screen background
    screen.fill(COLOUR3)

    # Draws everything onto the screen
    sprites.draw(screen)
    bullets.draw(screen)
    invaders.draw(screen)
    sprites.update()
    bullets.update()
    invaders.update()

    for allthebullets in bullets:
        hit = pygame.sprite.spritecollide(allthebullets, invaders, True)
        if hit:
            score += 1
            # Increases the score when there is a hit
    #end for

    if len(invaders) == 0 and lostBullets == 0:
        # SHOWS POSITIVE MESSAGE
        screen.fill(GREEN)
        screen.blit(pygame.font.SysFont('Palatino', 35, False, False).render("You killed all the invaders!", True, BLACK), [200, 400])
    elif lostBullets > 0:
        # SHOWS NEGATIVE MESSAGE
        screen.fill(RED)
        screen.blit(pygame.font.SysFont('Palatino', 35, False, False).render("You are a failure!", True, BLACK), [275, 400])
        screen.blit(pygame.font.SysFont('Palatino', 35, False, False).render(str("Score: " + str(score)), True, BLACK), [360, 300])

    #end if

    # Shows score in the corner
    text(0,0,str(score),BLACK)

    pygame.display.flip()
    clock.tick(30)
#end while
 
pygame.quit()

# I have kept the code very basic because this way,
# I can understand the logic in everything that I've written.