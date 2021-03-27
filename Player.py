import pygame, sys, random
from Block import Block


WIDTH = 1280
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constrain()