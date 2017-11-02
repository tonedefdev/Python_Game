import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats 
from ship import Ship
from button import Button 
from scoreboard import Scoreboard
import game_functions as gf  

def run_game():
	
	#Initialize game and createa a screen object.	
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make the Play button
	play_button = Button(ai_settings, screen, "Play")

	#Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	#Make a ship.
	ship = Ship(ai_settings, screen)
	#Make a group to store bullets in.
	bullets = Group()
	aliens = Group ()

	#Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Set the background color.
	bg_color = (230, 230, 230)

	#Start the main loop for the game.
	while True:

		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
			aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets)

		gf.update_screen(ai_settings, screen, ship, stats, sb, aliens, bullets, play_button)
		
run_game()