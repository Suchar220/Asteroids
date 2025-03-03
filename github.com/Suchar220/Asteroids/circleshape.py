import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collides_with(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
    
    # Calculate sum of radii
        radii_sum = self.radius + other_circle.radius
    
    # If distance <= sum of radii, they're colliding
        return distance <= radii_sum