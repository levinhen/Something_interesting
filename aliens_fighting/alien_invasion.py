# -*- coding: utf-8 -*-
import pygame
import aliens as aa
from settings import Settings
from ship import Ship
from game_functions import check_events,update_screen,create_fleet
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	play_button =Button(ai_settings,screen,'play~')
	#开始定义
	
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	create_fleet(ai_settings,screen,ship,aliens)
	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	ship.center_ship()
	while True:
		check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
			aa.update_aliens(ai_settings,aliens)
			for bullet in bullets.copy():#移除子弹
				if bullet.rect.bottom<=0:
					bullets.remove(bullet)
			collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)#移除碰撞的子弹与敌军
			if collisions:
				for alien in collisions.values():
					stats.score+=ai_settings.alien_points*len(alien)
					sb.prep_score()
				if stats.score>stats.high_score:
					stats.high_score=stats.score
					sb.prep_high_score()
			if len(aliens)==0:#重新创造敌军
				bullets.empty()
				ai_settings.increase_speed()
				create_fleet(ai_settings,screen,ship,aliens)
				stats.level+=1
				sb.prep_level()
		update_screen(ai_settings,stats,screen,ship,aliens,bullets,play_button,sb)
run_game()
