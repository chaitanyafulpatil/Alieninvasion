import sys
import pygame
from pygame.sprite import Group
from essentials.settings import Settings
from essentials.ship import Ship
from essentials.alien import Alien
import essentials.game_function as gf


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	
	while True :
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update( )
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens) 
		gf.update_screen(ai_settings, screen , ship, aliens, bullets)



run_game()
