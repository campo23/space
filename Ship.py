import pygame
from pygame.locals import *
from Vec2 import Vec2
from AABBox import AABBox

class Ship:
	def __init__(self, screen, w, h):
		self.pos      = Vec2(w/2,h-50)
		self._size    = Vec2(50,50)
		self._center  = self._size/2
		self._box     = AABBox(self.pos+self._center,self._center)
		self._shipR   = pygame.Rect(self.pos.x, self.pos.y, self._size.x, self._size.y)

	def box(self):
		return self._box
		
	def collision(self,aabb):
		return self._box.itersectionQuad(aabb)
	
	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), self._shipR)

	def move(self, key, h):
		if(key[pygame.K_d] and self.pos.x<h-50):
			self.pos.x +=2
		elif(key[pygame.K_a] and self.pos.x>0):
			self.pos.x -=2
		self._box.point=self.pos+self._center
		self._shipR.top=self.pos.y
		self._shipR.left=self.pos.x
		