# -*- coding: utf-8 -*-
import sys
import pygame
from aliens import Alien
from bullet import Bullet
from time import sleep
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit(0)
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=True
			elif event.key==pygame.K_LEFT:
				ship.moving_left=True
			elif event.key==pygame.K_UP:
				ship.moving_up=True
			elif event.key==pygame.K_DOWN:
				ship.moving_down=True
			elif event.key==pygame.K_SPACE:
				if len(bullets)>=ai_settings.bullet_allowed:
					pass
				else:
					new_bullet=Bullet(ai_settings,screen,ship)
					bullets.add(new_bullet)			
		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=False
			elif event.key==pygame.K_LEFT:
				ship.moving_left=False
			elif event.key==pygame.K_UP:
				ship.moving_up=False
			elif event.key==pygame.K_DOWN:
				ship.moving_down=False
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
			
def update_screen(ai_settings,stats,screen,ship,aliens,bullets,play_button,sb):#包含让游戏得以不无敌的原因
	screen_rect=screen.get_rect()
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	for alien in aliens:
		if alien.rect.bottom >=screen_rect.bottom:
			ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
			break
	if pygame.sprite.spritecollideany(ship,aliens):
			ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
	if not stats.game_active:
		play_button.draw_button()
	
	aliens.draw(screen)
	sb.show_score()
	pygame.display.flip()

	
def get_number_aliens_x(ai_settings,alien_width):
	available_space_x=ai_settings.screen_width-2*alien_width
	number_alien_x=int(available_space_x/(2*alien_width))
	return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
	available_space_y=(ai_settings.screen_height-(7*alien_height)-ship_height)
	number_rows=int(available_space_y/(2*alien_height))
	return number_rows

def create_aliens(ai_settings,screen,aliens,alien_number,row_number):
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	alien=Alien(ai_settings,screen)
	number_alien_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_alien_x):
			create_aliens(ai_settings,screen,aliens,alien_number,row_number)

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
	stats.ship_left-=1
	aliens.empty()
	bullets.empty()
	create_fleet(ai_settings,screen,ship,aliens)
	ship.center_ship()
	if stats.ship_left==0:
		stats.game_active=False
	sb.prep_lives()
	sleep(0.5)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
	if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
		stats.game_active=True
		stats.reset_stats()
		pygame.mouse.set_visible(False)
		aliens.empty()
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		ai_settings.initialize_dynamic_settings()
	else:
		stats.game_active=False
		pygame.mouse.set_visible(True)
				
