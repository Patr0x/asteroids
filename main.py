import sys

import pygame
from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from asteroidfield import AsteroidField
from shot import Shot



def main():
    updatable = pygame.sprite.Group()  # Create a group to hold all updateable objects
    drawable = pygame.sprite.Group()  # Create a group to hold all drawable objects
    asteroids = pygame.sprite.Group() # Create a group to hold all asteroid objects
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # Set the containers for the Player class
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    break
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    