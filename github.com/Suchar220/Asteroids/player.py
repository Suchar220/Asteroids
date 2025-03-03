# This should be at the top of your player.py file, not inside any class
from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS

# Then define your class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        # Also initialize the rotation
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)