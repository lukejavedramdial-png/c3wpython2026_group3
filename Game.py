# Pygame template - skeleton for a new pygame project
# Use this file as reference when making your projects!
import pygame

# Make constants

WIDTH = 720
HEIGHT = 720
FPS = 30

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Make a sprite

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("cat.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = 100
        self.rect.y = 100
        
        self.speed = 5
    def move(self, keys):
        # directions: 0 up, 1 right, 2 down, 3 left
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        

# initialize pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

# make game loop

# inside game loop:
# clock
# events
# drawing/rendering
# update events
# input

running = True

cat = Cat()
cat2 = Cat()

while running:
    # Clock
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Input
    keys = pygame.key.get_pressed()
    
    cat.move(keys)
    
    if keys[pygame.K_LSHIFT]:
        cat.speed = 10
    else:
        cat.speed = 5
    
    # Drawing
    screen.fill(color=BLUE) # drawing the background
    screen.blit(cat.image, cat.rect)
    pygame.display.flip()
    
    

# quit the game after the loop exits
pygame.quit()
