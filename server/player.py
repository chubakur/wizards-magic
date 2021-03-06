# -*- coding: utf-8 -*-
#import pygame
#SERVER!
import cards
import random
import globals
#import pygame
class Player(): #Прототип игрока
    def __init__(self):
        self.health = 50
        self.name = "player"
        self.action_points = True #Ходил игрок, или нет
    #def damage(self, damage, enemy):
     #   self.health -= damage
     #   if self.health <= 0:
      #      globals.gameinformationpanel.display("Game Over!")
   # def heal(self, health):
    #    self.health += health
    def get_mana(self): #Выдача маны!
        #маны должно быть 25 в сумме!!
        manas = ["self.water_mana","self.fire_mana","self.air_mana","self.earth_mana","self.life_mana","self.death_mana"]
        random.shuffle(manas) #раскидываем массив рендомно
        sum = 0
        for mana_id in xrange(0, len(manas)):
            if mana_id != len(manas) - 1:
                rand = random.randint(2,5)
                sum+=rand
                exec(manas[mana_id]+"=rand")
            else:
                exec(manas[mana_id]+"=25-sum")
    def get_mana_count(self): #просмотр кол-ва маны
        return [self.water_mana, self.fire_mana, self.air_mana, self.earth_mana, self.life_mana, self.death_mana]
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
            cards.water_cards.remove(cards.water_cards[randnum])
            #огня
            randnum = random.randint(0, len(cards.fire_cards)-1)
            self.fire_cards.append(cards.fire_cards[randnum])
            cards.fire_cards.remove(cards.fire_cards[randnum])
            #воздух
            randnum = random.randint(0, len(cards.air_cards)-1)
            self.air_cards.append(cards.air_cards[randnum])
            cards.air_cards.remove(cards.air_cards[randnum])
            #земля
            randnum = random.randint(0, len(cards.earth_cards)-1)
            self.earth_cards.append(cards.earth_cards[randnum])
            cards.earth_cards.remove(cards.earth_cards[randnum])
            #жизнь
            randnum = random.randint(0, len(cards.life_cards)-1)
            self.life_cards.append(cards.life_cards[randnum])
            cards.life_cards.remove(cards.life_cards[randnum])
            #смерть
            randnum = random.randint(0, len(cards.death_cards)-1)
            self.death_cards.append(cards.death_cards[randnum])
            cards.death_cards.remove(cards.death_cards[randnum])
#    def get_cards(self):
#        self.water_cards = []
#        self.fire_cards = []
#        self.air_cards = []
#        self.earth_cards = []
#        self.life_cards = []
#        self.death_cards = []
#        for i in xrange(0, 4):
#            #получаем карту элемента воды
#            randnum = random.randint(0, len(cards.water_cards)-1)
#            self.water_cards.append(cards.water_cards[randnum])
#            exec("self." + cards.water_cards[randnum].lower() + "=cards." + cards.water_cards[randnum] + "()")
#            cards.water_cards.remove(cards.water_cards[randnum])
#            #Элемент огня
#            randnum = random.randint(0, len(cards.fire_cards)-1)
#            self.fire_cards.append(cards.fire_cards[randnum])
#            exec("self." + cards.fire_cards[randnum].lower() + "=cards." + cards.fire_cards[randnum] + "()")
#            cards.fire_cards.remove(cards.fire_cards[randnum])
#            #Элемент воздуха
#            randnum = random.randint(0, len(cards.air_cards)-1)
#            self.air_cards.append(cards.air_cards[randnum])
#            exec("self." + cards.air_cards[randnum].lower() + "=cards." + cards.air_cards[randnum] + "()")
#            cards.air_cards.remove(cards.air_cards[randnum])
#            #Элемент земли
#            randnum = random.randint(0, len(cards.earth_cards)-1)
#            self.earth_cards.append(cards.earth_cards[randnum])
#            exec("self." + cards.earth_cards[randnum].lower() + "=cards." + cards.earth_cards[randnum] + "()")
#            cards.earth_cards.remove(cards.earth_cards[randnum])
#            #Элемент жизни
#            randnum = random.randint(0, len(cards.life_cards)-1)
#            self.life_cards.append(cards.life_cards[randnum])
#            exec("self." + cards.life_cards[randnum].lower() + "=cards." + cards.life_cards[randnum] + "()")
#            cards.life_cards.remove(cards.life_cards[randnum])
#            #Элемент смерти
#            randnum = random.randint(0, len(cards.death_cards)-1)
#            self.death_cards.append(cards.death_cards[randnum])
#            exec("self." + cards.death_cards[randnum].lower() + "=cards." + cards.death_cards[randnum] + "()")
#            cards.death_cards.remove(cards.death_cards[randnum])
#class Player1(Player):
#    def __init__(self):
#        self.id = 1
#        Player.__init__(self)
#class Player2(Player):
#    def __init__(self):
#        self.id = 2
#        Player.__init__(self)
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
        for spell in globals.magic_cards: #вызываем функцию повторения магия
            spell.periodical_cast()
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
        for spell in globals.magic_cards: #вызываем функцию повторения магия
            spell.periodical_cast()
        for card in globals.ccards_2: #Атакуем
            kill = card.attack()
            if kill:
                card.enemy_die()
            card.used_cast = False
        for card in globals.ccards_1:
            card.turn()