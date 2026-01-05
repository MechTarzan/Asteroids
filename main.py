# note: 
# "uv run main.py" runs code. Use it check the code works
# "source .venv/bin/activate" activates the virtual environment

# libraries and modules
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # initialize player
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y)

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
        player.update(dt)       #Checks to rotate ship
        player.draw(screen)     #draws the screen        

        # *Keep last!!!!*
        pygame.display.flip()     # reloads windows
        dt = clock.tick(60)/1000  # sets clock to 60 FPS and saves dt
        

if __name__ == "__main__":
    main()
