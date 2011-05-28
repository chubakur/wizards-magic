#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import pygame
import sys
import globals
from pygame.locals import *

class MenuButton(pygame.sprite.Sprite):
	''' menu item '''
	def __init__(self,pos=0,text="",cmd="", enabled=True):
		pygame.sprite.Sprite.__init__(self)
		self.type = 'button'
		self.color = (255,255,255)
		self.font = pygame.font.Font("misc/Domestic_Manners.ttf", 20)
		self.text=text
		self.pos=pos  #position of item inside menu
		self.cmd=cmd
		self.enabled=enabled

		self.image_normal = self.font.render(self.text,True,self.color)
		self.image_pressed = self.font.render(self.text,True,(176,154,133))
		self.image_disabled = self.font.render(self.text,True,(95,245,244))
		if self.enabled:
			self.image = self.image_normal.copy()
		else:
			self.image = self.image_disabled.copy()
		self.rect=self.image.get_rect()
		self.surface_backup = self.image.copy()
		globals.menu_group.add(self)
	def draw(self):
		self.image = self.surface_backup.copy()
		bgrect=globals.background.get_rect()
		self.rect.centerx = bgrect.centerx
		menupos = globals.menu_bg.get_rect()
		menupos.centery = globals.background.get_rect().centery
		self.rect.top=menupos.top+25+(self.rect.height+5)*self.pos
		globals.background.blit(self.image, self.rect)
	def update(self):
		self.draw()
	def onmouse(self):
		if self.enabled:
			self.image = self.image_pressed
			self.surface_backup = self.image.copy()
	def onmouseout(self):
		if self.enabled:
			self.image = self.image_normal
			self.surface_backup = self.image.copy()
	def onmousedown(self):
		if self.enabled:
			exec(self.cmd)
			self.image = self.image_pressed
			self.surface_backup = self.image.copy()
	def onmouseup(self):
		pass
	def default(self):
		self.image = self.image_normal
		self.surface_backup = self.image.copy()
		
def clean_question():
	globals.question=False
	globals.answer=""
	globals.answer_cmd=""
	globals.gameinformationpanel.show=False
		
def menu_esc_question():
	globals.gameinformationpanel.display("  You are leaving the game. Are you sure? (Y/N)", persistent=True)
	globals.question=True
	globals.answer=""
	globals.answer_cmd="menu.menu_esc()"
	globals.answer_maxchar=1

def menu_esc():
	''' function called after the user press ESC key and answer question '''
	if globals.answer.upper()=='Y':
		if globals.stage==0: 
			sys.exit(0)
		elif globals.stage<=2:
			globals.stage=0
	clean_question()

def menu_startgame():
	''' function called after the user click start menu item'''
	globals.stage=1
	globals.gameinformationpanel.show=False

def menu_main(): 
	''' display Main manu '''

	#http://www.feebleminds-gifs.com/wizard-flames.jpg
	globals.background = pygame.image.load('misc/wizard-flames.jpg').convert_alpha()
	globals.menu_bg = pygame.image.load('misc/menu_bg.gif').convert_alpha()
	menupos = globals.menu_bg.get_rect()
	menupos.centerx = globals.background.get_rect().centerx
	menupos.centery = globals.background.get_rect().centery
	globals.background.blit(globals.menu_bg, menupos)

	menu1 = MenuButton(0,"Start Game","menu_startgame()")
	menu2 = MenuButton(1,"Start Server","",enabled=False)
	menu3 = MenuButton(2,"Connect to Server","",enabled=False)
	menu4 = MenuButton(3,"Options","",enabled=False)
	menu5 = MenuButton(5,"Quit","menu_esc_question()")

	globals.menu_group.update()

def main():

	pygame.init()
	globals.screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Wizards Magic')
	globals.background = pygame.Surface(globals.screen.get_size())
	globals.background = globals.background.convert()
	globals.background.fill((250, 250, 250))

	menu1= MenuButton((100,100),"Menu de prueba","p()")
	menu1.draw()
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (100, 100, 100))
	textpos = text.get_rect()
	textpos.centerx = globals.background.get_rect().centerx
	globals.background.blit(text, textpos)
	globals.screen.blit(globals.background, (0, 0))
	pygame.display.flip()

	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

			print event
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					print "qqqqqqqqqqqqqqqqqq"
				else:
					print event.key
					print pygame.key.name(event.key)
		pygame.display.flip()

if __name__ == '__main__': main()
