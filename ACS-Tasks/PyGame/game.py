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


 
PI = 3.141592653
 
# Set the height and width of the screen
size = (800, 600) # Standard 4:3 ratio

# Set the size of the screen to be as listed above.
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sunrise / Sunset")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(NAVY)

    # Draw a rectangle

    # pygame.draw.rect(screen, COLOUR, [X_COORD, Y_COORD, WIDTH, HEIGHT], BORDER_THICKNESS)
    # HOUSE
    pygame.draw.rect(screen, MAROON, [300, 400, 200, 200], 0)

    # WINDOWS
    pygame.draw.rect(screen, CYAN, [100, 100, 30, 30], 0)
 
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Palatino', 20, False, True)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen

    text = font.render("Watch the Sun rise and fall!", True, SILVER)
    screen.blit(text, [280, 30])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()