import pygame
from pygame.locals import*
class Button():
    def __init__(self,display,x,y,img):
        self.img=img
        self.rect=self.img.get_rect()
        self.x=x
        self.y=y
        self.display=display
        self.clicked=False
    def drawbutton(self):
        
        go=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                go=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        self.display.blit(self.img,(self.x,self.y))
        return go