# -*- coding: utf-8 -*-
import pygame.sprite
# To change this template, choose Tools | Templates
# and open the template in the editor.
import pygame
import sys
from pygame.locals import *
import pgcontrols
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
#pgcontrols_gr = pygame.sprite.Group()
#pgcontrols.init(pg_controls_gr)
pygame.display.set_caption('test')
def btn1_action():
    print 'bye'
    sys.exit(0)
class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('misc/point_alpha.gif').convert_alpha()
        self.rect = pygame.Rect
    def draw(self,rect):
        background.blit(self.image, rect)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(rect)
point = Point()
btn1 = pgcontrols.Button(background,(0,0),btn1_action,'QUIT')
def btn2_action():
    if btn1.shown:
        btn1.hide()
    else:
        btn1.show()
btn2 = pgcontrols.Button(background,(100,0),btn2_action,'SQ')
a = 0
def switch_language():
    global a
    if not a:
        btn1.change_label('EXIT')
        btn2.change_label('PSV')
        btn3.change_label('US')
        a = 1
    else:
        btn1.change_label('QUIT')
        btn2.change_label('SQ')
        btn3.change_label('RU')
        a = 0
btn3 = pgcontrols.Button(background,(200,0),switch_language,'RU')
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == MOUSEBUTTONDOWN:
            point.draw(event.pos)
            collided = pygame.sprite.spritecollide(point, pgcontrols.group, 0)
            if collided:
                item = collided[-1]
                if item.type == "button":
                    item.press()
        elif event.type == MOUSEBUTTONUP:
            point.draw(event.pos)
            collided = pygame.sprite.spritecollide(point, pgcontrols.group, 0)
            if collided:
                item = collided[-1]
                if item.type == "button":
                    item.pull()
        pgcontrols.group.update()
        screen.blit(background,(0,0))
        background.fill((0,0,0))
        pygame.display.flip()
