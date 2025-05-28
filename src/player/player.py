# player.py

import pygame
from .bullet import Bullet


GRAVITY = 1.0
JUMP_POWER = -30

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
        self.lives=3
        self.is_alive=True
        self.rect=pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

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

    def shoot(self):
        # 원의 중심에서 총알 생성
        bullet = Bullet(self.x + self.radius, self.y)
        self.bullets.append(bullet)

    def update(self):
        self.handle_input()

        if self.is_jumping:
            self.y += self.jump_velocity
            self.jump_velocity += GRAVITY

            if self.y >= 500:
                self.y = 500
                self.is_jumping = False
                self.jump_velocity = 0

        for bullet in self.bullets:
            bullet.update()
        self.rect.x=self.x-self.radius
        self.rect.y=self.y-self.radius
        


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        for bullet in self.bullets:
            bullet.draw(screen)
    def take_hit(self):
        self.lives-=1
        print(f"남은 목숨: {self.lives}")
        if self.lives <=0:
            self.is_alive=False
            print("플레이어 사망")