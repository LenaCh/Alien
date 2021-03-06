import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_set, screen, penguin):
        super().__init__()
        self.screen = screen
        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_set.bullet_with, ai_set.bullet_height)
        self.rect.centerx = penguin.rect.centerx
        self.rect.top = penguin.rect.top
        self.y = float(self.rect.y)
        self.color = ai_set.bullet_color
        self.speed_factor = ai_set.bullet_speed_factor



    def update(self):
        """Перемещает пулю вверх по экрану."""
        self.y -= self.speed_factor
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)


