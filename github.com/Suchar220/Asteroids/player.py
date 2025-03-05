
from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
# Then define your class


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.rotation %= 360
        self.timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt, direction):
        if direction == "left":
            self.rotation -= PLAYER_TURN_SPEED * dt  # Rotate left
        elif direction == "right":
            self.rotation += PLAYER_TURN_SPEED * dt  # Rotate right
       
    def update(self, dt, shots_group=None):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, "left")
        if keys[pygame.K_d]:
            self.rotate(dt, "right")
        
        # Handle shooting if shots_group is provided
        if shots_group is not None and keys[pygame.K_SPACE]:
            new_shot = self.shoot()
            if new_shot:
                shots_group.add(new_shot)
        
        self.move(dt)

        if self.timer > 0:
            self.timer -= dt   
      
    
    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        if keys[pygame.K_w]:
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
            return new_shot
        return None
    
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        # Override the draw method to draw a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)
    
    def update(self, dt):
        # Override the update method to move the asteroid
        self.position += self.velocity * dt
    
    
        
    