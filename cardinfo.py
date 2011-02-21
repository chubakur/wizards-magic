# -*- coding: utf-8 -*-
import pygame
import globals
class CardInfo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'cardinfo'
        self.image = pygame.Surface((450, 300))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
        self.surface_backup = self.image.copy()
        self.rect = (globals.screen.get_size()[0] / 2-self.image.get_size()[0] / 2, globals.screen.get_size()[1] / 2-self.image.get_size()[1] / 2)
        self.show = False
        self.text = ""
        self.symbol_size = 7 #Размер символа по Х. Нужно для расчета переноса строк
        self.distance_between_rows = 20 #расстояние между строками
        self.symbols_in_row = int(self.image.get_size()[0] / self.symbol_size)
    def draw(self):
        self.image = self.surface_backup.copy()
        rows = len(self.text) / self.symbols_in_row
        if len(self.text) % self.symbols_in_row:
            rows += 1
        for row in xrange(0, rows):
            text = globals.font.render(self.text[row * self.symbols_in_row:self.symbols_in_row + row * self.symbols_in_row]+"-", True, (255, 255, 255))
            self.image.blit(text, (0, self.distance_between_rows * row))
        globals.background.blit(self.image, self.rect)
    def update(self):
        self.draw()