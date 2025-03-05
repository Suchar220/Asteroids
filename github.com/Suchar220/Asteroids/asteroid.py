from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
        self.radius = radius
    
    def draw(self, surface):
        # Override the draw method to draw a circle
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        # Override the update method to move the asteroid
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)

        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids
        # First asteroid
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2
        
        # Second asteroid
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2

        