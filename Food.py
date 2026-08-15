import pygame
import random
class Food(pygame.sprite.Sprite):
    images = {"berry.png", "fish.png"}
    def __init__(self, position):
        super().__init__()
    
        self.image = pygame.image.load(random.choice(list(self.images))).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = random.randint(2, 4)  # Random speed for each obstacle
        self.rect.center = position
    def update(self):
        self.rect.y += self.speed