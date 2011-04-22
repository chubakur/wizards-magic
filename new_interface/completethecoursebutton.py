# -*- coding: utf-8 -*-
import pygame
import globals
import player
class CompleteTheCourseButton(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        #self.panel = panel
        self.type = 'button'
        self.image = pygame.image.load('misc/complete_the_course.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect #.move(self.panel.rect[0], self.panel.rect[1])
        globals.interface.add(self)
    def onmouse(self):
        pass
    def onmouseout(self):
        pass
    def onmousedown(self):
        player.finish_turn()
    def onmouseup(self):
        pass
    def draw(self):
        globals.background.blit(self.image, self.relative_rect)
    def update(self):
        self.draw()