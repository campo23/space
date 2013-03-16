import pygame
from pygame.locals import *
from Vec2 import Vec2
from AABBox import AABBox

class Bullet:
	def __init__(self, w):				
		self.pos     = Vec2(0, 0)
		self._size   = Vec2(10, 10)
		self._vel    = -3
		self._center = self._size/2
		self._box    = AABBox(self.pos+self._center,self._center)
		self._bullR  = pygame.Rect(self.pos.x, self.pos.y, self._size.x, self._size.y)
	
	def box(self):
		return self._box
	
	def collision(self, aabb):
		return self._box.itersectionQuad(aabb)
		
	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 255), self._bullR) 
	
	def move(self):
		self._box.point=self.pos+self._center
		self._bullR.top=self.pos.y
		self._bullR.left=self.pos.x
		self.pos.y += self._vel