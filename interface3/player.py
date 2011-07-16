# -*- coding: utf-8 -*-
#import pygame
import cards
import os
import random
import globals
import sockets
import pygame
import ai
current_folder = os.path.dirname(os.path.abspath(__file__))

class Player(): #Прототип игрока
    def __init__(self, cli=False):
        self.health = 50
        self.name = "player"
        self.action_points = True #Ходил игрок, или нет
        self.get_cards()
        self.mana = {}
        self.get_mana()
        self.element = "none"
        self.ai = False
        self.cli = cli
        self.cards_generated = False
    def damage(self, damage, enemy, cast = False):
        self.health -= damage
        if self.health <= 0:
            globals.gameinformationpanel.display("Game Over!")
            globals.stage = False
    def heal(self, health):
        self.health += health
    def get_mana(self):
        #маны должно быть 25 в сумме!!
        manas = ["water","fire","air","earth","life","death"]
        random.shuffle(manas) #раскидываем массив рендомно
        sum = 0
        for mana_id in xrange(0, len(manas)):
            if mana_id != len(manas) - 1:
                rand = random.randint(2,5)
                sum+=rand
                self.mana[manas[mana_id]] = rand
            else:
                self.mana[manas[mana_id]] = 25 - sum
    def get_mana_count(self): #просмотр кол-ва маны
        return [self.mana['water'], self.mana['fire'], self.mana['air'], self.mana['earth'], self.mana['life'], self.mana['death']]
    def get_cards(self):
        self.water_cards = {}
        self.fire_cards = {}
        self.air_cards = {}
        self.earth_cards = {}
        self.life_cards = {}
        self.death_cards = {}
        water_cards_for_sort = []
        fire_cards_for_sort = []
        air_cards_for_sort = []
        earth_cards_for_sort = []
        life_cards_for_sort = []
        death_cards_for_sort = []
        for i in xrange(0, 4):
            #получаем карту элемента воды
            randnum = random.randint(0, len(cards.water_cards)-1)
            #self.water_cards[cards.links_to_cards[cards]]
            self.water_cards[cards.water_cards[randnum]] = cards.links_to_cards[cards.water_cards[randnum]]()
            water_cards_for_sort.append([self.water_cards[cards.water_cards[randnum]].level,self.water_cards[cards.water_cards[randnum]]])
            #print cards.links_to_cardscards.water_cards[randnum])
            #self.water_cards[cards.water_cards[randnum]].position_in_deck=i
            cards.water_cards.remove(cards.water_cards[randnum])
            #Элемент огня
            randnum = random.randint(0, len(cards.fire_cards)-1)
            self.fire_cards[cards.fire_cards[randnum]] = cards.links_to_cards[cards.fire_cards[randnum]]()
            #self.fire_cards[cards.fire_cards[randnum]].position_in_deck=i
            fire_cards_for_sort.append([self.fire_cards[cards.fire_cards[randnum]].level,self.fire_cards[cards.fire_cards[randnum]]])
            cards.fire_cards.remove(cards.fire_cards[randnum])
            #Элемент воздуха
            randnum = random.randint(0, len(cards.air_cards)-1)
            self.air_cards[cards.air_cards[randnum]] = cards.links_to_cards[cards.air_cards[randnum]]()
            #self.air_cards[cards.air_cards[randnum]].position_in_deck=i
            air_cards_for_sort.append([self.air_cards[cards.air_cards[randnum]].level,self.air_cards[cards.air_cards[randnum]]])
            cards.air_cards.remove(cards.air_cards[randnum])
            #Элемент земли
            randnum = random.randint(0, len(cards.earth_cards)-1)
            self.earth_cards[cards.earth_cards[randnum]] = cards.links_to_cards[cards.earth_cards[randnum]]()
            #self.earth_cards[cards.earth_cards[randnum]].position_in_deck=i
            earth_cards_for_sort.append([self.earth_cards[cards.earth_cards[randnum]].level,self.earth_cards[cards.earth_cards[randnum]]])
            cards.earth_cards.remove(cards.earth_cards[randnum])
            #Элемент жизни
            randnum = random.randint(0, len(cards.life_cards)-1)
            self.life_cards[cards.life_cards[randnum]] = cards.links_to_cards[cards.life_cards[randnum]]()
            #self.life_cards[cards.life_cards[randnum]].position_in_deck=i
            life_cards_for_sort.append([self.life_cards[cards.life_cards[randnum]].level,self.life_cards[cards.life_cards[randnum]]])
            cards.life_cards.remove(cards.life_cards[randnum])
            #Элемент смерти
            randnum = random.randint(0, len(cards.death_cards)-1)
            self.death_cards[cards.death_cards[randnum]] = cards.links_to_cards[cards.death_cards[randnum]]()
            #self.death_cards[cards.death_cards[randnum]].position_in_deck=i
            death_cards_for_sort.append([self.death_cards[cards.death_cards[randnum]].level,self.death_cards[cards.death_cards[randnum]]])
            cards.death_cards.remove(cards.death_cards[randnum])
        water_cards_for_sort.sort()
        fire_cards_for_sort.sort()
        air_cards_for_sort.sort()
        earth_cards_for_sort.sort()
        life_cards_for_sort.sort()
        death_cards_for_sort.sort()
        for i in xrange(0,4):
            water_cards_for_sort[i][1].position_in_deck = i
            fire_cards_for_sort[i][1].position_in_deck = i
            air_cards_for_sort[i][1].position_in_deck = i
            earth_cards_for_sort[i][1].position_in_deck = i
            life_cards_for_sort[i][1].position_in_deck = i
            death_cards_for_sort[i][1].position_in_deck = i
        del water_cards_for_sort
        del fire_cards_for_sort
        del air_cards_for_sort
        del earth_cards_for_sort
        del life_cards_for_sort
        del death_cards_for_sort
class Player1(Player):
    def __init__(self):
        self.id = 1
        Player.__init__(self)
class Player2(Player):
    def __init__(self):
        self.id = 2
        Player.__init__(self)
def switch_position():
    #globals.attack_started = False
    globals.attack_started.pop()
    for cardbox in globals.cardboxes:
        cardbox.opposite = not cardbox.opposite
def me_finish_turn():
    #Добавляем ману другому игроку.
    #globals.attack_started = True
    globals.attack_started.append(True)
    globals.player.enemy.mana['water'] += 1
    globals.player.enemy.mana['fire'] += 1
    globals.player.enemy.mana['air'] += 1
    globals.player.enemy.mana['earth'] += 1
    globals.player.enemy.mana['life'] += 1
    globals.player.enemy.mana['death'] += 1
    #Меняем игрока
    pygame.mixer.music.load(current_folder+'/misc/sounds/card_attack.mp3')
    globals.playmusic()
    if globals.player.id == 1:
        globals.player = globals.player2
        globals.player.action_points = True
        for card in globals.ccards_1: #Атакуем
            kill = card.attack()
            if kill:
                card.enemy_die()
            card.used_cast = False
        for spell in globals.magic_cards: #вызываем функцию повторения магия
            spell.periodical_cast()
        for card in globals.ccards_2:
            card.turn()
        for card in globals.ccards_2:
            card.additional_turn_action()
    else:
        globals.player = globals.player1
        globals.player.action_points = True
        for card in globals.ccards_2: #Атакуем
            kill = card.attack()
            if kill:
                card.enemy_die()
            card.used_cast = False
        for spell in globals.magic_cards: #вызываем функцию повторения магия
            spell.periodical_cast()
        for card in globals.ccards_1:
            card.turn()
        for card in globals.ccards_1:
            card.additional_turn_action()
    if globals.player.ai:
        cb = ai.select_cardbox()
        if cb:
            c = ai.select_card(cb.card)
            #print 'SELECTED',c
            cb.card = c()
            cb.card.field = True
            globals.player.mana[cb.card.element] -= cb.card.level
            cb.card.parent = cb
            if globals.player.id == 1:
                globals.ccards_1.add(cb.card)
            else:
                globals.ccards_2.add(cb.card)
            cb.card.summon()
        finish_turn()
def finish_turn():
    me_finish_turn()
    sockets.query({"action":"switch_turn"})
    #switch_position()
