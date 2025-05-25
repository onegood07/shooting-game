# stage.py

from ..player.player import Player
from ..enemy.enemy import EnemyBase, all_sprites_group

import pygame
import random

WIDTH = 1000
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("슈팅게임")
    clock = pygame.time.Clock()

    player = Player()
    enemy_spawn_timer = 0
    enemy_spawn_interval = 2000  # 2초마다 적 생성

    running = True
    while running:
        dt = clock.tick(FPS)
        enemy_spawn_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # player.fire() 함수가 없으면 그냥 무시해도 됨
                    if hasattr(player, 'fire'):
                        player.fire()

        # 플레이어 움직임은 호출 안함 (아직 함수 없음)

        if enemy_spawn_timer >= enemy_spawn_interval:
            EnemyBase()
            enemy_spawn_timer = 0

        all_sprites_group.update()

        screen.fill(BLACK)
        player.draw(screen)
        all_sprites_group.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()