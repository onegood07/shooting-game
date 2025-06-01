import pygame
import random
import os

# 현재 스크립트 파일 위치 기준으로 상위 폴더(swopen10)를 찾아 assets 경로 설정
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SWOPEN10_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))
ASSET_DIR = os.path.join(SWOPEN10_DIR, 'assets')
# 기본 설정
WIDTH = 1000
HEIGHT = 600
FPS = 60
SIZE_UNIT = 8
INIT_POS = (WIDTH // 2, HEIGHT - 30)

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
score = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1952 GAME score: " + str(score))
clock = pygame.time.Clock()

all_sprites_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

class BulletFromEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vy=2, vx=0):
        super().__init__()
        image_path = os.path.join(ASSET_DIR, "bullet.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (4, 4))
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        all_sprites_group.add(self)
        enemy_bullet_group.add(self)

    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx

class EnemyBase(pygame.sprite.Sprite):
    def __init__(self, image_path, w=32, h=32):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.collider = self.rect

        self.rect.x = WIDTH + random.randint(0, 80)
        self.rect.y = random.randint(HEIGHT // 3, HEIGHT // 2)

        self.velocity_x = random.uniform(-2.5, -0.8) + (random.random() - 0.5) * 0.5
        self.last_fire_time = pygame.time.get_ticks()
        self.fire_interval = 1000
        self.hp = 1

        all_sprites_group.add(self)
        enemy_group.add(self)

    def update(self):
        self.rect.x += self.velocity_x

        if self.rect.right < 0:
            self.kill()

        now = pygame.time.get_ticks()
        if now - self.last_fire_time >= self.fire_interval:
            self.fire()
            self.last_fire_time = now

    def fire(self):
        BulletFromEnemy(self.rect.centerx, self.rect.bottom, vy=3)

class EnemyTank(EnemyBase):
    def __init__(self):
        image_path = os.path.join(ASSET_DIR, "enemy_t.png")
        super().__init__(image_path=image_path, w=80, h=80)
        self.fire_interval = 1300
        self.collider.y = HEIGHT - 80

    def fire(self):
        BulletFromEnemy(self.collider.centerx, self.collider.centery, vy=0, vx=-4)

class EnemySpread(EnemyBase):
    def __init__(self):
        image_path = os.path.join(ASSET_DIR, "enemy_s.png")
        super().__init__(image_path=image_path, w=48, h=48)
        self.fire_interval = 1600

    def fire(self):
        BulletFromEnemy(self.rect.centerx, self.rect.centery, vy=-1, vx=-3)
        BulletFromEnemy(self.rect.centerx, self.rect.centery, vy=0, vx=-3)
        BulletFromEnemy(self.rect.centerx, self.rect.centery, vy=1, vx=-3)

class EnemyPatroller(EnemyBase):
    def __init__(self):
        image_path = os.path.join(ASSET_DIR, "enemy_p.png")
        super().__init__(image_path=image_path, w=48, h=48)
        self.fire_interval = 1600
        self.direction = 1
        self.move_speed = 1
        self.top_limit = HEIGHT // 3
        self.bottom_limit = HEIGHT // 2

    def update(self):
        self.rect.y += self.direction * self.move_speed
        if self.rect.y <= self.top_limit or self.rect.y >= self.bottom_limit:
            self.direction *= -1
        super().update()

    def fire(self):
        BulletFromEnemy(self.rect.centerx, self.rect.centery, vy=0, vx=-3)

#테스트를 위한 실행코드
def game_loop():
    last_spawn_time = pygame.time.get_ticks()
    spawn_interval = 700

    while True:
        now = pygame.time.get_ticks()
        if now - last_spawn_time >= spawn_interval and len(enemy_group) < 10:
            enemy_class = random.choice([EnemyTank, EnemySpread, EnemyPatroller])
            enemy_class()
            last_spawn_time = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        all_sprites_group.update()
        all_sprites_group.draw(screen)
        pygame.display.set_caption("1952 GAME score: " + str(score))
        pygame.display.flip()
        clock.tick(FPS)

game_loop()