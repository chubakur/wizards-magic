# -*- coding: utf-8 -*-
import globals
import pygame
import player
import cards
import sys
from pygame.locals import *
class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('misc/point_alpha.gif').convert_alpha()
        self.rect = self.image.get_rect()
    def draw(self, rect):
        globals.background.blit(self.image, rect)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(rect)
class Event_handler():
    def __init__(self):
        pass
    def event(self, event):
        if event.type == QUIT:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                #global player
                globals.point.draw(event.pos)
                collided = pygame.sprite.spritecollide(globals.point, globals.cards_in_deck, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(globals.point, globals.interface, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(globals.point, globals.panels, 0)
                if not collided:
                    return
                item = collided[len(collided)-1]
                if item.type == "warrior_card": #Карта в колоде! Карта на поле в cardbox
                    exec('selected_card_0 = cards.' + item.name + '()') #Переменной selected_card_0 присваиваем новый объект
                    globals.selected_card = selected_card_0 # из локальной в глобальную
                    return
                if item.player.id != globals.player.id:
                    return
                if item.type == "cardbox": #Если клик на карточный бокс
                    if item.card.name != "player": #Если в этом блоке есть карта
                        if item.card.cast: #если есть каст
                            if not item.card.used_cast: # если еще не кастовали
                                item.card.cast_action()
                    if globals.selected_card: #если выбрана карта
                        if not globals.player.action_points: #если уже ходил
                            return
                        exec('available_mana = globals.player.' + globals.selected_card.element + '_mana') # Вычисляем сколько маны у нас есть. Значение помещаем в локальную переменную available_mana
                        if available_mana < globals.selected_card.level:
                            return
                        item.card = globals.selected_card
                        item.card.parent = item
                        #item.card.cardboxes = cardboxes
                        #item.card.playerscards = playerscards
                        item.card.field = True
                        item.card.summon() #функция которая хранит описание действий при выводе карты
                        globals.player.action_points = False
                        exec('globals.player.' + globals.selected_card.element + '_mana -= ' + str(globals.selected_card.level)) #Отнимаем ману
                        globals.interface.remove(globals.cardsofelementshower1) #Закрываем окна выбора карты
                        globals.interface.remove(globals.cardsofelementshower2) #Закр. окна выбора карты
                        globals.cards_in_deck.empty() #очищаем группу карты в колоде
                        if item.player.id == 1:
                            globals.ccards_1.add(item.card)
                        else:
                            globals.ccards_2.add(item.card)
                        globals.selected_card = 0
                if item.type == 'elementbutton':
#                    global cards_of_element_shower_element
                    globals.cards_in_deck.empty()
                    if globals.player.id == 1:
                        globals.interface.add(globals.cardsofelementshower1)
                    else:
                        globals.interface.add(globals.cardsofelementshower2)
                    if item.element == 'water':
                        globals.cards_of_element_shower_element = "water"
                    elif item.element == 'fire':
                        globals.cards_of_element_shower_element = "fire"
                    elif item.element == 'air':
                        globals.cards_of_element_shower_element = "air"
                    elif item.element == 'earth':
                        globals.cards_of_element_shower_element = "earth"
                    elif item.element == 'life':
                        globals.cards_of_element_shower_element = "life"
                    elif item.element == 'death':
                        globals.cards_of_element_shower_element = "death"
                elif item.type == 'completethecoursebutton':
                    player.finish_turn()
            elif event.button == 3: #ПРАВАЯ КНОПКА МЫШИ
                globals.point.draw(event.pos)
                collided = pygame.sprite.spritecollide(globals.point, globals.cards_in_deck, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(globals.point, globals.interface, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(globals.point, globals.panels, 0)
                if not collided:
                    return
                item = collided[len(collided)-1]
                if item.type == "warrior_card": #по боевой карте
                    globals.card_info_group.add(globals.cardinfo)
                    globals.cardinfo.text = item.info
                    globals.cardinfo.show = True
                if item.type == "cardbox":
                    if item.card.name != "player":
                        globals.card_info_group.add(globals.cardinfo)
                        globals.cardinfo.text = item.card.info
                        globals.cardinfo.show = True
                if item.type == 'cardsofelementshower':
                    globals.interface.remove(globals.cardsofelementshower1)
                    globals.interface.remove(globals.cardsofelementshower2)
                    globals.cards_in_deck.empty()
        elif event.type == MOUSEBUTTONUP: #отпускаем кнопку мыши
            if event.button == 3: #Правую
                if globals.cardinfo.show:
                    globals.cardinfo.show = False
                    globals.card_info_group.empty()