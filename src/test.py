import pygame
import sys

# 작동 확인용 코드
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("프로젝트 테스트 화면 - pygame import 확인용")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (400, 300), 50)
    pygame.display.flip()

pygame.quit()
sys.exit()

