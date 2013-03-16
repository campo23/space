import pygame
import random
from pygame.locals import *
from Vec2 import Vec2
from AABBox import AABBox

class Asteroid:
	random.seed()
	def __init__(self, pos,size):				
		self.pos     = pos
		self._size   = size
		self._center = self._size/2
		self._box    = AABBox(self.pos+self._center,self._center)
		self._astR   = pygame.Rect(self.pos.x, self.pos.y, self._size.x, self._size.y)
	
	def box(self):
		return self._box
	
	def collision(self,aabb):
		return self._box.itersectionQuad(aabb)
		
	def draw(self, screen):
		pygame.draw.rect(screen, (0, 0, 255), self._astR) 
	
	def move(self,pos):
		self.pos=pos
		self._box.point=self.pos+self._center
		self._astR.top=self.pos.y
		self._astR.left=self.pos.x
