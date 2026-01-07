# note: 
# "uv run main.py" runs code. Use it check the code works
# "source .venv/bin/activate" activates the virtual environment

# libraries and modules
import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# main function
def main():
    # prints simple values
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initializing pygame and screen settings
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # initialize clock
    clock = pygame.time.Clock()
    dt = 0

    # creating player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # initialize player
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y)

    # creating asteroid group
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # creating asteroid field
    AsteroidField.containers = (updatable,)
    AsteroidField()

    # infinite while loop "Ctrl+C" closes the program
    while True:
        # log current state
        log_state()

        # Makes it so the window's close button actually work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update screen state
        screen.fill("black")    #sets black screen
        updatable.update(dt)    #Checks to rotate ship
        
        # checking for collisions
        for asteroid in asteroids:
            collision = player.collides_with(asteroid)

            if collision:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # draw sprites
        for sprite in drawable:
            sprite.draw(screen)     #draws the screen        

        # *Keep last!!!!*
        pygame.display.flip()     # reloads windows
        dt = clock.tick(60)/1000  # sets clock to 60 FPS and saves dt
        

if __name__ == "__main__":
    main()
