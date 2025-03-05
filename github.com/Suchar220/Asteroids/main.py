import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    # Adding shots_group to Shot containers
    Shot.containers = (drawable, updatable, shots_group)
    
    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        
        # Remove player from updatable group to update it separately
        updatable.remove(player)
        
        # Update player with shots_group
        player.update(dt, shots_group)
        
        # Update other sprites
        for sprite in updatable:
            if sprite != player:  # Just to be extra safe
                sprite.update(dt)
        
        # Add player back to updatable group
        updatable.add(player)
        
        # Clear screen
        screen.fill("black")
        
        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)   
        # After update step in game loop - this should be indented the same as the lines above
        # After update step in game loop
        for asteroid in asteroids:
            for shot in shots_group:  # Loop through all bullets
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
            # What should happen when a bullet hits an asteroid?
            # According to the instructions...


        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
                
        print(clock.get_fps())
        pygame.display.flip()
if __name__ == "__main__":
    main()

