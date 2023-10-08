import pygame
import random
import time

"""""""""
Task at hand:

- Block that starts slightly off centre and then bounces off the corners.

"""""""""

def print_d(thing):
    print(thing)
    time.sleep(0.5)

def print_dd(thing):
    print(thing)
    time.sleep(1)

print_d("WELCOME TO THIS GAME:")
print_d("This allows you to control a moving ball by hitting it using the box controllable by the arrow keys.")
print_d("WHEN then box hits a corner, it bounces off.")
print_d("BUT if the box goes off the end, you lose a life.")
print_d("AT WHICH POINT the ball relocates randomly with a 2 second delay.")
print_d("Lives increase when the white barrier is hit.")
print_dd(3)
print_dd(2)
print_dd(1)

pygame.init()

#VARIABLE INITS
x_inc = 10
y_inc = 10
y_coord = 180
x_coord = 180
box_x = 20
box_y = 20
box_x_speed = 0
box_y_speed = 0
ball = pygame.Rect(x_coord, y_coord, 50, 50)
thingy = pygame.Rect(box_x, box_y, 35, 200)
total = 5

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

fill = OLIVE
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                box_y_speed = -10
            elif event.key == pygame.K_DOWN:
                box_y_speed = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                box_y_speed = 0

    box_x += box_x_speed
    box_y += box_y_speed

    if box_y >= 380:
        box_y = 380
    elif box_y <= 20:
        box_y = 20
    #end if 

    screen.fill(fill)

    # pygame.draw.rect(screen, COLOUR, [X_COORD, Y_COORD, WIDTH, HEIGHT], BORDER_THICKNESS)
    x_coord += x_inc
    y_coord += y_inc
    if y_coord >= 550 or y_coord <= 0:
        y_inc *= -1
    #end if

    if x_coord >= 750:
        x_inc *= -1
    #end if

    if x_coord <= 0:
        time.sleep(2)
        total -= 1
        x_coord, y_coord = random.randint(0, 800), random.randint(0, 600)

    ball = pygame.Rect(x_coord, y_coord, 50, 50)
    thingy = pygame.Rect(box_x, box_y, 35, 200)

    pygame.draw.rect(screen, NAVY, ball, 0)

    pygame.draw.rect(screen, WHITE, thingy, 0)

    if ball.colliderect(thingy) or thingy.colliderect(ball):
        y_inc *= -1
        x_inc *= -1
        total += 1

    font = pygame.font.SysFont('Palatino', 20, False, True)
    text = font.render("Lives: " + str(total), True, SILVER)
    screen.blit(text, [280, 30])

    if total == 0:
        pygame.time.wait(200)
        screen.blit(font.render("THE GAME HAS ENDED.", True, SILVER), [400, 30])
        pygame.time.wait(200)
        pygame.quit()

    # Update screen
    pygame.display.flip()

    # 60 updates per second.
    clock.tick(60)
pygame.quit()

print("WELL DONE!")