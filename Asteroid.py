import pygame
from pygame.locals import *
from Vec2 import Vec2

class Asteroid:
	def __init__(self, w):
		self.pos = Vec2(w/2, 0)
		self._size = Vec2(20,20)
	
	def draw(self, screen):
		ast = pygame.Rect(self.pos.x, self.pos.y, self._size.x, self._size.y)
		pygame.draw.rect(screen, (0, 0, 255), ast) 
	
	def move(self):
		a = 1