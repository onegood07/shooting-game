from ..player.player import Player
from ..enemy.enemy import EnemyBase, enemy_group, enemy_bullet_group, all_sprites_group
import pygame
import random

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

    player = Player()
    player_life = 3

    enemy_spawn_timer = 0
    enemy_spawn_interval = 2000  # 2초마다 적 생성

    running = True
    while running:
        dt = clock.tick(FPS)
        enemy_spawn_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 게임 업데이트
        player.update()
        all_sprites_group.update()

        if enemy_spawn_timer >= enemy_spawn_interval:
            EnemyBase()
            enemy_spawn_timer = 0

        # --- 🔺 충돌 검사: 내 총알 vs 적 ---
        for bullet in player.bullets[:]:  # 복사본 순회
            for enemy in enemy_group:
                if bullet.rect.colliderect(enemy.collider):
                    enemy.kill()
                    player.bullets.remove(bullet)
                    break

        # --- 🔺 충돌 검사: 적 총알 vs 나 ---
        player_rect = pygame.Rect(player.x - player.radius, player.y - player.radius, player.radius*2, player.radius*2)
        for bullet in enemy_bullet_group:
            if bullet.rect.colliderect(player_rect):
                player_life -= 1
                bullet.kill()
                print(f"Player hit! Life remaining: {player_life}")
                if player_life <= 0:
                    print("Game Over")
                    running = False
                break

        # --- 🔺 화면 그리기 ---
        screen.fill(BLACK)
        player.draw(screen)
        all_sprites_group.draw(screen)

        # 🔺 목숨 표시
        life_text = font.render(f"LIFE: {player_life}", True, WHITE)
        screen.blit(life_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()