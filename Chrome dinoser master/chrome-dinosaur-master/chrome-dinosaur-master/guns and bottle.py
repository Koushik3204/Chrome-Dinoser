import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Classes
class Revolver:
    def __init__(self):
        self.bullet_chamber = random.randint(1, 6)  # Randomly select a chamber for the bullet

    def spin_chamber(self):
        self.bullet_chamber = random.randint(1, 6)

class Bullet:
    def __init__(self):
        self.fired = False
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def fire(self):
        self.fired = True

class Bottle:
    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.radius = 30

    def draw(self, screen):
        pygame.draw.circle(screen, RED, self.position, self.radius)

    def check_collision(self, bullet):
        bullet_pos = bullet.position
        distance_squared = (bullet_pos[0] - self.position[0]) ** 2 + (bullet_pos[1] - self.position[1]) ** 2
        if distance_squared <= self.radius ** 2:
            return True
        return False

# Initialize game objects
revolver = Revolver()
bullet = Bullet()
bottle = Bottle()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guns and Bottle Game")

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                revolver.spin_chamber()
            elif event.key == pygame.K_RETURN:
                bullet.fire()

    # Draw bottle
    bottle.draw(screen)

    # Check collision
    if bullet.fired and bottle.check_collision(bullet):
        print("Bang! You hit the bottle. Game over!")
        running = False

    # Draw revolver
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 100, 50)) #example only
