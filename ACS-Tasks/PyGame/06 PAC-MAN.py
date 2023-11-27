import pygame

pygame.init()

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

pygame.display.set_caption("PAC-MAN")

done = False
clock = pygame.time.Clock()

# BLOCKS CLASS #
class Block(pygame.sprite.Sprite):
    def __init__(self, blX, blY):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = blX
        self.rect.y = blY
    #end def
#end class

class Player(pygame.sprite.Sprite):
    def __init__(self, plX, plY):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.rect.x = plX
        self.rect.y = plY
        self.speedX = 0
        self.speedY = 0
        self.radius = 10
    #end def

    def update(self):
        pygame.draw.circle(screen, YELLOW, (self.rect.x + 10, self.rect.y + 10), self.radius)
        self.rect.x += self.speedX
        self.rect.y += self.speedY
    #end def

    def setSpeed(self, spX, spY):
        self.speedX = spX
        self.speedY = spY
#end class

walls = pygame.sprite.Group()
players = pygame.sprite.Group()

# DRAWS HORIZONTAL WALLS #
for _ in range(1, 39):
    wallBlock = Block(20 * _, 20)
    walls.add(wallBlock)
    wallBlock = Block(20 * _, 560)
    walls.add(wallBlock)
#end for

# DRAWS VERTICAL WALLS #
for _ in range(1, 29):
    wallBlock = Block(20, 20 * _)
    walls.add(wallBlock)
    wallBlock = Block(760, 20 * _)
    walls.add(wallBlock)
#end for

player = Player(400-10, 300-10)
players.add(player)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.setSpeed(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.setSpeed(1, 0)
            elif event.key == pygame.K_UP:
                player.setSpeed(0, -1)
            elif event.key == pygame.K_DOWN:
                player.setSpeed(0, 1)
        #end if
    #end for

    screen.fill(BLACK)

    walls.draw(screen)
    players.draw(screen)
    players.update()

    for allthewalls in walls:
        hit = pygame.sprite.spritecollide(allthewalls, players, True)
        print("YOU DIED")
    #end for

    pygame.display.flip()

    clock.tick(60)
#end while

pygame.quit()