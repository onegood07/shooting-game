import random
import pygame
import os
from ..player.player import Player
from ..enemy.enemy import (
    EnemyBase,
    EnemyTank,
    EnemySpread,
    EnemyPatroller,
    all_sprites_group,
    enemy_group,
    enemy_bullet_group
)

WIDTH = 1000
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("슈팅게임")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # 📌 배경 이미지 로드
    current_path = os.path.dirname(__file__)
    bg_path = os.path.join(current_path, '../../assets/stageBackground.png')
    background_image = pygame.image.load(bg_path).convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    player = Player()
    player_life = 3

    enemy_spawn_timer = 0
    enemy_spawn_interval = 2000

    paused = False  # 일시정지 상태 변수

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 일시정지 토글
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused

        if not paused:
            enemy_spawn_timer += dt

            player.update()
            all_sprites_group.update()

            if enemy_spawn_timer >= enemy_spawn_interval:
                enemy_class = random.choice([EnemyTank, EnemySpread, EnemyPatroller])
                enemy_class()
                enemy_spawn_timer = 0

            # 플레이어 총알 - 적 충돌
            for bullet in player.bullets[:]:
                for enemy in enemy_group:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.kill()
                        player.bullets.remove(bullet)
                        break

            # 적 총알 - 플레이어 충돌
            player_rect = pygame.Rect(player.x - player.radius, player.y - player.radius, player.radius * 2, player.radius * 2)
            for bullet in enemy_bullet_group:
                if bullet.rect.colliderect(player_rect):
                    player_life -= 1
                    bullet.kill()
                    if player_life <= 0:
                        print("게임 종료")
                        running = False
                    break

        # 🔄 화면 그리기
        screen.blit(background_image, (0, 0))  # 배경 이미지 먼저
        player.draw(screen)
        all_sprites_group.draw(screen)

        # 일시정지 표시
        if paused:
            pause_text = font.render("PAUSED", True, WHITE)
            rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(pause_text, rect)

        # 목숨 표시
        life_text = font.render(f"LIFE: {player_life}", True, WHITE)
        screen.blit(life_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()