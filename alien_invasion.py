import pygame
from pygame.sprite import Group

from setting import Setting
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Setting()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings,screen,"Play")
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	ship = Ship(ai_settings,screen)
	aliens  = Group()
	bullets = Group()
	gf.create_fleet(ai_settings,screen,aliens,ship)
	
	while True:
		gf.check_events(ai_settings,screen,ship,bullets,
			stats,play_button,aliens,sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,ship,screen,bullets,aliens,
				stats,sb)
			gf.update_aliens(ai_settings,aliens,ship,stats,screen,
				bullets,sb)
		gf.update_screen(ai_settings,screen,ship,bullets,aliens
				,play_button,stats,sb)

run_game()
