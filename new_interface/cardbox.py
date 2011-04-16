# -*- coding: utf-8 -*-
import pygame
import globals
class Cardbox(pygame.sprite.Sprite):
    def __init__(self, rect, player, position):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'cardbox'
        self.position = position
        self.player = player #первый или второй
        self.image = pygame.image.load('misc/cardbox_bg.gif').convert_alpha()
        self.light_image = pygame.image.load('misc/cardbox-activated.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        self.card = self.player
        self.light = False
        globals.panels.add(self)
    def get_opposite_cardbox(self):
        if self.position < 5:
            opposite_position = self.position + 5 #Id - блока, куда атаковать
        else:
            opposite_position = self.position-5
        return globals.cardboxes[opposite_position]
    def draw(self):
        #self.image = self.surface_backup.copy()
        if self.light:
            self.image.blit(self.light_image,(0,0))
            globals.background.blit(self.image, self.rect)
            self.image = self.surface_backup.copy()
            return
        globals.background.blit(self.image, self.rect)
    def update(self):
        self.draw()