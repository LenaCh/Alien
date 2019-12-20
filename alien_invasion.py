import pygame
from settings import Settings
from penguin import Penguin
import game_functions as gf
from pygame.sprite import Group

def startgame():
    pygame.init()
    ai_set = Settings()
    screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
    pygame.display.set_caption('buugggssss')
    penguin = Penguin(screen,  ai_set)
    bullets = Group()
    while True:
       gf.check_events(ai_set, screen, penguin, bullets)
       penguin.update()
       bullets.update()
       gf.update_screen(ai_set, screen, penguin, bullets)

startgame()
