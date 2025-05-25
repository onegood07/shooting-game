# player.py

import pygame

GRAVITY = 0.5
JUMP_POWER = -10

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

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP] and not self.is_jumping:
            self.jump_velocity = JUMP_POWER
            self.is_jumping = True
        
        if keys[pygame.K_SPACE]:
            self.shoot()


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        for bullet in self.bullets:
            bullet.draw(screen)