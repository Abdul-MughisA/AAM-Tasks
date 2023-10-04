import pygame

"""""""""
Task at hand:

- Block that starts slightly off centre and then bounces off the corners.

"""""""""

pygame.init()

#VARIABLE INITS
x_inc = 20
y_inc = 20
y_coord = 50
x_coord = 0

#COLOURS

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

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Boingy Boingy")
 
done = False
clock = pygame.time.Clock()
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  
    screen.fill(OLIVE)

    # pygame.draw.rect(screen, COLOUR, [X_COORD, Y_COORD, WIDTH, HEIGHT], BORDER_THICKNESS)
    x_coord += x_inc
    y_coord += y_inc
    if y_coord >= 550 or y_coord <= 0:
        y_inc = y_inc * -1
    #end if

    if x_coord >= 750 or x_coord <= 0:
        x_inc = x_inc * -1
    #end if
    pygame.draw.rect(screen, NAVY, [x_coord, y_coord, 50, 50], 0)

    

    # Font, size, bold, italics
    font = pygame.font.SysFont('Palatino', 20, False, True)
 
    # "True" = anti-aliased.
    text = font.render("Watch this box go BOING!", True, SILVER)
    screen.blit(text, [280, 30])

    font = pygame.font.SysFont('Palatino', 20, True, True)
    text = font.render("!! SO AMAZING !!", True, SILVER)
    screen.blit(text, [320, 60])
 
    # Update screen
    pygame.display.flip()
 
    # 60 updates per second.
    clock.tick(60)
 
pygame.quit()