import pygame
from pygame.locals import *
from Vec2 import Vec2
from AABBox import AABBox

class Ship:
	def __init__(self, screen, h, w):
		self.size = Vec2(50,50)
		self.pos  = Vec2(h/2,w-50)
		self.shipR = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

	def collision(self,aabb):
		return AABBox(self.pos,self.size).itersectionQuad(aabb)
	
	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), self.shipR)

	def move(self, key, h):
		if(key[pygame.K_d] and self.pos.x<h-50):
			self.pos.x +=2
		elif(key[pygame.K_a] and self.pos.x>0):
			self.pos.x -=2
		self.shipR.top=self.pos.y
		self.shipR.left=self.pos.x
		