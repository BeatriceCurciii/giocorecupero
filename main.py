import pygame,sys
from pygame.locals import*
pygame.init()

window_size=(800,600)
screen=pygame.display.set_mode(window_size)
pygame.display.set_caption('catchall')
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100,100,100))
    

    pygame.display.flip()
    clock.tick(60)
