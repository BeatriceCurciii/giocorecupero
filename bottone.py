import pygame
from pygame.locals import*

class Button():
	def __init__(self,display, posx,posy,img,x,y):
		self.img = img
		self.posx=posx
		self.posy=posy
		self.x=x
		self.y=y
		self.display = display
		self.rect = pygame.Rect(self.posx,self.posy,self.x,self.y)
		
		
		self.clicked = False

	def drawbutton(self):
		go = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				go= True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		self.display.blit(self.img, self.rect)
		return go