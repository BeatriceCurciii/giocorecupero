import pygame,sys
from pygame.locals import*
from sfondo import Platform
from bottone import Button
from oggetti import Object1
from oggetti import Object2
from oggetti import Object3

import random

pygame.init()
#creo schermo
window_size=(800,600)
screen=pygame.display.set_mode(window_size,0,32)
display=pygame.Surface((800,600))
pygame.display.set_caption('FRUIT NINJA')
clock=pygame.time.Clock()
fps=60

#aggiungo musica

#creo scritte
font=pygame.font.SysFont('Arial 93',70)
font_score=pygame.font.SysFont('Arial 93',70)

def draw_text(text,font,text_col,x,y):
	img=font.render(text,True,text_col)
	screen.blit(img,(x,y))
white=(255,255,255)
#scarico immagini x bottoni
start_img=pygame.image.load('image/start.png')
start_img=pygame.transform.scale(start_img,(200,200))

quit_img=pygame.image.load('image/quit.png')
quit_img=pygame.transform.scale(quit_img,(200,200))

play_img=pygame.image.load('image/play.png')
play_img=pygame.transform.scale(play_img,(200,200))

pause_img=pygame.image.load('image/pause.png')
pause_img=pygame.transform.scale(pause_img,(200,200))

gameover_img=pygame.image.load('image/gameover.png')
gameover_img=pygame.transform.scale(gameover_img,(600,300))


#creo bottoni
bottonestart=Button(display,160,200,start_img,200,200)
bottonequit=Button(display,480,200,quit_img,200,200)
bottoneplay=Button(display,100,480,play_img,200,200)
bottonepause=Button(display,500,480,pause_img,200,200)
bottonegameover=Button(display,0,400,gameover_img,600,300)


#creo sfondo
sfondo=Platform(display)

#carico oggetti che cadono
fnomi=['fragola','ciliegie','limone','mela','banana','arancia','bomba']
frutta1=Object1(display,sfondo,f'image/{random.choice(fnomi)}.png')
frutta2=Object2(display,sfondo,f'image/{random.choice(fnomi)}.png')
frutta3=Object3(display,sfondo,f'image/{random.choice(fnomi)}.png')
while frutta1.img=='image/bomba.png' and frutta2.img=='image/bomba.png' and frutta3.img=='image/bomba.png':
    frutta1=Object1(display,sfondo,f'image/{random.choice(fnomi)}.png')
    frutta2=Object2(display,sfondo,f'image/{random.choice(fnomi)}.png')
    frutta3=Object3(display,sfondo,f'image/{random.choice(fnomi)}.png')

menu=False
game=True
run=True
while run:
    clock.tick(60)
    
    #schermata principale
    if game==True:
        bottonestart=Button(display,160,200,start_img,200,200)
        bottonequit=Button(display,480,200,quit_img,200,200)
        display.fill((202,228,241))
        if bottonestart.drawbutton():
            game=False
        if bottonequit.drawbutton():
            run=False
    
    
    #avvio del gioco
    if game==False:
        
        #disegno sfondo
        sfondo=Platform(display)
        sfondo.drawsfondo()
        bottonequit=Button(display,0,480,quit_img,200,200)
        
        #creo oggetti che cadono
        
        while frutta1.moveobj() or frutta1.go==True:
            frutta1=Object1(display,sfondo,f'image/{random.choice(fnomi)}.png')
            frutta1.moveobj()
        if frutta1.moveobj()==False and frutta1.bomba==True:
            if bottonegameover.drawbutton():
                run=False
            
            
           

        while frutta2.moveobj() or frutta2.go==True :
            frutta2=Object2(display,sfondo,f'image/{random.choice(fnomi)}.png')
            frutta2.moveobj()
            
        if frutta2.moveobj()==False and frutta2.bomba==True:
            if bottonegameover.drawbutton():
                run=False
            
            
        while frutta3.moveobj() or frutta3.go==True:
            frutta3=Object3(display,sfondo,f'image/{random.choice(fnomi)}.png')
            frutta3.moveobj()  
        if frutta3.moveobj()==False and frutta3.bomba==True:
            if bottonegameover.drawbutton():
                run=False
                
             
        frutta1.drawobj()
        frutta2.drawobj()
        frutta3.drawobj()
        #controllo quando gli oggetti escono tutti dallo schermo
        if frutta1.rect.y>600 and frutta2.rect.x>800 and frutta3.rect.x<-100:
            if bottonegameover.drawbutton():
                run=False
                
                
            
        #disegno pulsanti pause
        if bottonepause.drawbutton():
            sfondo=Platform(display)

            #carico oggetti che cadono
            fnomi=['fragola','ciliegie','limone','mela','banana','arancia','bomba']
            frutta1=Object1(display,sfondo,f'image/{random.choice(fnomi)}.png')
            frutta2=Object2(display,sfondo,f'image/{random.choice(fnomi)}.png')
            frutta3=Object3(display,sfondo,f'image/{random.choice(fnomi)}.png')
            game=True
        if bottonequit.drawbutton():
            run=False  

    

            
        

   
       
        

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
       

            
        
    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    pygame.display.flip()
    