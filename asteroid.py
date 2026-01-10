import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,LINE_WIDTH)

    def update(self, dt):
        # moves it in a straight line
        self.position += self.velocity*dt

    def split(self):

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            log_event("asteroid_split")

            # new speed and radius
            trajectory = random.uniform(20,50)
            velocity1 = 1.2*self.velocity.rotate(trajectory)
            velocity2 = 1.2*self.velocity.rotate(-trajectory)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # creating the asteroids 
            asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
            asteroid1.velocity = velocity1
            asteroid2.velocity = velocity2

            # kill old asteroid
            self.kill()
            