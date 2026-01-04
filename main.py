# note: 
# "uv run main.py" runs code. Use it check the code works
# "source .venv/bin/activate" activates the virtual environment

# libraries and modules
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

# main function
def main():
    # prints simple values
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initializing pygame and displaying GUI
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # infinite while loop "Ctrl+C" closes the program
    while True:
        # log current state
        log_state()

        # Makes it so the window's close button actually work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # displays a black sreen
        screen.fill("black")

        # Reloads screen *Keep last!!!!*
        pygame.display.flip()

if __name__ == "__main__":
    main()
