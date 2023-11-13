# This is a game of space invaders.

import pygame
import random
import math

pygame.init()

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

COLOUR1 = (168, 165, 204)   #DIRTY MAUVE
COLOUR2 = (97, 93, 153)     #DARKER MAUVE
COLOUR3 = (205, 201, 255)   #LIGHTEST COLOUR
COLOUR4 = (47, 42, 102)     #DARKER RICH MAUVE
COLOUR5 = (13, 11, 51)      #DARKEST COLOUR

size = (800, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

bullet_list = pygame.sprite.Group()
 
done = False
clock = pygame.time.Clock()

# CLASSES
class Invader(pygame.sprite.Sprite):

    #CONSTRUCTORS
    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(COLOUR2)
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(-50, 0)
    #end def

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

class Player(pygame.sprite.Sprite):

    def __init__(self, s_width, s_length):
        super().__init__()

        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(COLOUR5)
        self.speed = 0
        self.rect = self.image.get_rect()
        self.rect.x = size[0] / 2 - s_width
        self.rect.y = size[1] - s_length

    def update(self):
        if self.rect.y > 600:
            self.rect.y -= 600
        elif self.rect.x < 0:
            self.rect.x += 800
        elif self.rect.x > 800:
            self.rect.x -= 800
        else:
            self.rect.x = self.rect.x + self.speed
    #end def

    def player_set_speed(self, speed):
        self.speed = speed
#end class

class Bullets(pygame.sprite.Sprite):
    def __init__(self, b_width, b_length):
        super().__init__()

        self.image = pygame.Surface([b_width, b_length])
        self.image.fill(COLOUR2)
        self.speed = -1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(-50, 0)

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

sprites = pygame.sprite.Group()
number_of_invaders = 10
for i in range(0, number_of_invaders):
    invader = Invader(10, 10)
    sprites.add(invader)
#end for
player = Player(10, 10)
sprites.add(player)

 
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            #INSERT BULLET THING
        #end if
    #end for
  
    # Clear the screen and set the screen background
    screen.fill(COLOUR3)

    sprites.draw(screen)
    sprites.update()

    for bullet in bullet_list:

        block_hit_list = pygame.sprite.spritecollide(player, invader, True)

        for block in block_hit_list:
            sprites.remove(block)
        #end for
    #end for

    pygame.display.flip()
 
    # 60 updates per second.
    clock.tick(60)
#end while
 
pygame.quit()
