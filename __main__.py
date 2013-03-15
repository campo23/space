import pygame
from pygame.locals import *
from Ship import Ship

def run():
	pygame.init()   
	start = 1
	h = 800
	w = 600
	screen = pygame.display.set_mode((h, w))
	ship = Ship(screen, h, w)
	while start:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		print "2"
		screen.fill((0, 0, 0)) 
		print "hello"
		ship.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
    exit(run())