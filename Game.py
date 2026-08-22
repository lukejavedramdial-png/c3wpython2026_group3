# Pygame template - skeleton for a new pygame project
# Use this file as reference when making your projects!
import pygame
import Obstacle 
import score
import random
import Food
import sys
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
font = pygame.font.Font(None, 36)
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
pygame.time.set_timer(pygame.USEREVENT, 2000)
pygame.time.set_timer(pygame.USEREVENT+1, 2000)  # Add an obstacle every 2 seconds
game_score = score.RiverGameScore()
win = False
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
            pygame.time.set_timer(pygame.USEREVENT, random.randint(2000, 4000))  # Reset the timer for the next obstacle
        if event.type == pygame.USEREVENT+1:
            new_x = random.randint(200,800)
            new_food = Food.Food((new_x, 0))
            food_group.add(new_food)
            pygame.time.set_timer(pygame.USEREVENT+1, random.randint(3000, 5000))  # Reset the timer for the next food item
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

    if win_area.colliderect(duck.rect) and win == False:
        game_score.finish_crossing() 
        win = True
         # End the game after crossing the river
    # Drawing
    
    screen.blit(background, (0, 0))
    screen.blit(font.render(f"Score: {game_score.score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Health: {game_score.health}", True, (255, 0, 0)), (10, 50))
    screen.blit(duck.image, duck.rect)
    obstacle_group.draw(screen)
    food_group.draw(screen)
    if win == True:
        screen.fill((0, 0, 255))
        screen.blit(font.render(f"You Win! Your score was {game_score.score}", True, (0, 255, 0)), (WIDTH // 2 - 50, HEIGHT // 2))
    if game_score.health <= 0:
        screen.fill((255, 0, 0))
        screen.blit(font.render(f"You Lose! Your score was {game_score.score}", True, (255, 255, 255)), (WIDTH // 2 - 50, HEIGHT // 2))
    pygame.display.flip()
    
   
    

# quit the game after the loop exits
pygame.quit()