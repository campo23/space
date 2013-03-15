import pygame
from pygame.locals import *
from Ship import Ship

def run():
	pygame.init()   
	start = 1
	h = 1024
	w = 600
	screen = pygame.display.set_mode((h, w))
	ship = Ship(screen, h, w)
	while start:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		screen.fill((0, 0, 0))
		key = pygame.key.get_pressed()
		ship.move(key, h)
		ship.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
    exit(run())