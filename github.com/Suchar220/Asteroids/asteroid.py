from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
        self.radius = radius
    
    def draw(self, surface):
        # Override the draw method to draw a circle
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        # Override the update method to move the asteroid
        self.position += self.velocity * dt