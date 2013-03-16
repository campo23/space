import pygame
from pygame.locals import *
from Vec2 import Vec2
from AABBox import AABBox
from Asteroid import Asteroid


class NPCAsteroids:

	def __init__(self,w,h,size,subsize):
		#make grid
		self._windowBox=Vec2(w,h)
		self._boxsize=subsize
		offset=(size-subsize)/2
		nbox=Vec2(int(w/size.x),int(h/size.y))
		count=0
		self.asteroids=[]
		for y in range(0,nbox.y):
			count+=1
			self.asteroids.append([[count%2,y*size.y],[]])
			for x in range(0,nbox.x):
				self.asteroids[y][1].append(Asteroid(Vec2(x,y)*size+offset,subsize))

	def draw(self,screen):
		for line in self.asteroids:
			for ast in line[1]:
				ast.draw(screen)

	def collision(self,aabb):		
		for line in self.asteroids:
			for ast in line[1]:
				if ast.collision(aabb):
					return True
		return False

	def collisionLine(self,line,aabb):
		for ast in line[1]:
			if ast.collision(aabb):
				return True
		return False

	def setDirLineBox(self,line):
		firstbox=line[1][0]
		lastbox=line[1][len(line[1])-1]
		min_x=firstbox.pos.x
		max_x=lastbox.pos.x+self._boxsize.x
		if min_x<=0:
			line[0][0]=1
			line[0][1]+=self._boxsize.y
		elif max_x >= self._windowBox.x:			
			line[0][0]=0
			line[0][1]+=self._boxsize.y


	def move(self):
		countLine=0		
		for line in self.asteroids:
			for ast in line[1]:
				if line[0][0]==1 :
					ast.move(Vec2(ast.pos.x+.1,line[0][1]))
				else:
					ast.move(Vec2(ast.pos.x-.1,line[0][1]))
			self.setDirLineBox(line)

