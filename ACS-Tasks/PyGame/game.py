import pygame
import time
 
"""""""""
Task at hand:

- Static house (middle bottom of screen)
  - Windows
  - Chimney
  - Frame (using a triangle)

- Sun moving across the screen from LEFT to RIGHT (from x = 0 to x = length of screen)
- Changes colour from night when x-coordinate out of bounds

"""""""""

# Initialize the game engine
pygame.init()
 
# Define some colors

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

BROWN = (150, 75, 0)

var_x_rect = 100
var_y_rect = 100
var_height_rect = 100
var_width_rect = 100
 
PI = 3.141592653
 
size = (800, 600) # Standard 4:3 ratio

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sunrise / Sunset")
 
done = False
clock = pygame.time.Clock()
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  
    # Clear the screen and set the screen background
    screen.fill(NAVY)

    # pygame.draw.rect(screen, COLOUR, [X_COORD, Y_COORD, WIDTH, HEIGHT], BORDER_THICKNESS)

    # HOUSE
    pygame.draw.rect(screen, MAROON, [300, 400, 200, 200], 0)

    #CHIMNEY ******** NOT YET FINISHED *******

    pygame.draw.rect(screen, MAROON, [425, 300, 40, 80], 0)

    #WINDOWS

    #WINDOW TOP LEFT
    pygame.draw.rect(screen, CYAN, [320, 420, 60, 60], 0)

    #WINDOW TOP RIGHT
    pygame.draw.rect(screen, CYAN, [420, 420, 60, 60], 0)

    #DOOR

    pygame.draw.rect(screen, BROWN, [375, 540, 50, 60], 0)

    #DOORKNOB
    pygame.draw.circle(screen, YELLOW, [385, 570], 5)

    #ROOF
    pygame.draw.polygon(screen, BROWN, [(290, 400), (510, 400), (400, 300)], 0)

    #MOVING CIRCLE


 
    # Font, size, bold, italics
    font = pygame.font.SysFont('Palatino', 20, False, True)
 
    # "True" = anti-aliased.
    # Creates image only.

    text = font.render("Watch the Sun rise and fall!", True, SILVER)
    screen.blit(text, [280, 30])

    font = pygame.font.SysFont('Palatino', 20, True, True)
    text = font.render("JUST LIKE THE CHINESE EMPIRE", True, SILVER)
    screen.blit(text, [250, 60])
 
    # Update screen
    pygame.display.flip()
 
    # 60 updates per second.
    clock.tick(60)
 
pygame.quit()