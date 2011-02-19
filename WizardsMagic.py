# -*- coding: utf-8 -*-
import pygame.sprite
#Wizards Magic
#Copyright (C) 2011  сhubakur
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# To change this template, choose Tools | Templates
# and open the template in the editor.
#import pygame.sprite
#Внимание!! Для того, чтобы слои не наслаивались, я использую объект surface_backup , который является копией изображения. После этого они заменяются
__author__ = "chubakur"
__date__ = "$12.02.2011 12:11:42$"
import pygame
from pygame.locals import *
import sys
import cards
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Wizards Magic')
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
panels = pygame.sprite.Group() #Нижний уровень
interface = pygame.sprite.Group() #Уровень кнопок
cards_in_deck = pygame.sprite.Group() #Уровень дополнительный
ccards_1 = pygame.sprite.Group() #  Карты, которые вывел первый игрок
ccards_2 = pygame.sprite.Group() # Карты, которые вывел второй игрок
cards_of_element_shower_element = "" #какой элемент показывать
selected_card = False #Выбранная карта
card_info_group = pygame.sprite.Group() #  Группа, которая содержит спрайт, содержащий панель вывода информации о карте
font = pygame.font.Font(None, 20)
font.set_bold(0)
#class GameParams():
    #def __init__(self):
        # self.player.id = 1
#game_params = GameParams()
class Player(): #Прототип игрока
    def __init__(self):
        self.health = 50
        self.name = "player"
        self.action_points = True #Ходил игрок, или нет
        self.get_cards()
        self.get_mana()
    def damage(self, damage, enemy):
        self.health -= damage
        if self.health <= 0:
            print "Game Over"
    def recovery(self, health):
        self.health += health
    def get_mana(self):
        self.water_mana = random.randint(1, 6)
        self.fire_mana = random.randint(1, 6)
        self.air_mana = random.randint(1, 6)
        self.earth_mana = random.randint(1, 6)
        self.life_mana = random.randint(1, 6)
        self.death_mana = random.randint(1, 6)
    def get_cards(self):
        self.water_cards = []
        self.fire_cards = []
        self.air_cards = []
        self.earth_cards = []
        self.life_cards = []
        self.death_cards = []
        for i in xrange(0, 4):
            #получаем карту элемента воды
            randnum = random.randint(0, len(cards.water_cards)-1)
            self.water_cards.append(cards.water_cards[randnum])
            exec("self." + cards.water_cards[randnum].lower() + "=cards." + cards.water_cards[randnum] + "()")
            cards.water_cards.remove(cards.water_cards[randnum])
            #Элемент огня
            randnum = random.randint(0, len(cards.fire_cards)-1)
            self.fire_cards.append(cards.fire_cards[randnum])
            exec("self." + cards.fire_cards[randnum].lower() + "=cards." + cards.fire_cards[randnum] + "()")
            cards.fire_cards.remove(cards.fire_cards[randnum])
            #Элемент воздуха
            randnum = random.randint(0, len(cards.air_cards)-1)
            self.air_cards.append(cards.air_cards[randnum])
            exec("self." + cards.air_cards[randnum].lower() + "=cards." + cards.air_cards[randnum] + "()")
            cards.air_cards.remove(cards.air_cards[randnum])
            #Элемент земли
            randnum = random.randint(0, len(cards.earth_cards)-1)
            self.earth_cards.append(cards.earth_cards[randnum])
            exec("self." + cards.earth_cards[randnum].lower() + "=cards." + cards.earth_cards[randnum] + "()")
            cards.earth_cards.remove(cards.earth_cards[randnum])
            #Элемент жизни
            randnum = random.randint(0, len(cards.life_cards)-1)
            self.life_cards.append(cards.life_cards[randnum])
            exec("self." + cards.life_cards[randnum].lower() + "=cards." + cards.life_cards[randnum] + "()")
            cards.life_cards.remove(cards.life_cards[randnum])
            #Элемент смерти
            randnum = random.randint(0, len(cards.death_cards)-1)
            self.death_cards.append(cards.death_cards[randnum])
            exec("self." + cards.death_cards[randnum].lower() + "=cards." + cards.death_cards[randnum] + "()")
            cards.death_cards.remove(cards.death_cards[randnum])
class Player1(Player):
    def __init__(self):
        self.id = 1
        Player.__init__(self)
class Player2(Player):
    def __init__(self):
        self.id = 2
        Player.__init__(self)
player1 = Player1()
player2 = Player2()
player = player1
def finish_turn():
    global player
    #Меняем игрока
    if player.id == 1:
        player = player2
        player.action_points = True
        for card in ccards_1: #Атакуем
            card.attack()
            #card.used_cast = False # Даем возможность кастовать
            #card.moves_alive+=1
        for card in ccards_2:
            #
            card.turn()
    else:
        player = player1
        player.action_points = True
        for card in ccards_2: #Атакуем
            card.attack()
            card.used_cast = False
        for card in ccards_1:
            card.turn()
    #Добавляем ману
    player.water_mana += 1
    player.fire_mana += 1
    player.air_mana += 1
    player.earth_mana += 1
    player.life_mana += 1
    player.death_mana += 1
class CardInfo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'cardinfo'
        self.image = pygame.Surface((450, 300))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
        self.surface_backup = self.image.copy()
        self.rect = (screen.get_size()[0] / 2-self.image.get_size()[0] / 2, screen.get_size()[1] / 2-self.image.get_size()[1] / 2)
        self.show = False
        self.text = ""
        self.symbol_size = 8 #Размер символа по Х. Нужно для расчета переноса строк
        self.distance_between_rows = 20 #расстояние между строками
        self.symbols_in_row = int(self.image.get_size()[0] / self.symbol_size)
    def draw(self):
        self.image = self.surface_backup.copy()
        rows = len(self.text) / self.symbols_in_row
        if len(self.text) % self.symbols_in_row:
            rows += 1
        for row in xrange(0, rows):
            text = font.render(self.text[row * self.symbols_in_row:self.symbols_in_row + row * self.symbols_in_row], True, (255, 255, 255))
            self.image.blit(text, (0, self.distance_between_rows * row))
        background.blit(self.image, self.rect)
    def update(self):
        self.draw()
class CardsOfElementShower(pygame.sprite.Sprite):
    #Не прототип!
    def __init__(self, rect, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.type = 'cardsofelementshower'
        self.image = pygame.image.load('misc/cards_box.gif').convert_alpha()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        self.cards = 0
        self.shift = 32
    def draw(self):
        background.blit(self.image, self.rect)
    def update(self):
        if self.player.id != player.id:
            return
        self.cards = 0
        if self.player.id == 1:
            if cards_of_element_shower_element == "water":
                for card in player1.water_cards:
                    exec("cards_in_deck.add(player1." + card.lower() + ")")
            elif cards_of_element_shower_element == "fire":
                for card in player1.fire_cards:
                    exec("cards_in_deck.add(player1." + card.lower() + ")")
            elif cards_of_element_shower_element == "air":
                for card in player1.air_cards:
                    exec("cards_in_deck.add(player1." + card.lower() + ")")
            elif cards_of_element_shower_element == "earth":
                for card in player1.earth_cards:
                    exec("cards_in_deck.add(player1." + card.lower() + ")")
            elif cards_of_element_shower_element == "life":
                for card in player1.life_cards:
                    exec("cards_in_deck.add(player1." + card.lower() + ")")
            else:
                for card in player1.death_cards:
                    exec("cards_in_deck.add(player1." + card.lower() + ")")
        else:
            if cards_of_element_shower_element == "water":
                for card in player2.water_cards:
                    exec("cards_in_deck.add(player2." + card.lower() + ")")
            elif cards_of_element_shower_element == "fire":
                for card in player2.fire_cards:
                    exec("cards_in_deck.add(player2." + card.lower() + ")")
            elif cards_of_element_shower_element == "air":
                for card in player2.air_cards:
                    exec("cards_in_deck.add(player2." + card.lower() + ")")
            elif cards_of_element_shower_element == "earth":
                for card in player2.earth_cards:
                    exec("cards_in_deck.add(player2." + card.lower() + ")")
            elif cards_of_element_shower_element == "life":
                for card in player2.life_cards:
                    exec("cards_in_deck.add(player2." + card.lower() + ")")
            else:
                for card in player2.death_cards:
                    exec("cards_in_deck.add(player2." + card.lower() + ")")
        self.draw()
class CompleteTheCourseButton(pygame.sprite.Sprite):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'completethecoursebutton'
        self.player = panel.player
        self.image = pygame.image.load('misc/complete_the_course.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
    def draw(self):
        if not self.player.id == player.id:
            return
        self.panel.image.blit(self.image, self.relative_rect)
    def update(self):
        self.draw()
class ElementButton(pygame.sprite.Sprite):
    def __init__(self):
        #Это прототип!
        pass
    def draw(self):
        self.image = self.surface_backup.copy()
        exec("text = font.render(str(player" + str(self.player.id) + "." + self.element + "_mana),True,(255,255,255))")
        self.image.blit(text, (5, 16))
        self.panel.image.blit(self.image, self.relative_rect)
    def update(self):
        self.draw()
class WaterElementButton(ElementButton):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'water'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_water.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
class FireElementButton(ElementButton):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'fire'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_fire.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
class AirElementButton(ElementButton):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'air'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_air.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
class EarthElementButton(ElementButton):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'earth'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_earth.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
class LifeElementButton(ElementButton):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'life'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_life.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
class DeathElementButton(ElementButton):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'death'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_death.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
class HealthWindow(pygame.sprite.Sprite):
    def __init__(self, rect, panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'healthwindow'
        self.player = panel.player
        self.image = pygame.image.load('misc/health_window.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.relative_rect = self.image.get_rect().move((rect[0], rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0], self.panel.rect[1])
        interface.add(self)
        self.font = pygame.font.Font(None, 22)
    def draw(self):
        self.image = self.surface_backup.copy()
        if self.player.id == 1:
            text = self.font.render(str(player1.health), True, (255, 255, 255))
        else:
            text = self.font.render(str(player2.health), True, (255, 255, 255))
        self.image.blit(text, (25, 5))
        self.panel.image.blit(self.image, self.relative_rect)
    def update(self):
        self.draw()
class Cardbox(pygame.sprite.Sprite):
    def __init__(self, rect, player, position):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'cardbox'
        self.position = position
        self.player = player #первый или второй
        self.image = pygame.image.load('misc/cardbox_bg.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        self.card = self.player
        panels.add(self)
    def draw(self):
        #self.image = self.surface_backup.copy()
        background.blit(self.image, self.rect)
    def update(self):
        self.draw()
class Infopanel(pygame.sprite.Sprite):
    def __init__(self, rect, player):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'infopanel'
        self.player = player
        #self.image = pygame.Surface((screen.get_size()[0],screen.get_size()[1]/25))
        self.image = pygame.image.load('misc/infopanel_bg.gif').convert_alpha()
        #self.image.convert()
        #self.image.fill((0,0,255))
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        panels.add(self)
    def draw(self):
        background.blit(self.image, self.rect)
    def update(self):
        self.draw()
class Actionpanel(pygame.sprite.Sprite):
    def __init__(self, rect, player):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'actionpanel'
        self.player = player
        self.image = pygame.image.load('misc/actionpanel_bg.gif').convert_alpha()
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        panels.add(self)
    def draw(self):
        background.blit(self.image, self.rect)
        self.image = self.surface_backup.copy()
    def update(self):
        self.draw()
class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('misc/point_alpha.gif').convert_alpha()
        self.rect = self.image.get_rect()
    def draw(self, rect):
        background.blit(self.image, rect)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(rect)
point = Point()
cardinfo = CardInfo()
###############################################################################################################
#ACTIONS
class Event_handler():
    def __init__(self):
        pass
    def event(self, event):
        if event.type == QUIT:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                global player, selected_card
                point.draw(event.pos)
                collided = pygame.sprite.spritecollide(point, cards_in_deck, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(point, interface, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(point, panels, 0)
                if not collided:
                    return
                item = collided[len(collided)-1]
                if item.type == "warrior_card": #Карта в колоде! Карта на поле в cardbox
                    exec('selected_card_0 = cards.' + item.name + '()') #Переменной selected_card_0 присваиваем новый объект
                    selected_card = selected_card_0 # из локальной в глобальную
                    return
                if item.player.id != player.id:
                    return
                if item.type == "cardbox": #Если клик на карточный бокс
                    if item.card.name != "player": #Если в этом блоке есть карта
                        if item.card.cast: #если есть каст
                            if not item.card.used_cast: # если еще не кастовали
                                item.card.cast_action()
                    if selected_card: #если выбрана карта
                        if not player.action_points: #если уже ходил
                            return
                        exec('available_mana = player.' + selected_card.element + '_mana') # Вычисляем сколько маны у нас есть. Значение помещаем в локальную переменную available_mana
                        if available_mana < selected_card.level:
                            return
                        item.card = selected_card
                        item.card.parent = item
                        item.card.cardboxes = cardboxes
                        item.card.playerscards = playerscards
                        item.card.field = True
                        player.action_points = False
                        exec('player.' + selected_card.element + '_mana -= ' + str(selected_card.level)) #Отнимаем ману
                        interface.remove(cardsofelementshower1) #Закрываем окна выбора карты
                        interface.remove(cardsofelementshower2) #Закр. окна выбора карты
                        cards_in_deck.empty() #очищаем группу карты в колоде
                        if item.player.id == 1:
                            ccards_1.add(item.card)
                        else:
                            ccards_2.add(item.card)
                        selected_card = 0
                if item.type == 'elementbutton':
                    global cards_of_element_shower_element
                    cards_in_deck.empty()
                    if player.id == 1:
                        interface.add(cardsofelementshower1)
                    else:
                        interface.add(cardsofelementshower2)
                    if item.element == 'water':
                        cards_of_element_shower_element = "water"
                    elif item.element == 'fire':
                        cards_of_element_shower_element = "fire"
                    elif item.element == 'air':
                        cards_of_element_shower_element = "air"
                    elif item.element == 'earth':
                        cards_of_element_shower_element = "earth"
                    elif item.element == 'life':
                        cards_of_element_shower_element = "life"
                    elif item.element == 'death':
                        cards_of_element_shower_element = "death"
                elif item.type == 'completethecoursebutton':
                    finish_turn()
            elif event.button == 3: #ПРАВАЯ КНОПКА МЫШИ
                point.draw(event.pos)
                collided = pygame.sprite.spritecollide(point, cards_in_deck, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(point, interface, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(point, panels, 0)
                if not collided:
                    return
                item = collided[len(collided)-1]
                if item.type == "warrior_card": #по боевой карте
                    card_info_group.add(cardinfo)
                    cardinfo.text = item.info
                    cardinfo.show = True
                if item.type == "cardbox":
                    if item.card.name != "player":
                        card_info_group.add(cardinfo)
                        cardinfo.text = item.card.info
                        cardinfo.show = True
                if item.type == 'cardsofelementshower':
                    interface.remove(cardsofelementshower1)
                    interface.remove(cardsofelementshower2)
                    cards_in_deck.empty()
        elif event.type == MOUSEBUTTONUP: #отпускаем кнопку мыши
            if event.button == 3: #Правую
                if cardinfo.show:
                    cardinfo.show = False
                    card_info_group.empty()
#################################################################################################3
event_handler = Event_handler()
infopanel1 = Infopanel((0, 0), player1) #Инициализация панели верхнего игрока
infopanel2 = Infopanel((0, 545), player2) #Инициализация панели нижнего игрока
actionpanel1 = Actionpanel((0, 25), player1) #Панель с кнопками верхнего игрока
actionpanel2 = Actionpanel((0, 570), player2) #Панель с кнопками нижнего игрока
# 0 1 2 3 4   //Расположение
# 5 6 7 8 9
cardbox0 = Cardbox((0, 55), player1, 0) #0 место на поле
cardbox1 = Cardbox((160, 55), player1, 1) #1 место на поле
cardbox2 = Cardbox((320, 55), player1, 2) #2 место на поле
cardbox3 = Cardbox((480, 55), player1, 3) #3 место на поле
cardbox4 = Cardbox((640, 55), player1, 4) #4 место на поле
cardbox5 = Cardbox((0, 301), player2, 5) #5 место на поле
cardbox6 = Cardbox((160, 301), player2, 6) #6 место на поле
cardbox7 = Cardbox((320, 301), player2, 7) #7 место на поле
cardbox8 = Cardbox((480, 301), player2, 8) #8 место на поле
cardbox9 = Cardbox((640, 301), player2, 9) #9 место на поле
cardboxes = [cardbox0, cardbox1, cardbox2, cardbox3, cardbox4, cardbox5, cardbox6, cardbox7, cardbox8, cardbox8] #Ссылки на объекты
playerscards = [ccards_1, ccards_2] #Ссылки
#exec('Cardbox((640,301),2)')
#ElementsWindow((0,0),actionpanel1)
#ElementsWindow((0,0),actionpanel2)
HealthWindow((0, 0), infopanel1) #Окошко здоровья верхнего игрока
HealthWindow((0, 0), infopanel2) #Окошко здоровья нижнего игрока
# Кнопки колод стихий первого игрока
WaterElementButton((0, 0), actionpanel1)
FireElementButton((31, 0), actionpanel1)
AirElementButton((62, 0), actionpanel1)
EarthElementButton((93, 0), actionpanel1)
LifeElementButton((124, 0), actionpanel1)
DeathElementButton((155, 0), actionpanel1)
# Кнопки колод стихий второго игрока
WaterElementButton((0, 0), actionpanel2)
FireElementButton((31, 0), actionpanel2)
AirElementButton((62, 0), actionpanel2)
EarthElementButton((93, 0), actionpanel2)
LifeElementButton((124, 0), actionpanel2)
DeathElementButton((155, 0), actionpanel2)
#Кнопки завершения хода первого и второго игрока.
CompleteTheCourseButton((760, 0), actionpanel1)
CompleteTheCourseButton((760, 0), actionpanel2)
#Окна выбора карты стихии
cardsofelementshower1 = CardsOfElementShower((0, 301), player1)
cardsofelementshower2 = CardsOfElementShower((0, 55), player2)
#********************************************************************************
screen.blit(background, (0, 0))
panels.update()
interface.update()
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        event_handler.event(event)
    panels.update()
    interface.update()
    if player.id == 1:
        ccards_1.update(0)
        cards_in_deck.update(cardsofelementshower1)
    else:
        ccards_2.update(0)
        cards_in_deck.update(cardsofelementshower2)
    card_info_group.update()
    #interface_up_layer.update()
    screen.blit(background, (0, 0))
    background.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(8)