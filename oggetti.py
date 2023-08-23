import pygame
from pygame.locals import*
import random

class Object1():
    def __init__(self,display,sfondo,img,bomba=False):
        self.img=img
        self.bomba=bomba
        self.display=display
        self.sfondo = sfondo
        self.pos=[random.randint(0,600),-100]
        self.image=pygame.image.load(self.img)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pygame.Rect(self.pos[0],self.pos[1], 100, 100)
      
        self.vel_caduta=0.005
        self.falling=False

    def moveobj(self):
        self.vel_caduta +=0.007
        self.rect.y += self.vel_caduta
        
        pos = pygame.mouse.get_pos()
        action=True
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.img=='image/bomba.png':
                        action=False
                        self.bomba=True
                else:
                    action=True
                self.clicked = True
        else:
            if self.img=='image/bomba.png':
                action=True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
            
    def drawobj(self):
        self.display.blit(self.image,self.rect)



class Object2():
    def __init__(self,display,sfondo,img,bomba=False):
        self.img=img
        self.bomba=bomba
        self.display=display
        self.sfondo = sfondo
        self.pos=[-100,random.randint(0,400)]
        self.image=pygame.image.load(self.img)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pygame.Rect(self.pos[0],self.pos[1], 100, 100)
      
        self.vel_oriz=0.005
        self.falling=False

    def moveobj(self):
        self.vel_oriz +=0.005
        self.rect.x += self.vel_oriz
        
        pos = pygame.mouse.get_pos()
        
        action=True
        if self.rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.img=='image/bomba.png':
                    
                    
                    action=False
                    self.bomba=True
                else:
                    action=True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return action
            
            
    def drawobj(self):
        self.display.blit(self.image,self.rect)






class Object3():
    def __init__(self,display,sfondo,img,bomba=False):
        self.img=img
        self.bomba=bomba
        self.display=display
        self.sfondo = sfondo
        self.pos=[800,random.randint(0,400)]
        self.image=pygame.image.load(self.img)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pygame.Rect(self.pos[0],self.pos[1], 100, 100)
      
        self.vel_oriz=0.005
        self.falling=False

    def moveobj(self):
        self.vel_oriz +=0.005
        self.rect.x -= self.vel_oriz
        
        pos = pygame.mouse.get_pos()
        action=True
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.img=='image/bomba.png':
                    
                    action=False
                    self.bomba=True
                else:
                    action=True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
            
    
         
    def drawobj(self):
        self.display.blit(self.image,self.rect)



