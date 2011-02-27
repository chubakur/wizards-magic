# -*- coding: utf-8 -*-
#import pygame
import cards
import random
import globals
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
            globals.gameinformationpanel.display("Game Over!")
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
def finish_turn():
    #Добавляем ману другому игроку.
    globals.player.enemy.water_mana += 1
    globals.player.enemy.fire_mana += 1
    globals.player.enemy.air_mana += 1
    globals.player.enemy.earth_mana += 1
    globals.player.enemy.life_mana += 1
    globals.player.enemy.death_mana += 1
    #Меняем игрока
    if globals.player.id == 1:
        globals.player = globals.player2
        globals.player.action_points = True
        for card in globals.ccards_1: #Атакуем
            kill = card.attack()
            if kill:
                card.enemy_die()
            card.used_cast = False
        for card in globals.ccards_2:
            card.turn()
    else:
        globals.player = globals.player1
        globals.player.action_points = True
        for card in globals.ccards_2: #Атакуем
            kill = card.attack()
            if kill:
                card.enemy_die()
            card.used_cast = False
        for card in globals.ccards_1:
            card.turn()