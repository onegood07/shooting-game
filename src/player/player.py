# player.py

import pygame

class Player:
    def __init__(self):
        self.x=100
        self.y=500
        self.radius = 25
        self.color = (50,50,50)
        self.speed=5
        self.jump_velocity=0
        self.is_jumping=False
        self.bullets=[] 

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        for bullet in self.bullets:
            bullet.draw(screen)