import pygame
from math import ceil
class Platform:
    def __init__(self,display,nomefile='mappe/mappa.txt')->None:
        self.display=display
        self.background=pygame.image.load('image/background.png')
        self.cubo=pygame.image.load('image/cubo.png')
        with open(nomefile)as f:
            self.mappa=[list(map(int,riga.strip().split()))for riga in f]
        self.num_rig=len(self.mappa)
        self.num_col=len(self.mappa[0])
        self.wtile=ceil(display.get_width()/self.num_col)
        self.htile=ceil(display.get_height()/self.num_rig)
        self.background=pygame.transform.scale(self.background,(800,600))
        self.cubo=pygame.transform.scale(self.cubo,(self.wtile,self.htile))
        self.griglia=[]
        for y,r in enumerate(self.mappa):
            for x,cella in enumerate(r):
                if cella!=0:
                    self.griglia.append(pygame.Rect(x*self.wtile,y*self.htile,self.wtile,self.htile))
    def drawsfondo(self):
        self.display.fill((0,0,0))
        self.display.blit(self.background,(0,0))
        for y,r in enumerate(self.mappa):
            for x,cella in enumerate(r):
                if cella==1:
                    self.display.blit(self.cubo,(x*self.wtile,y*self.htile))