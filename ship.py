import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""docstring for Ship"""
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/ship3.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		self.move_right = False
		self.move_left = False

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.move_right and self.rect.right<self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.move_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center	


	def center_ship(self):
		self.center = self.screen_rect.centerx

