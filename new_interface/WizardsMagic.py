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
#Внимание!! Для того, чтоsбы слои не наслаивались, я использую объект surface_backup , который является копией изображения. После этого они заменяются
__author__ = "chubakur"
__date__ = "$12.02.2011 12:11:42$"
import pygame
from pygame.locals import *
import sys
import player
import globals
import elementbutton
import cards
import cardinfo
import cardsofelementshower
import completethecoursebutton
import healthwindow
import cardbox
import eventhandler
import gameinformation
pygame.init()
globals.screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Wizards Magic')
clock = pygame.time.Clock()
globals.background = pygame.image.load('misc/bg_sample.gif')
#globals.background = globals.background.convert()
#globals.background = pygame.Surface(globals.screen.get_size())
globals.background = globals.background.convert_alpha()
#globals.background.fill((0, 0, 0))
background_backup = globals.background.copy()
#font.set_bold(0)
globals.player1 = player.Player1()
globals.player2 = player.Player2()
globals.player1.enemy = globals.player2
globals.player2.enemy = globals.player1
globals.player = globals.player1
globals.point = eventhandler.Point()
globals.cardinfo = cardinfo.CardInfo()
###############################################################################################################
#ACTIONS
#################################################################################################3
globals.event_handler = eventhandler.Event_handler()
#globals.infopanel1 = infopanel.Infopanel((0, 0), globals.player1) #Инициализация панели верхнего игрока
#globals.infopanel2 = infopanel.Infopanel((0, 545), globals.player2) #Инициализация панели нижнего игрока
#globals.actionpanel1 = actionpanel.Actionpanel((0, 25), globals.player1) #Панель с кнопками верхнего игрока
#globals.actionpanel2 = actionpanel.Actionpanel((0, 570), globals.player2) #Панель с кнопками нижнего игрока
# 0 1 2 3 4   //Расположение
# 5 6 7 8 9
globals.cardbox0 = cardbox.Cardbox((32, 44), globals.player1, 0) #0 место на поле
globals.cardbox1 = cardbox.Cardbox((187, 44), globals.player1, 1) #1 место на поле
globals.cardbox2 = cardbox.Cardbox((340, 44), globals.player1, 2) #2 место на поле
globals.cardbox3 = cardbox.Cardbox((495, 44), globals.player1, 3) #3 место на поле
globals.cardbox4 = cardbox.Cardbox((651, 44), globals.player1, 4) #4 место на поле
globals.cardbox5 = cardbox.Cardbox((32, 248), globals.player2, 5) #5 место на поле
globals.cardbox6 = cardbox.Cardbox((187, 248), globals.player2, 6) #6 место на поле
globals.cardbox7 = cardbox.Cardbox((340, 248), globals.player2, 7) #7 место на поле
globals.cardbox8 = cardbox.Cardbox((495, 248), globals.player2, 8) #8 место на поле
globals.cardbox9 = cardbox.Cardbox((651, 248), globals.player2, 9) #9 место на поле
globals.cardboxes = [globals.cardbox0, globals.cardbox1, globals.cardbox2, globals.cardbox3, globals.cardbox4, globals.cardbox5, globals.cardbox6, globals.cardbox7, globals.cardbox8, globals.cardbox9] #Ссылки на объекты
#playerscards = [globals.ccards_1, globals.ccards_2] #Ссылки
#exec('Cardbox((640,301),2)')
#ElementsWindow((0,0),actionpanel1)
#ElementsWindow((0,0),actionpanel2)
#healthwindow.HealthWindow((0, 0), globals.infopanel1) #Окошко здоровья верхнего игрока
#healthwindow.HealthWindow((0, 0), globals.infopanel2) #Окошко здоровья нижнего игрока
# Кнопки колод стихий первого игрока
elementbutton.WaterElementButton((369, 0),  globals.player1)
elementbutton.FireElementButton((400, 0),  globals.player1)
elementbutton.AirElementButton((431, 0),  globals.player1)
elementbutton.EarthElementButton((462, 0),  globals.player1)
elementbutton.LifeElementButton((493, 0),  globals.player1)
elementbutton.DeathElementButton((524, 0), globals.player1)
# Кнопки колод стихий второго игрока
elementbutton.WaterElementButton((186, 430),  globals.player2)
elementbutton.FireElementButton((217, 430),  globals.player2)
elementbutton.AirElementButton((248, 430),  globals.player2)
elementbutton.EarthElementButton((279, 430),  globals.player2)
elementbutton.LifeElementButton((310, 430),  globals.player2)
elementbutton.DeathElementButton((341, 430), globals.player2)
#Кнопки завершения хода первого и второго игрока.
completethecoursebutton.CompleteTheCourseButton((760, 0), globals.player1)
completethecoursebutton.CompleteTheCourseButton((760, 430), globals.player2)
#Окна выбора карты стихии
#globals.cardsofelementshower1 = cardsofelementshower.CardsOfElementShower((0, 301), globals.player1)
#globals.cardsofelementshower2 = cardsofelementshower.CardsOfElementShower((0, 55), globals.player2)
globals.cardofelementsshower = cardsofelementshower.CardsOfElementShower()
globals.gameinformationpanel = gameinformation.GameInformationPanel()
globals.gameinformationpanel.display('Battle started.')
#********************************************************************************
globals.screen.blit(globals.background, (0, 0))
globals.panels.update()
globals.interface.update()
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        globals.event_handler.event(event)
    globals.panels.update()
    globals.interface.update()
    if globals.player.id == 1:
        globals.ccards_1.update()
    else:
        globals.ccards_2.update()
    globals.cardofelementsshower.update()
    globals.cards_in_deck.update()
    globals.card_info_group.update()
    globals.information_group.update()
    #interface_up_layer.update()
    globals.screen.blit(globals.background, (0, 0))
    #globals.background.fill((0,0,0))
    globals.background = background_backup.copy()
    pygame.display.flip()
    clock.tick(10)