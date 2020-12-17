# -*- coding: utf-8 -*-
class Settings():
	def __init__(self):
		self.screen_width=1000
		self.screen_height=600
		self.bg_color=(230,230,230)
		
		self.ship_limit=3
		
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullet_allowed=5
		
		self.fleet_drop_speed=10
		
		self.speedup_scale=1.1
		self.score_scale=1.5
		
		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		self.ship_speed=4.0
		self.alien_speed=1
		self.bullet_speed_factor=3
		self.direction=1
		self.alien_points=1
		
	def increase_speed(self):
		self.ship_speed*=self.speedup_scale
		self.alien_speed*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_points=int(self.score_scale*self.alien_points)
