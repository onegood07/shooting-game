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

class EnemyTank(EnemyBase):
    def __init__(self):
        super().__init__(color=WHITE)
        self.fire_interval = 1300
        self.collider.y = HEIGHT - 40  # 위치 설정시 collider 사용

    def fire(self):
        BulletFromEnemy(self.collider.centerx, self.collider.top, vy=0, vx=-4)


class EnemySpread(EnemyBase):
    def __init__(self):
        super().__init__(color=WHITE)
        self.fire_interval = 1600

    def fire(self):
        BulletFromEnemy(self.rect.centerx, self.rect.bottom, vy=-1, vx=-3)
        BulletFromEnemy(self.rect.centerx, self.rect.bottom, vy=0, vx=-3)
        BulletFromEnemy(self.rect.centerx, self.rect.bottom, vy=1, vx=-3)


class EnemyPatroller(EnemyBase):
    def __init__(self):
        super().__init__(color=WHITE)
        self.fire_interval = 1600
        self.direction = 1  # 1이면 아래, -1이면 위
        self.move_speed = 1
        self.top_limit = HEIGHT // 3
        self.bottom_limit = HEIGHT // 2

    def update(self):
        # 위아래로 왕복
        self.rect.y += self.direction * self.move_speed
        if self.rect.y <= self.top_limit or self.rect.y >= self.bottom_limit:
            self.direction *= -1
        super().update()

    def fire(self):
        # 수직으로 아래 방향 탄환 발사
        BulletFromEnemy(self.rect.centerx, self.rect.bottom, vy=0, vx=-3)