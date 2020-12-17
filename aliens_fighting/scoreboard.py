#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame.font
class Scoreboard():
	def __init__(self,ai_settings,screen,stats):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.stats=stats
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_lives()
		
	def prep_score(self):
		score_str=str(self.stats.score)
		self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=self.screen_rect.top
		
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.screen.blit(self.lives_image,self.lives_rect)

	def prep_high_score(self):
		self.high_score_image=self.font.render(str(self.stats.high_score),True,self.text_color,self.ai_settings.bg_color)
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.centerx=self.screen_rect.centerx
		self.high_score_rect.top=self.screen_rect.top
	
	def prep_level(self):
		self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.screen_rect.right-20
		self.level_rect.top=self.screen_rect.top+30
	
	def prep_lives(self):
		self.lives='lives:'+str(self.stats.ship_left)
		self.lives_image=self.font.render(self.lives,True,self.text_color,self.ai_settings.bg_color)
		self.lives_rect=self.lives_image.get_rect()
		self.lives_rect.left=self.screen_rect.left+20
		self.level_rect.top=self.screen_rect.top+20
