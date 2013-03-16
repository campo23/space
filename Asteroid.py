import pygame
from pygame.locals import *

class Asteroid:
	def __init__(self):
		self.pos = Vec2(w/2, 0)
		self._size = Vec2(20,20)