# player.py

import pygame
from .bullet import Bullet
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SWOPEN10_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))
ASSET_DIR = os.path.join(SWOPEN10_DIR, 'assets')



class Player:
    def __init__(self):
        self.x=100
        self.y=500
        self.radius = 25
        self.color = (0,255,0)
        self.speed=5
        image_path = os.path.join(ASSET_DIR, "player.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        
        self.bullets=[] 
        self.lives=3
        self.is_alive=True
        self.rect=pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.shoot_cooldown = 300  # 밀리초 단위 (예: 0.3초)
        self.last_shot_time = 0

        

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y-= self.speed
        if keys[pygame.K_DOWN]:
            self.y+= self.speed
     

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            bullet = Bullet(self.x + self.radius, self.y)
            self.bullets.append(bullet)
            self.last_shot_time = current_time


    def update(self):
        self.handle_input()
       
        for bullet in self.bullets:
            bullet.update()
        self.rect.x=self.x-self.radius
        self.rect.y=self.y-self.radius
        


    def draw(self, screen):
        screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        for bullet in self.bullets:
            bullet.draw(screen)
        


    def take_hit(self):
        self.lives-=1
        print(f"남은 목숨: {self.lives}")
        if self.lives <=0:
            self.is_alive=False
            print("플레이어 사망")



