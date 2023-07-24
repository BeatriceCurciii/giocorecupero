import pygame
from pygame.locals import*
from sfondo import Platform

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

class Steve:
    def __init__(self,display,pos,sfondo)->None:
        self.display=display
        self.sfondo = sfondo
        self.size = sfondo.wtile, sfondo.htile
        self.image=pygame.image.load('image/pokemon.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.vel=[0,0]
        self.gravita=0.3
        self.mr=False
        self.ml=False
        self.veloriz=5
        self.max_vel_caduta=5
        self.falling=False
    
    def movesteve(self):
        keys=pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.mr=True
        else:
            self.mr=False
        if keys[K_LEFT]:
            self.ml=True
        else:
            self.ml=False
        
    
        self.vel[1] += self.gravita
        self.rect.bottom += self.vel[1]
        self.falling = True

        if self.rect.bottom>self.display.get_height():
            self.rect.bottom=self.display.get_height()
            self.vel[1]=0
            self.falling=False

        if self.mr:
            self.rect.left+=self.veloriz
            if self.rect.left<0:
                self.rect.left=0 
        if self.ml:
            self.rect.left-=self.veloriz
            if self.rect.left<0:
                self.rect.left=0
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        hit_list = collision_test(self.rect, self.sfondo.griglia)
        for tile in hit_list:
            # muovo a destra
            if self.vel[0] > 0:
                self.rect.right = tile.left
                collision_types['right'] = True
            # muovo a sinistra
            if self.vel[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True

        # muovo in verticale
        self.vel[1] += self.gravita
        if self.vel[1] > self.max_vel_caduta:
            self.vel[1] = self.max_vel_caduta
        self.rect.y += self.vel[1]


        hit_list = collision_test(self.rect, self.sfondo.griglia)
        for tile in hit_list:
            # muovo in basso
            if self.vel[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            # muovo in alto
            if self.vel[1] < 0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
                self.vel[1] = 0

        # devo controllare anche se esco dallo schermo di lato (potrei inventare un modo con dei rect che formano il bordo)
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > self.display.get_width():
            self.rect.right = self.display.get_width()

        

    def draw(self):
        self.display.blit(self.image,self.rect)
