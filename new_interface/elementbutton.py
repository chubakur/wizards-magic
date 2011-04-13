# -*- coding: utf-8 -*-
import pygame
import globals
class ElementButton(pygame.sprite.Sprite):
    def __init__(self):
        #Это прототип!
        pass
    def draw(self):
        self.image = self.surface_backup.copy()
        #exec("text = globals.font.render(str(globals.player" + str(self.player.id) + "." + self.element + "_mana),True,(255,255,255))")
        exec("text = globals.font.render(str(self.player" + "." + self.element + "_mana),True,(255,255,255))")
        self.image.blit(text, (2, 9))
        globals.background.blit(self.image, self.rect)
    def update(self):
        self.draw()
class WaterElementButton(ElementButton):
    def __init__(self, rect, id):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'elementbutton'
        self.element = 'water'
        self.player = id
        self.image = pygame.image.load('misc/elements_water.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)
class FireElementButton(ElementButton):
    def __init__(self, rect, id):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'elementbutton'
        self.element = 'fire'
        self.player = id
        self.image = pygame.image.load('misc/elements_fire.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)
class AirElementButton(ElementButton):
    def __init__(self, rect, id):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'elementbutton'
        self.element = 'air'
        self.player = id
        self.image = pygame.image.load('misc/elements_air.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)
class EarthElementButton(ElementButton):
    def __init__(self, rect, id):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'elementbutton'
        self.element = 'earth'
        self.player = id
        self.image = pygame.image.load('misc/elements_earth.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)
class LifeElementButton(ElementButton):
    def __init__(self, rect, id):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'elementbutton'
        self.element = 'life'
        self.player = id
        self.image = pygame.image.load('misc/elements_life.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)
class DeathElementButton(ElementButton):
    def __init__(self, rect, id):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'elementbutton'
        self.element = 'death'
        self.player = id
        self.image = pygame.image.load('misc/elements_death.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)