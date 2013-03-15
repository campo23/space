import pygame
from pygame.locals import *
from Vec2 import Vec2
from AABBox import AABBox

class Ship:
	def __init__(self, screen, w, h):
		self.size    = Vec2(50,50)
		self.pos     = Vec2(w/2,h-50)
		self.center  =Vec2(self.size.x/2,self.size.y/2)
		self.box     = AABBox(self.pos+self.center,self.center)
		self.shipR   = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

	def getAABBox():
		return self.box
		
	def collision(self,aabb):
		return self.box.itersectionQuad(aabb)
	
	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), self.shipR)

	def move(self, key, h):
		if(key[pygame.K_d] and self.pos.x<h-50):
			self.pos.x +=2
		elif(key[pygame.K_a] and self.pos.x>0):
			self.pos.x -=2
		self.box=self.pos+self.center
		self.shipR.top=self.pos.y
		self.shipR.left=self.pos.x
		