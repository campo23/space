import pygame
from pygame.locals import *

class Ship:
	def __init__(self, screen, h, w):
		self.width = 50
		self.height = 50
		self.x = h/2
		self.y = w-50		
		self.shipR = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), self.shipR)

	def move(self, key, h):
		if(key[pygame.K_d] and self.x<h-50):
			self.x +=2
		elif(key[pygame.K_a] and self.x>0):
			self.x -=2
		self.shipR = pygame.Rect(self.x, self.y, self.width, self.height)