import pygame
from pygame.locals import*
import random

class Object():
    def __init__(self,display,sfondo,img):
        self.display=display
        self.sfondo = sfondo
        self.pos=[random.randint(0,600),0]
        self.size = sfondo.wtile/2, sfondo.htile/2
        self.image=pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
        self.gravita=0.3
        self.vel_caduta=2
        self.falling=False

    def moveobj(self):
        self.vel_caduta += self.gravita
        self.rect.bottom += self.vel_caduta
        self.falling = True

       
        
    def drawobj(self):
        self.display.blit(self.image,self.rect)
