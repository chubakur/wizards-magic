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
        if globals.player_id == globals.player.id:
            player.finish_turn()
        else:
            return
    def onmouseup(self):
        pass
    def draw(self):
        if globals.player.id != globals.player_id:
            return
        globals.background.blit(self.image, self.relative_rect)
    def update(self):
        self.draw()