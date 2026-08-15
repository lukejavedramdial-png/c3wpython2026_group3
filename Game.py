# Pygame template - skeleton for a new pygame project
# Use this file as reference when making your projects!
import pygame
import Obstacle 
import score
import random
import Food
# Make constants

WIDTH = 1093
HEIGHT = 700
FPS = 30
background = pygame.image.load("Background.png")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Make a sprite

class Duck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("duck.png").convert_alpha()
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

duck = Duck()
win_area = pygame.Rect(1000, 0, 110, HEIGHT)  # Define the win area as a rectangle
obstacle_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()
pygame.time.set_timer(pygame.USEREVENT, 2000)  # Add an obstacle every 2 seconds
game_score = score.RiverGameScore()
while running:
    # Clock
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            new_x = random.randint(200,800)
            new_obstacle = Obstacle.Obstacle((new_x, 0))
            obstacle_group.add(new_obstacle)
            pygame.time.set_timer(pygame.USEREVENT, 2000)  # Reset the timer for the next obstacle
    
    # Input
    keys = pygame.key.get_pressed()
    
    duck.move(keys)
    
    
    if keys[pygame.K_LSHIFT]:
        duck.speed = 10
    else:
        duck.speed = 5
        
    obstacle_group.update()
    if pygame.sprite.spritecollide(duck, obstacle_group, True):
        game_score.hit_obstacle()

    food_group.update()
    if pygame.sprite.spritecollide(duck, food_group, True):
        food_type = random.choice(["berries", "fish", "large_game"])
        game_score.collect_food(food_type)

    if win_area.colliderect(duck.rect):
        game_score.finish_crossing()
         # End the game after crossing the river
    # Drawing
    
    screen.blit(background, (0, 0))
    screen.blit(duck.image, duck.rect)
    obstacle_group.draw(screen)
    food_group.draw(screen)
    pygame.display.flip()
   
    

# quit the game after the loop exits
pygame.quit()