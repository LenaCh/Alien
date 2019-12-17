import pygame
from settings import Settings


class Penguin():
    def __init__(self, screen, ai_set):
        self.screen = screen
        self.ai_set = ai_set
        self.image = pygame.image.load('images/penguin.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moove_right = False
        self.moove_left = False
        self.moove_up = False
        self.moove_down = False
    def blitme(self):
            # """Рисует корабль в текущей позиции."""
         self.screen.blit(self.image, self.rect)
         # self.screen.blit(self.background_image, (0, 0))

    def update(self):
        # """Обновляет позицию корабля с учетом флагов."""
        # Обновляется атрибут center, не rect.
         if self.moove_right:
             # не позволяет выходить за экран правый
             if self.moove_right and self.rect.right < self.screen_rect.right:
                 self.rect.centerx += self.ai_set.penguin_speed_factor
         elif self.moove_left:
             # не позволяет выходить за экран левый
             if self.moove_left and self.rect.left > 0:
                 self.rect.centerx -= self.ai_set.penguin_speed_factor
             # Обновление атрибута rect на основании self.center
         elif self.moove_up:
             # двигается вверх
             if self.moove_up and self.rect.top >0:
                self.rect.bottom -= self.ai_set.penguin_speed_factor
         elif self.moove_down:
             # двигается вниз
             if self.moove_down and self.rect.bottom < self.screen_rect.bottom:
                self.rect.bottom += self.ai_set.penguin_speed_factor