import pygame
from pygame.locals import *
from Vec2 import Vec2
from Ship import Ship
from Asteroid import Asteroid
from NPCAsteroids import NPCAsteroids

def run():
	pygame.init()   
	start = 1
	w = 1024
	h = 600
	screen = pygame.display.set_mode((w, h))
	ship = Ship(screen, w, h)
	npc=NPCAsteroids(w,h/2,Vec2(64,64),Vec2(32,32))
    
	while start:
		pygame.time.wait(5)
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		screen.fill((0, 0, 0))
		key = pygame.key.get_pressed()
		#update logic
		ship.move(key, w)
		npc.move()
		#update graphics
		ship.draw(screen)
		npc.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
    exit(run())
