import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if self.containers:
            self.add(self.containers)
    
    def draw(self,surface):
        pygame.draw.circle(surface,(255,255,255),self.position, self.radius, width = 2)

    
    def update(self, dt):
        self.position = (self.velocity * dt) + self.position