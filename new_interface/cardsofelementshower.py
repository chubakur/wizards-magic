# -*- coding: utf-8 -*-
import globals
import pygame
#globals.cards_of_element_shower_element содержит стихию
class CardsOfElementShower(pygame.sprite.Sprite):
    #Не прототип!
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.player = player
        self.type = 'cardsofelementshower'
        self.image = pygame.image.load('misc/cards_box.gif').convert_alpha()
        #self.rect = self.image.get_rect().move((rect[0], rect[1]))
        self.cards = 0
        self.shift = 2
        self.first_part = True #True - shows 1,2,3 from list, False shows 2,3,4 elements
    def draw(self):
        pass
        #globals.background.blit(self.image, self.rect)
    def update(self):
        #print self.type, 'update'
        globals.cards_in_deck.empty()
        self.cards = 0
        if globals.cards_of_element_shower_element == "water":
            if self.first_part:
                for card in globals.player.water_cards[0:3]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
            else:
                for card in globals.player.water_cards[1:4]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
        elif globals.cards_of_element_shower_element == "fire":
            if self.first_part:
                for card in globals.player.fire_cards[0:3]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
            else:
                for card in globals.player.fire_cards[1:4]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
        elif globals.cards_of_element_shower_element == "air":
            if self.first_part:
                for card in globals.player.air_cards[0:3]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
            else:
                for card in globals.player.air_cards[1:4]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
        elif globals.cards_of_element_shower_element == "earth":
            if self.first_part:
                for card in globals.player.earth_cards[0:3]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
            else:
                for card in globals.player.earth_cards[1:4]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
        elif globals.cards_of_element_shower_element == "life":
            if self.first_part:
                for card in globals.player.life_cards[0:3]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
            else:
                for card in globals.player.life_cards[1:4]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
        else:
            if self.first_part:
                for card in globals.player.death_cards[0:3]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")
            else:
                for card in globals.player.death_cards[1:4]:
                    exec("globals.cards_in_deck.add(globals.player." + card.lower() + ")")