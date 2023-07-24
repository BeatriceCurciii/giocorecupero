import pygame,sys
from pygame.locals import*
from personaggio import Steve
from sfondo import Platform

pygame.init()

window_size=(800,600)
screen=pygame.display.set_mode(window_size,0,32)
display=pygame.Surface((800,600))
pygame.display.set_caption('catchall')
clock=pygame.time.Clock()
fps=60


sfondo=Platform(display)
steve=Steve(display,(100,100),sfondo)
while True:
   
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    sfondo.drawsfondo()
    steve.movesteve()
    steve.draw()
    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    pygame.display.flip()
    clock.tick(60)
