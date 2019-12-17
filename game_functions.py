import sys
import pygame
from bullet import Bullet


def check_events(ai_set, screen, penguin, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(penguin, event, ai_set, bullets, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(penguin, event)

def check_keydown_events(penguin,event,ai_set,screen, bullets):
    # нажатие клавиши
     if event.key == pygame.K_RIGHT:
         # Переместить корабль вправо.
         penguin.moove_right = True
     elif event.key == pygame.K_LEFT:
         # Переместить корабль влево.
         penguin.moove_left = True
     elif event.key == pygame.K_UP:
         # Переместить корабль влево.
         penguin.moove_up = True
     elif event.key == pygame.K_DOWN:
         # Переместить корабль влево.
         penguin.moove_down = True
     elif event.key == pygame.K_SPACE:
         new_bullet = Bullet(ai_set, screen, penguin)
         # bullets = pygame.sprite.Group()
         bullets.add(new_bullet)

def check_keyup_events(penguin, event):
    # отпускание клавиши
    if event.key == pygame.K_RIGHT:
       penguin.moove_right = False
    elif event.key == pygame.K_LEFT:
       penguin.moove_left = False
    elif event.key == pygame.K_UP:
       penguin.moove_up = False
    elif event.key == pygame.K_DOWN:
       penguin.moove_down = False

def update_screen(ai_set, screen, penguin , bullets):
    screen.fill(ai_set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    penguin.blitme()
    pygame.display.flip()