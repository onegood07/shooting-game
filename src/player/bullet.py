import pygame

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)   # 총알의 위치(x, y)와 크기(10x5)를 가진 사각형
        self.speed = 10                        # 총알이 움직이는 속도 (오른쪽으로)
        self.color = (255, 0, 0)               # 빨간색 (RGB)으로 그릴 예정

    def update(self):
        self.rect.x += self.speed              # 총알을 오른쪽으로 이동시킴

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # 총알을 화면에 그리기