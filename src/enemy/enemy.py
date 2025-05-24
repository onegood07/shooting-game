# enemy

import pygame
import random
#기본 크기,프레임 블록크기 설정
WIDTH=1000
HEIGHT=600
FPS=60
SIZE_UNIT=8

#색깔
WHITE = (255, 255, 255)


# 이미지 넣을 예정이므로 스프라이트 그룹 사용 
all_sprites_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()


class BulletFromEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vy=0, vx=0):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        all_sprites_group.add(self)
        enemy_bullet_group.add(self)

    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx


class EnemyBase(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, w=SIZE_UNIT * 4, h=SIZE_UNIT*4):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)

        # 실제 rect는 유지 (Pygame 스프라이트 필수)
        self.rect = self.image.get_rect()
        
        # 이미지가 들어가 보이는 사이즈가 달라질 예정으로 충돌박스로 이름 변경
        self.collider = self.rect

        self.rect.x = WIDTH + random.randint(0, 80)
        self.rect.y = random.randint(HEIGHT // 3, HEIGHT // 2)

        self.velocity_x = random.uniform(-2.5, -0.8) + (random.random() - 0.5) * 0.5
        self.last_fire_time = pygame.time.get_ticks()
        self.fire_interval = 1000
        self.hp = 1
        #추후 플레이어클래스에 탄환 도입되면 체력관련 추가 예정

        all_sprites_group.add(self)
        enemy_group.add(self)

    def update(self):
        #시간에 따른 움직임 구현
        self.rect.x += self.velocity_x

        if self.rect.right < 0:
            self.kill()

        now = pygame.time.get_ticks()
        if now - self.last_fire_time >= self.fire_interval:
            self.fire()
            self.last_fire_time = now

    def fire(self):
        #함수는 자식클래스에서 변경해서 사용
        BulletFromEnemy(self.rect.centerx, self.rect.bottom, vy=0, vx=0)