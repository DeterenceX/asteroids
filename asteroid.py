import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,surface):
        pygame.draw.circle(surface,(255,255,255),self.position, self.radius, width = 2)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            angle1 = self.velocity.rotate(random_angle)
            angle2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x,self.position.y, new_radius)
            ast2 = Asteroid(self.position.x,self.position.y, new_radius)
            ast1.velocity = angle1 * 1.2
            ast2.velocity = angle2 * 1.2

            for group in self.groups():
                group.add(ast1)
                group.add(ast2)