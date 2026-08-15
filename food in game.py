import pygame
import sys

# Initialize Pygame
pygame.init()

# Setup display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duck Food Art")

# Colors
BG_COLOR = (50, 50, 50)       # Dark gray background
BAG_COLOR = (210, 180, 140)   # Tan/burlap color
BAG_DARK = (180, 150, 110)    # Shadow color
WHITE = (255, 255, 255)       # Label color
GREEN = (34, 139, 34)         # Text color
FEET_COLOR = (255, 140, 0)    # Orange for duck icon
STITCH_COLOR = (139, 69, 19)  # Brown for stitch details

def draw_duck_food_bag(surface, x, y):
    """Draws a stylized bag of duck food at coordinates (x, y)"""
    
    # 1. Main Bag Body (polygon for a cinched sack shape)
    # Points ordered: top-left, top-right, bottom-right, bottom-left
    bag_points = [
        (x + 30, y + 40),   # Cinched neck left
        (x + 70, y + 40),   # Cinched neck right
        (x + 90, y + 150),  # Wide base right
        (x + 10, y + 150)   # Wide base left
    ]
    pygame.draw.polygon(surface, BAG_COLOR, bag_points)
    pygame.draw.polygon(surface, STITCH_COLOR, bag_points, 3) # Outline
    
    # 2. Flared Top (above the cinch)
    top_points = [
        (x + 20, y + 15),
        (x + 80, y + 15),
        (x + 70, y + 40),
        (x + 30, y + 40)
    ]
    pygame.draw.polygon(surface, BAG_COLOR, top_points)
    pygame.draw.polygon(surface, STITCH_COLOR, top_points, 3)
    
    # 3. Rope/Tie at the cinch
    pygame.draw.rect(surface, STITCH_COLOR, (x + 28, y + 38, 44, 6), 0, 3)
    
    # 4. White Label on the front
    label_rect = pygame.Rect(x + 25, y + 65, 50, 60)
    pygame.draw.rect(surface, WHITE, label_rect, 0, 4)
    pygame.draw.rect(surface, BAG_DARK, label_rect, 2, 4)
    
    # 5. Stylized Duck Icon on label (Circle head + Oval body + Orange beak/feet)
    pygame.draw.ellipse(surface, GREEN, (x + 35, y + 85, 25, 18))  # Duck body
    pygame.draw.circle(surface, GREEN, (x + 55, y + 80), 8)        # Duck head
    pygame.draw.polygon(surface, FEET_COLOR, [(x + 62, y + 78), (x + 68, y + 80), (x + 62, y + 84)]) # Beak
    pygame.draw.line(surface, FEET_COLOR, (x + 42, y + 102), (x + 42, y + 108), 2) # Foot 1
    pygame.draw.line(surface, FEET_COLOR, (x + 50, y + 102), (x + 50, y + 108), 2) # Foot 2

    # 6. Text on Label ("DUCK")
    font = pygame.font.SysFont("Arial", 12, bold=True)
    text_surface = font.render("DUCK", True, GREEN)
    surface.blit(text_surface, (x + 35, y + 112))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Clear screen
    screen.fill(BG_COLOR)
    
    # Draw the duck food bag in the center of the screen
    # (Subtracting half the asset width/height to center it perfectly)
    draw_duck_food_bag(screen, (SCREEN_WIDTH // 2) - 50, (SCREEN_HEIGHT // 2) - 80)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
