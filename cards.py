# -*- coding: utf-8 -*-
import pygame.sprite
#from WizardsMagic import cardbox0
# To change this template, choose Tools | Templates
# and open the template in the editor.
__author__="chubakur"
__date__ ="$13.02.2011 18:46:32$"
water_cards = ["Nixie","Hydra","Waterfall","Leviathan","IceGuard","Poseidon","IceWizard","Testw"]
fire_cards = ["Demon","Devil","Firelord","RedDrake","Efreet","Salamander","Vulcan","Cerberus"]
air_cards = ["Phoenix","Zeus","Fairy","Nymph","Gargoyle","Manticore","Titan","Testa"]
earth_cards = ["Satyr","Golem","Dryad","Centaur","Elemental","Ent","Echidna","ForestSpirit"]
life_cards = ["Priest","Paladin","Pegasus","Unicorn","Apostate","MagicHealer","Chimera","Testl"]
death_cards = ["Zombie","Vampire","GrimReaper","Ghost","Werewolf","Banshee","Darklord","Lich"]
import pygame
pygame.font.init()
font = pygame.font.Font(None,25)
class Prototype(pygame.sprite.Sprite): #Прототип карты воина
    def __init__(self):
        #self.group = group #Группа, в которой лежит эта карта
        self.parent = 0
        self.image = self.image.convert_alpha()
        self.surface_backup = self.image.copy()
        self.font = pygame.font.Font(None,19)
        self.type = "card"
        self.moves_alive = 0 #Сколько ходов прожила карта
        self.max_health = self.health #Максимальное кол-во жизней
    def attack(self): #Функция , срабатываемая при атаке персонажа
        if self.moves_alive:
            if self.parent.position<5:
                attack_position = self.parent.position+5 #Id - блока, куда атаковать
                self.cardboxes[attack_position].card.damage(self.power,self)
            else:
                attack_position = self.parent.position-5
                self.cardboxes[attack_position].card.damage(self.power,self)
        else:
            return
    def cast(self):
        pass
    def damage(self,damage,enemy): #Функция, срабатываемая при получении урона.
        self.health-=damage
        if self.health<=0:
            self.die()
    def die(self): #Смерть персонажа
            self.parent.card = self.parent.player #Обнуляем карту в объекте-родителе
            self.parent.image.blit(self.parent.surface_backup,(0,0)) #Рисуем объект-родитель поверх карты
            self.kill() #Выкидываем карту из всех групп
    def turn(self):
        pass # Функция, которая вызывается каждый ход. Например для ледяного голема, у которого отнимаются жизни каждый ход.
    def update(self,cards_of_element_shower,field): #Field - True если рисовать на поле, false - если рисовать в таблице выбора
        text_level = font.render(str(self.level),True,(255,255,255))
        text_power = font.render(str(self.power),True,(255,255,255))
        text_health = font.render(str(self.health),True,(255,255,255))
        self.image = self.surface_backup.copy()
        #print text_power
        self.image.blit(text_level,(130,10))
        self.image.blit(text_power,(10,230))
        self.image.blit(text_health,(130,230))
        if not field: #Рисование в колоде
            self.parent = cards_of_element_shower
            xshift = self.parent.shift*(self.parent.cards+1)+self.parent.cards*160
            self.parent.image.blit(self.image,(xshift,0))
            self.rect = self.image.get_rect().move((self.parent.rect[0],self.parent.rect[1]))
            self.rect = self.rect.move(xshift,0)
            self.parent.cards+=1
        else:
            self.parent.image.blit(self.image,(0,0))
class Nixie(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Nixie"
        self.element = "water"
        self.level = 4
        self.power = 3
        self.health = 10
        self.image = pygame.image.load('misc/cards/water/nixie.gif')
        Prototype.__init__(self)
class Hydra(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Hydra"
        self.element = "water"
        self.level = 13
        self.power = 5
        self.health = 29
        self.image = pygame.image.load('misc/cards/water/hydra.gif')
        Prototype.__init__(self)
class Waterfall(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Waterfall"
        self.element = "water"
        self.level = 9
        self.power = 1
        self.health = 33
        self.image = pygame.image.load('misc/cards/water/waterfall.gif')
        Prototype.__init__(self)
class Leviathan(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Leviathan"
        self.element = "water"
        self.level = 11
        self.power = 6
        self.health = 37
        self.image = pygame.image.load('misc/cards/water/leviathan.gif')
        Prototype.__init__(self)
class IceGuard(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ice Guard" 
        self.element = "water"
        self.level = 5
        self.power = 4
        self.health = 19
        self.image = pygame.image.load('misc/cards/water/ice_guard.gif')
        Prototype.__init__(self)
class Poseidon(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Poseidon"        
        self.element = "water"
        self.level = 8
        self.power = 3
        self.health = 25
        self.image = pygame.image.load('misc/cards/water/poseidon.gif')
        Prototype.__init__(self)
class IceWizard(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ice Wizard"        
        self.element = "water"
        self.level = 10
        self.power = 4
        self.health = 22
        self.image = pygame.image.load('misc/cards/water/ice_wizard.gif')
        Prototype.__init__(self)
class Testw(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Testw"        
        self.element = "water"
        self.level = 1
        self.power = 1
        self.health = 1
        self.image = pygame.image.load('misc/cards/water/testw.gif')
        Prototype.__init__(self)
class Demon(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Demon"        
        self.element = "fire"
        self.level = 5
        self.power = 2
        self.health = 12
        self.image = pygame.image.load('misc/cards/fire/demon.gif')
        Prototype.__init__(self)
class Devil(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Devil"        
        self.element = "fire"
        self.level = 6
        self.power = 4
        self.health = 27
        self.image = pygame.image.load('misc/cards/fire/devil.gif')
        Prototype.__init__(self)
class RedDrake(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Red Drake"        
        self.element = "fire"
        self.level = 7
        self.power = 5
        self.health = 16
        self.image = pygame.image.load('misc/cards/fire/red_drake.gif')
        Prototype.__init__(self)
class Firelord(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Firelord"        
        self.element = "fire"
        self.level = 11
        self.power = 7
        self.health = 21
        self.image = pygame.image.load('misc/cards/fire/firelord.gif')
        Prototype.__init__(self)
class Salamander(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Salamander"        
        self.element = "fire"
        self.level = 8
        self.power = 3
        self.health = 15
        self.image = pygame.image.load('misc/cards/fire/salamander.gif')
        Prototype.__init__(self)
class Efreet(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Efreet"        
        self.element = "fire"
        self.level = 10
        self.power = 6
        self.health = 33
        self.image = pygame.image.load('misc/cards/fire/efreet.gif')
        Prototype.__init__(self)
class Vulcan(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Vulcan"        
        self.element = "fire"
        self.level = 12
        self.power = 1
        self.health = 27
        self.image = pygame.image.load('misc/cards/fire/vulcan.gif')
        Prototype.__init__(self)
class Cerberus(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Cerberus"        
        self.element = "fire"
        self.level = 4
        self.power = 4
        self.health = 6
        self.image = pygame.image.load('misc/cards/fire/cerberus.gif')
        Prototype.__init__(self)
class Nymph(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Nymph"        
        self.element = "air"
        self.level = 3
        self.power = 1
        self.health = 12
        self.image = pygame.image.load('misc/cards/air/nymph.gif')
        Prototype.__init__(self)
class Fairy(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Fairy"        
        self.element = "air"
        self.level = 3
        self.power = 3
        self.health = 7
        self.image = pygame.image.load('misc/cards/air/fairy.gif')
        Prototype.__init__(self)
class Phoenix(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Phoenix"        
        self.element = "air"
        self.level = 6
        self.power = 4
        self.health = 20
        self.recovered = 0 #Восстанавливалась ли карта
        self.image = pygame.image.load('misc/cards/air/phoenix.gif')
        Prototype.__init__(self)
    def damage(self,damage,enemy):
        self.health-=damage
        if self.health<=0:
            if enemy.element == "fire": #Если стихия врага - огонь
                if not self.recovered: #если не восстанавливалась
                    self.health = self.max_health
                    self.recovered = True
                else:
                    self.die()
            else:
                self.die()
            #self.die()
class Zeus(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Zeus"        
        self.element = "air"
        self.level = 9
        self.power = 3
        self.health = 24
        self.image = pygame.image.load('misc/cards/air/zeus.gif')
        Prototype.__init__(self)
class Gargoyle(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Gargoyle"        
        self.element = "air"
        self.level = 5
        self.power = 4
        self.health = 15
        self.image = pygame.image.load('misc/cards/air/gargoyle.gif')
        Prototype.__init__(self)
class Manticore(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Manticore"        
        self.element = "air"
        self.level = 7
        self.power = 5
        self.health = 19
        self.image = pygame.image.load('misc/cards/air/manticore.gif')
        Prototype.__init__(self)
class Titan(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Titan"        
        self.element = "air"
        self.level = 11
        self.power = 7
        self.health = 28
        self.image = pygame.image.load('misc/cards/air/titan.gif')
        Prototype.__init__(self)
class Testa(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Testa"        
        self.element = "air"
        self.level = 1
        self.power = 1
        self.health = 1
        self.image = pygame.image.load('misc/cards/air/testa.gif')
        Prototype.__init__(self)
class Satyr(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Satyr"        
        self.element = "earth"
        self.level = 2
        self.power = 3
        self.health = 10
        self.image = pygame.image.load('misc/cards/earth/satyr.gif')
        Prototype.__init__(self)
class Golem(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Golem"        
        self.element = "earth"
        self.level = 5
        self.power = 4
        self.health = 15
        self.image = pygame.image.load('misc/cards/earth/golem.gif')
        Prototype.__init__(self)
class Dryad(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Dryad"        
        self.element = "earth"
        self.level = 4
        self.power = 4
        self.health = 12
        self.image = pygame.image.load('misc/cards/earth/dryad.gif')
        Prototype.__init__(self)
class ForestSpirit(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Forest Spirit"        
        self.element = "earth"
        self.level = 3
        self.power = 2
        self.health = 3
        self.image = pygame.image.load('misc/cards/earth/forest_spirit.gif')
        Prototype.__init__(self)
    def damage(self,damage):
        self.health-=1
        if self.health<=0:
            self.die()
class Centaur(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Centaur"        
        self.element = "earth"
        self.level = 6
        self.power = 5
        self.health = 14
        self.image = pygame.image.load('misc/cards/earth/centaur.gif')
        Prototype.__init__(self)
class Elemental(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Elemental"
        self.element = "earth"        
        self.level = 13
        self.power = 1
        self.health = 45
        self.image = pygame.image.load('misc/cards/earth/elemental.gif')
        Prototype.__init__(self)
class Ent(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ent"
        self.element = "earth"        
        self.level = 7
        self.power = 3
        self.health = 22
        self.image = pygame.image.load('misc/cards/earth/ent.gif')
        Prototype.__init__(self)
class Echidna(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Echidna"
        self.element = "earth"        
        self.level = 10
        self.power = 7
        self.health = 26
        self.image = pygame.image.load('misc/cards/earth/echidna.gif')
        Prototype.__init__(self)
class Priest(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Priest"        
        self.element = "life"
        self.level = 4
        self.power = 1
        self.health = 9
        self.image = pygame.image.load('misc/cards/life/priest.gif')
        Prototype.__init__(self)
class Paladin(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Paladin"
        self.element = "life"        
        self.level = 8
        self.power = 4
        self.health = 20
        self.image = pygame.image.load('misc/cards/life/paladin.gif')
        Prototype.__init__(self)
class Pegasus(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Pegasus"
        self.element = "life"        
        self.level = 6
        self.power = 6
        self.health = 15
        self.image = pygame.image.load('misc/cards/life/pegasus.gif')
        Prototype.__init__(self)
class Unicorn(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Unicorn"
        self.element = "life"        
        self.level = 9
        self.power = 8
        self.health = 25
        self.image = pygame.image.load('misc/cards/life/unicorn.gif')
        Prototype.__init__(self)
class Apostate(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Apostate"
        self.element = "life"        
        self.level = 5
        self.power = 4
        self.health = 14
        self.image = pygame.image.load('misc/cards/life/apostate.gif')
        Prototype.__init__(self)
class MagicHealer(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Magic Healer"
        self.element = "life"        
        self.level = 3
        self.power = 2
        self.health = 10
        self.image = pygame.image.load('misc/cards/life/magic_healer.gif')
        Prototype.__init__(self)
class Chimera(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Chimera"
        self.element = "life"        
        self.level = 11
        self.power = 11
        self.health = 30
        self.image = pygame.image.load('misc/cards/life/chimera.gif')
        Prototype.__init__(self)
class Testl(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Testl"
        self.element = "life"        
        self.level = 1
        self.power = 1
        self.health = 1
        self.image = pygame.image.load('misc/cards/life/testl.gif')
        Prototype.__init__(self)
class Zombie(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Zombie"        
        self.element = "death"
        self.level = 4
        self.power = 3
        self.health = 11
        self.image = pygame.image.load('misc/cards/death/zombie.gif')
        Prototype.__init__(self)
class Ghost(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ghost"
        self.element = "death"        
        self.level = 3
        self.power = 3
        self.health = 13
        self.image = pygame.image.load('misc/cards/death/ghost.gif')
        Prototype.__init__(self)
class Vampire(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Vampire"
        self.element = "death"        
        self.level = 9
        self.power = 6
        self.health = 22
        self.image = pygame.image.load('misc/cards/death/vampire.gif')
        Prototype.__init__(self)
class Werewolf(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Werewolf"        
        self.element = "death"
        self.level = 6
        self.power = 6
        self.health = 16
        self.image = pygame.image.load('misc/cards/death/werewolf.gif')
        Prototype.__init__(self)
class Banshee(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Banshee"        
        self.element = "death"
        self.level = 7
        self.power = 5
        self.health = 12
        self.image = pygame.image.load('misc/cards/death/banshee.gif')
        Prototype.__init__(self)
class GrimReaper(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        
        self.name = "Grim Reaper"
        self.element = "death"
        self.level = 12
        self.power = 8
        self.health = 22
        self.image = pygame.image.load('misc/cards/death/grim_reaper.gif')
        Prototype.__init__(self)
class Darklord(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Darklord"
        self.element = "death"        
        self.level = 8
        self.power = 4
        self.health = 14
        self.image = pygame.image.load('misc/cards/death/darklord.gif')
        Prototype.__init__(self)
class Lich(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Lich"
        self.element = "death"        
        self.level = 10
        self.power = 7
        self.health = 18
        self.image = pygame.image.load('misc/cards/death/lich.gif')
        Prototype.__init__(self)