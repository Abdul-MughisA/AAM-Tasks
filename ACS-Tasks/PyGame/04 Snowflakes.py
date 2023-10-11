# This is snowflakes.

import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
NAVY = (0, 0, 128)

size = (1680, 1050)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snowflakes")
 
done = False
clock = pygame.time.Clock()

# CLASSES
class Snow(pygame.sprite.Sprite):

    #CONSTRUCTORS
    def __init__(self, s_width, s_length, x, y):
        super().__init__()
        self.width = s_width
        self.length = s_length
        self.x_pos = x
        self.y_pos = y

        self.image= pygame.Surface([s_width, s_length])
        self.image.fill(WHITE)
        self.speed = 5
        pygame.draw.rect(self.image, WHITE)
    #end def
#end class

#GLOBAL VARIABLES
snow_list = []
for i in range(0, 50):
    flake = Snow(10, 10, random.randint(0, 500), 100)
    snow_list.__add__(flake)
#end for
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #end if
    #end for
  
    # Clear the screen and set the screen background
    screen.fill(NAVY)

    snow_list.draw(screen)

    pygame.display.flip()
 
    # 60 updates per second.
    clock.tick(60)
#end while
 
pygame.quit()