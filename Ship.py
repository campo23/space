import pygame
from pygame.locals import *

class Ship:
	def __init__(self, screen, h, w):
		self.width = 50
		self.height = 50
		self.ship = pygame.Rect(w/2, h-50, self.width, self.height)

	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), self.ship)