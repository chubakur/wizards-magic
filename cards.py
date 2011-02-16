# -*- coding: utf-8 -*-
import pygame.sprite
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
class Prototype(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def attack(self):
        pass
    def cast(self):
        pass
    def turn(self):
        pass # Функция, которая вызывается каждый ход. Например для ледяного голема, у которого отнимаются жизни каждый ход.
    def update(self,cards_of_element_shower,field): #Field - True если рисовать на поле, false - если рисовать в таблице выбора
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
        self.type = "card"
        self.element = "water"
        self.level = 4
        self.power = 3
        self.health = 10
        self.image = pygame.image.load('misc/cards/water/nixie.gif')
class Hydra(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Hydra"
        self.type = "card"
        self.element = "water"
        self.level = 13
        self.power = 5
        self.health = 29
        self.image = pygame.image.load('misc/cards/water/hydra.gif')
class Waterfall(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Waterfall"
        self.type = "card"
        self.element = "water"
        self.level = 9
        self.power = 1
        self.health = 33
        self.image = pygame.image.load('misc/cards/water/waterfall.gif')
class Leviathan(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Leviathan"
        self.type = "card"
        self.element = "water"
        self.level = 11
        self.power = 6
        self.health = 37
        self.image = pygame.image.load('misc/cards/water/leviathan.gif')
class IceGuard(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ice Guard"
        self.type = "card"
        self.element = "water"
        self.level = 5
        self.power = 4
        self.health = 19
        self.image = pygame.image.load('misc/cards/1.gif')
class Poseidon(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Poseidon"
        self.type = "card"
        self.element = "water"
        self.level = 8
        self.power = 3
        self.health = 25
        self.image = pygame.image.load('misc/cards/1.gif')
class IceWizard(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ice Wizard"
        self.type = "card"
        self.element = "water"
        self.level = 10
        self.power = 4
        self.health = 22
        self.image = pygame.image.load('misc/cards/1.gif')
class Testw(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Testw"
        self.type = "card"
        self.element = "water"
        self.level = 1
        self.power = 1
        self.health = 1
        self.image = pygame.image.load('misc/cards/1.gif')
class Demon(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Demon"
        self.type = "card"
        self.element = "fire"
        self.level = 5
        self.power = 2
        self.health = 12
        self.image = pygame.image.load('misc/cards/1.gif')
class Devil(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Devil"
        self.type = "card"
        self.element = "fire"
        self.level = 6
        self.power = 4
        self.health = 27
        self.image = pygame.image.load('misc/cards/1.gif')
class RedDrake(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Red Drake"
        self.type = "card"
        self.element = "fire"
        self.level = 7
        self.power = 5
        self.health = 16
        self.image = pygame.image.load('misc/cards/1.gif')
class Firelord(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Firelord"
        self.type = "card"
        self.element = "fire"
        self.level = 11
        self.power = 7
        self.health = 21
        self.image = pygame.image.load('misc/cards/1.gif')
class Salamander(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Salamander"
        self.type = "card"
        self.element = "fire"
        self.level = 8
        self.power = 3
        self.health = 15
        self.image = pygame.image.load('misc/cards/1.gif')
class Efreet(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Efreet"
        self.type = "card"
        self.element = "fire"
        self.level = 10
        self.power = 6
        self.health = 33
        self.image = pygame.image.load('misc/cards/1.gif')
class Vulcan(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Vulcan"
        self.type = "card"
        self.element = "fire"
        self.level = 12
        self.power = 1
        self.health = 27
        self.image = pygame.image.load('misc/cards/1.gif')
class Cerberus(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Cerberus"
        self.type = "card"
        self.element = "fire"
        self.level = 4
        self.power = 4
        self.health = 6
        self.image = pygame.image.load('misc/cards/1.gif')
class Nymph(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Nymph"
        self.type = "card"
        self.element = "air"
        self.level = 3
        self.power = 1
        self.health = 12
        self.image = pygame.image.load('misc/cards/1.gif')
class Fairy(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Fairy"
        self.type = "card"
        self.element = "air"
        self.level = 3
        self.power = 3
        self.health = 7
        self.image = pygame.image.load('misc/cards/1.gif')
class Phoenix(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Phoenix"
        self.type = "card"
        self.element = "air"
        self.level = 6
        self.power = 4
        self.health = 20
        self.image = pygame.image.load('misc/cards/1.gif')
class Zeus(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Zeus"
        self.type = "card"
        self.element = "air"
        self.level = 9
        self.power = 3
        self.health = 24
        self.image = pygame.image.load('misc/cards/1.gif')
class Gargoyle(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Gargoyle"
        self.type = "card"
        self.element = "air"
        self.level = 5
        self.power = 4
        self.health = 15
        self.image = pygame.image.load('misc/cards/1.gif')
class Manticore(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Manticore"
        self.type = "card"
        self.element = "air"
        self.level = 7
        self.power = 5
        self.health = 19
        self.image = pygame.image.load('misc/cards/1.gif')
class Titan(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Titan"
        self.type = "card"
        self.element = "air"
        self.level = 11
        self.power = 7
        self.health = 28
        self.image = pygame.image.load('misc/cards/1.gif')
class Testa(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Testa"
        self.type = "card"
        self.element = "air"
        self.level = 1
        self.power = 1
        self.health = 1
        self.image = pygame.image.load('misc/cards/1.gif')
class Satyr(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Satyr"
        self.type = "card"
        self.element = "earth"
        self.level = 2
        self.power = 3
        self.health = 10
        self.image = pygame.image.load('misc/cards/1.gif')
class Golem(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Golem"
        self.type = "card"
        self.element = "earth"
        self.level = 5
        self.power = 4
        self.health = 15
        self.image = pygame.image.load('misc/cards/1.gif')
class Dryad(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Dryad"
        self.type = "card"
        self.element = "earth"
        self.level = 4
        self.power = 4
        self.health = 12
        self.image = pygame.image.load('misc/cards/1.gif')
class ForestSpirit(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Forest Spirit"
        self.type = "card"
        self.element = "earth"
        self.level = 3
        self.power = 2
        self.health = 3
        self.image = pygame.image.load('misc/cards/1.gif')
class Centaur(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Centaur"
        self.type = "card"
        self.element = "earth"
        self.level = 6
        self.power = 5
        self.health = 14
        self.image = pygame.image.load('misc/cards/1.gif')
class Elemental(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Elemental"
        self.element = "earth"
        self.type = "card"
        self.level = 13
        self.power = 1
        self.health = 45
        self.image = pygame.image.load('misc/cards/1.gif')
class Ent(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ent"
        self.element = "earth"
        self.type = "card"
        self.level = 7
        self.power = 3
        self.health = 22
        self.image = pygame.image.load('misc/cards/1.gif')
class Echidna(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Echidna"
        self.element = "earth"
        self.type = "card"
        self.level = 10
        self.power = 7
        self.health = 26
        self.image = pygame.image.load('misc/cards/1.gif')
class Priest(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Priest"
        self.type = "card"
        self.element = "life"
        self.level = 4
        self.power = 1
        self.health = 9
        self.image = pygame.image.load('misc/cards/1.gif')
class Paladin(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Paladin"
        self.element = "life"
        self.type = "card"
        self.level = 8
        self.power = 4
        self.health = 20
        self.image = pygame.image.load('misc/cards/1.gif')
class Pegasus(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Pegasus"
        self.element = "life"
        self.type = "card"
        self.level = 6
        self.power = 6
        self.health = 15
        self.image = pygame.image.load('misc/cards/1.gif')
class Unicorn(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Unicorn"
        self.element = "life"
        self.type = "card"
        self.level = 9
        self.power = 8
        self.health = 25
        self.image = pygame.image.load('misc/cards/1.gif')
class Apostate(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Apostate"
        self.element = "life"
        self.type = "card"
        self.level = 5
        self.power = 4
        self.health = 14
        self.image = pygame.image.load('misc/cards/1.gif')
class MagicHealer(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Magic Healer"
        self.element = "life"
        self.type = "card"
        self.level = 3
        self.power = 2
        self.health = 10
        self.image = pygame.image.load('misc/cards/1.gif')
class Chimera(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Chimera"
        self.element = "life"
        self.type = "card"
        self.level = 11
        self.power = 11
        self.health = 30
        self.image = pygame.image.load('misc/cards/1.gif')
class Testl(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Testl"
        self.element = "life"
        self.type = "card"
        self.level = 1
        self.power = 1
        self.health = 1
        self.image = pygame.image.load('misc/cards/1.gif')
class Zombie(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Zombie"
        self.type = "card"
        self.element = "death"
        self.level = 4
        self.power = 3
        self.health = 11
        self.image = pygame.image.load('misc/cards/1.gif')
class Ghost(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Ghost"
        self.element = "death"
        self.type = "card"
        self.level = 3
        self.power = 3
        self.health = 13
        self.image = pygame.image.load('misc/cards/1.gif')
class Vampire(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Vampire"
        self.element = "death"
        self.type = "card"
        self.level = 9
        self.power = 6
        self.health = 22
        self.image = pygame.image.load('misc/cards/1.gif')
class Werewolf(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Werewolf"
        self.type = "card"
        self.element = "death"
        self.level = 6
        self.power = 6
        self.health = 16
        self.image = pygame.image.load('misc/cards/1.gif')
class Banshee(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Banshee"
        self.type = "card"
        self.element = "death"
        self.level = 7
        self.power = 5
        self.health = 12
        self.image = pygame.image.load('misc/cards/1.gif')
class GrimReaper(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "card"
        self.name = "Grim Reaper"
        self.element = "death"
        self.level = 12
        self.power = 8
        self.health = 22
        self.image = pygame.image.load('misc/cards/1.gif')
class Darklord(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Darklord"
        self.element = "death"
        self.type = "card"
        self.level = 8
        self.power = 4
        self.health = 14
        self.image = pygame.image.load('misc/cards/1.gif')
class Lich(Prototype):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Lich"
        self.element = "death"
        self.type = "card"
        self.level = 10
        self.power = 7
        self.health = 18
        self.image = pygame.image.load('misc/cards/1.gif')