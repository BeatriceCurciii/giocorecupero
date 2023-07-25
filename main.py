import pygame,sys
from pygame.locals import*
from personaggio import Steve
from sfondo import Platform
from bottone import Button

pygame.init()
#creo schermo
window_size=(800,600)
screen=pygame.display.set_mode(window_size,0,32)
display=pygame.Surface((800,600))
pygame.display.set_caption('catchall')
clock=pygame.time.Clock()
fps=60

#aggiungo musica

#creo scritte

#scarico immagini x bottoni
start_img=pygame.image.load('image/start.png')
start_img=pygame.transform.scale(start_img,(80,60))
exit_img=pygame.image.load('image/exit.png')
exit_img=pygame.transform.scale(exit_img,(80,60))

#creo bottoni
bottonestart=Button(display,160,200,start_img)
bottoneexit=Button(display,480,200,exit_img)

#creo personaggio e sfondo
sfondo=Platform(display)
steve=Steve(display,(100,100),sfondo)
game=True
run=True
while run:
    clock.tick(60)
    display.fill((202,228,241))

    if game:
        
        if bottonestart.drawbutton():
            print('ok')
        if bottoneexit.drawbutton():
            run=False
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    
    else:
        #disegno sfondo
        sfondo.drawsfondo()

        #faccio muovere il personaggio
        steve.movesteve()
        steve.draw()

    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    pygame.display.flip()
    