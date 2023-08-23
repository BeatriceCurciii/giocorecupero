import pygame
from pygame.locals import*

class Button():
	def __init__(self,display, x, y, img):
		self.img = img
		self.display = display
		self.rect = self.img.get_rect()
		self.rect.x = x
		self.rect.y = y
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