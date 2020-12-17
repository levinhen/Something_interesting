# -*- coding: utf-8 -*-
import sys
import pygame

class Ship():
	def __init__(self,screen):
		self.screen=screen
		self.image=pygame.image.load('ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
	def blitme(self):
		self.screen.blit(self.image,self.rect)
def check_events(ship):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				ship.rect.centerx+=1
def run_game():
	pygame.init()
	screen=pygame.display.set_mode((1200,700))
	pygame.display.set_caption('Alien Invasion')
	bg_color=(230,230,230)
	ship=Ship(screen)
	
	while True:
		check_events(ship)
		screen.fill(bg_color)
		ship.blitme()
		pygame.display.flip()

run_game()
