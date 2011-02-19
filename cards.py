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
        pygame.sprite.Sprite.__init__(self)
        self.parent = 0
        self.image = self.image.convert_alpha()
        self.surface_backup = self.image.copy()
        self.font = pygame.font.Font(None,19)
        self.type = "warrior_card"
        self.moves_alive = 0 #Сколько ходов прожила карта
        self.max_health = self.health #Максимальное кол-во жизней
        self.field = False
        self.used_cast = False #Использовал cast
        #self.cast_button = pygame.Surface((30,20))
        #self.cast_button = self.cast_button.convert()
        #self.cast_button.fill((0,0,255))
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
    def cast_action(self):
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
        self.used_cast = False
        self.moves_alive+=1
        #print 1
        #print self.playerscards[self.parent.player.id-1].sprites()
        pass # Функция, которая вызывается каждый ход. Например для ледяного голема, у которого отнимаются жизни каждый ход.
    def update(self,cards_of_element_shower): #Field - True если рисовать на поле, false - если рисовать в таблице выбора
        text_level = font.render(str(self.level),True,(255,255,255))
        text_power = font.render(str(self.power),True,(255,255,255))
        text_health = font.render(str(self.health),True,(255,255,255))
        self.image = self.surface_backup.copy()
        if self.cast:
            if not self.used_cast:
                text_cast = font.render("Cast",True,(0,0,255))
                self.image.blit(text_cast,(50,100))
            else:
                text_cast = font.render("Cast",True,(0,0,0))
                self.image.blit(text_cast,(50,100))
        #print text_power
        self.image.blit(text_level,(130,10))
        self.image.blit(text_power,(10,230))
        self.image.blit(text_health,(130,230))
        if not self.field: #Рисование в колоде
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
        self.name = "Nixie"
        self.element = "water"
        self.level = 4
        self.power = 3
        self.health = 10
        self.cast = True
        self.image = pygame.image.load('misc/cards/water/nixie.gif')
        self.info = "SAghdagshagsdhuqwetghhsadgdhsassuahdyuhashgasdjeuidjzbjkxjofjhjfnbjghjdfhjdfhjchjjj  ghfvghjk23221123123"
        Prototype.__init__(self)
    def attack(self):
        if self.moves_alive:
            if self.parent.position<5:
                self.attack_position = self.parent.position+5 #Id - блока, куда атаковать
            else:
                self.attack_position = self.parent.position-5
            if self.cardboxes[self.attack_position].card.name!="player": #если есть карта
                if self.cardboxes[self.attack_position].card.element == "fire": #если стихия карты - огонь
                    self.cardboxes[self.attack_position].card.damage(self.power*2,self)
                else:
                    self.cardboxes[self.attack_position].card.damage(self.power,self)
            else:
                self.cardboxes[self.attack_position].card.damage(self.power,self)
        else:
            return
    def cast_action(self):
        print "Nixie Cast"
        if self.parent.player.fire_mana:
            self.parent.player.fire_mana-=1
            self.parent.player.water_mana+=1
            self.used_cast = True
        #Наносит картам элемента огня урон 200%
        #КАСТ:уменьшает ману огня на 1, увеличивает ману воды на 1
class Hydra(Prototype):
    def __init__(self):        
        self.name = "Hydra"
        self.element = "water"
        self.level = 13
        self.power = 5
        self.cast = False
        self.health = 29
        self.info = "Attacks both adjacent slots. Reduces owner`s Water by 2 every turn. CAST: Consumes friendly unit, receiving up to 50% of his health."
        self.image = pygame.image.load('misc/cards/water/hydra.gif')
        Prototype.__init__(self)
class Waterfall(Prototype):
    def __init__(self):        
        self.name = "Waterfall"
        self.element = "water"
        self.level = 9
        self.power = 1
        self.cast = False
        self.health = 33
        self.image = pygame.image.load('misc/cards/water/waterfall.gif')
        self.info = "One of the toughest Elementals. Health itself for 3 whenever any player casts water spell of summons water creature. Attack equal to owner`s Water."
        Prototype.__init__(self)
class Leviathan(Prototype):
    def __init__(self):        
        self.name = "Leviathan"
        self.element = "water"
        self.level = 11
        self.power = 6
        self.cast = False
        self.health = 37
        self.image = pygame.image.load('misc/cards/water/leviathan.gif')
        self.info = ""
        Prototype.__init__(self)
class IceGuard(Prototype):
    def __init__(self):        
        self.name = "IceGuard" 
        self.element = "water"
        self.level = 5
        self.info = "Reduces all damage done to owner by 50%. Suffers 200% damage from fire."
        self.power = 4
        self.cast = False
        self.health = 19
        self.image = pygame.image.load('misc/cards/water/ice_guard.gif')
        Prototype.__init__(self)
class Poseidon(Prototype):
    def __init__(self):        
        self.name = "Poseidon"        
        self.element = "water"
        self.level = 8
        self.power = 3
        self.info = "Every time anyone casts Water spell or summons Water creature, opponent suffers 4 damage and owner gains 2 health."
        self.cast = False
        self.health = 25
        self.image = pygame.image.load('misc/cards/water/poseidon.gif')
        Prototype.__init__(self)
class IceWizard(Prototype):
    def __init__(self):        
        self.name = "IceWizard"        
        self.element = "water"
        self.level = 10
        self.info = "Increases Water by 2 every turn. Suffers 200% damage from fire. All damage from Water equal to 1. CAST: Casting Healing Water heals owner equal to 2*Water points. Owner loses all Water."
        self.power = 4
        self.cast = False
        self.health = 22
        self.image = pygame.image.load('misc/cards/water/ice_wizard.gif')
        Prototype.__init__(self)
class Testw(Prototype):
    def __init__(self):        
        self.name = "Testw"        
        self.element = "water"
        self.level = 1
        self.power = 1
        self.info = ""
        self.cast = False
        self.health = 1
        self.image = pygame.image.load('misc/cards/water/testw.gif')
        Prototype.__init__(self)
class Demon(Prototype):
    def __init__(self):        
        self.name = "Demon"        
        self.element = "fire"
        self.level = 5
        self.power = 2
        self.info = "Doesn`t suffer from Fire and Earth spells. CAST: Whenewer Demon cassts Fire Bleed owner loses 1 Earth and receives 2 Fire elements."
        self.cast = False
        self.health = 12
        self.image = pygame.image.load('misc/cards/fire/demon.gif')
        Prototype.__init__(self)
        #Не получает повреждения от заклинаний огня и земли
        #cast: владелец теряет один элемент земли и получает 2 огня
class Devil(Prototype):
    def __init__(self):        
        self.name = "Devil"        
        self.element = "fire"
        self.info = "Damage from Water is multiplied by 2. Whenever Devil dies, owner suffers 10 damage. CAST: Sacrificing owner`s Fire creature gives 3 Fire to the owner, also healing owner by this amount."
        self.level = 6
        self.power = 4
        self.cast = False
        self.health = 27
        self.image = pygame.image.load('misc/cards/fire/devil.gif')
        Prototype.__init__(self)
class RedDrake(Prototype):
    def __init__(self):        
        self.name = "RedDrake"        
        self.element = "fire"
        self.level = 7
        self.info = ""
        self.power = 5
        self.cast = False
        self.health = 16
        self.image = pygame.image.load('misc/cards/fire/red_drake.gif')
        Prototype.__init__(self)
class Firelord(Prototype):
    def __init__(self):        
        self.name = "Firelord"        
        self.element = "fire"
        self.level = 11
        self.power = 7
        self.cast = False
        self.info = ""
        self.health = 21
        self.image = pygame.image.load('misc/cards/fire/firelord.gif')
        Prototype.__init__(self)
class Salamander(Prototype):
    def __init__(self):        
        self.name = "Salamander"        
        self.element = "fire"
        self.level = 8
        self.power = 3
        self.cast = False
        self.info = ""
        self.health = 15
        self.image = pygame.image.load('misc/cards/fire/salamander.gif')
        Prototype.__init__(self)
class Efreet(Prototype):
    def __init__(self):        
        self.name = "Efreet"        
        self.element = "fire"
        self.level = 10
        self.power = 6
        self.cast = False
        self.health = 33
        self.info = "Whenever any creature attacks Efreet, that creature suffers half of damage send back (same applies to Fire Shield spell). Uppon summoning, all enemy Water creatures suffer 6 damage. CAST: Casts Fire Shield on any owner`s creature. Costs 2 Fire. Fire Shield burns creature from inside, damaging it for 2 points per turn, unless it`s a Fire creature."
        self.image = pygame.image.load('misc/cards/fire/efreet.gif')
        Prototype.__init__(self)
class Vulcan(Prototype):
    def __init__(self):        
        self.name = "Vulcan"        
        self.element = "fire"
        self.level = 12
        self.power = 1
        self.cast = False
        self.info = "Fire Elemental. Immune to harmful Fire spells. When summoned, enemy player loses 3 Fire, and opposed Elemental unit suffers 9 damage. Attack equal to owner`s Fire + 3. CAST: Casts Volcano Explode. Vulcan dies, but every unit on field suffers damage equal to 50% of Vulcan`s health."
        self.health = 27
        self.image = pygame.image.load('misc/cards/fire/vulcan.gif')
        Prototype.__init__(self)
class Cerberus(Prototype):
    def __init__(self):        
        self.name = "Cerberus"        
        self.element = "fire"
        self.level = 4
        self.power = 4
        self.info = "Attacks adjacent enemy units at a half of it`s strength."
        self.cast = False
        self.health = 6
        self.image = pygame.image.load('misc/cards/fire/cerberus.gif')
        Prototype.__init__(self)
class Nymph(Prototype):
    def __init__(self):        
        self.name = "Nymph"        
        self.element = "air"
        self.level = 3
        self.power = 1
        self.cast = False
        self.info = ""
        self.health = 12
        self.image = pygame.image.load('misc/cards/air/nymph.gif')
        Prototype.__init__(self)
    def turn(self):
        self.parent.player.air_mana+=1
        #Каждый ход владелец получает дополнительно 1 воздух
class Fairy(Prototype):
    def __init__(self):        
        self.name = "Fairy"        
        self.element = "air"
        self.info = "Increases its attack by 1 for each creature, killed on a field. CAST: Enslave Mind forces strongest enemy creature to attack it`s owner. Costs 1 Air."
        self.level = 3
        self.power = 3
        self.cast = False
        self.health = 7
        self.image = pygame.image.load('misc/cards/air/fairy.gif')
        Prototype.__init__(self)
        #Атака увеличивается на 1 за каждого убитого
        #КАСТ. Сильнейшая карта врага атакует своего героя. 1 воздух.
class Phoenix(Prototype):
    def __init__(self):        
        self.name = "Phoenix"        
        self.element = "air"
        self.info = "If Phoenix was killed by Fire spell or creature, rebirth with full health."
        self.level = 6
        self.power = 4
        self.cast = False
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
        self.name = "Zeus"        
        self.element = "air"
        self.level = 9
        self.power = 3
        self.cast = False
        self.health = 24
        self.info = "Owner receives 1 air element for each enemy creature, killed by Zeus. CAST: Strikes Lighting into choosen creature. Costs 1 Air and inflicts 8 damage. Cannot strike creatures of level 7 and highter."
        self.image = pygame.image.load('misc/cards/air/zeus.gif')
        Prototype.__init__(self)
class Gargoyle(Prototype):
    def __init__(self):        
        self.name = "Gargoyle"        
        self.element = "air"
        self.info = "Suffers no damage from Earth and Air spells. CAST: Casts Petrification on self, as effect turns to stone. In stone form Gargoyle reduces damage done to it by 2 . Owner loses 3 Air and 1 Earth."
        self.level = 5
        self.power = 4
        self.cast = False
        self.health = 15
        self.image = pygame.image.load('misc/cards/air/gargoyle.gif')
        Prototype.__init__(self)
class Manticore(Prototype):
    def __init__(self):        
        self.name = "Manticore"        
        self.element = "air"
        self.info = "Attacks casters with additional 3 damage. Only suffers 50% damage from spells. CAST: Casts Memory Loss. Target enemy creature permanently loses ability to cast. Costs 2 Air."
        self.level = 7
        self.power = 5
        self.cast = False
        self.health = 19
        self.image = pygame.image.load('misc/cards/air/manticore.gif')
        Prototype.__init__(self)
class Titan(Prototype):
    def __init__(self):        
        self.name = "Titan"        
        self.element = "air"
        self.level = 11
        self.power = 7
        self.cast = False
        self.info = "When summoned, enemy loses 3 Air. Titan`s attack is increased by 1 for each Air creature in play. CAST: Casts Thunder Fist. All enemy Earth creatures suffer 3 damage. Owner loses 1 Air."
        self.health = 28
        self.image = pygame.image.load('misc/cards/air/titan.gif')
        Prototype.__init__(self)
class Testa(Prototype):
    def __init__(self):        
        self.name = "Testa"        
        self.element = "air"
        self.level = 1
        self.info = ""
        self.power = 1
        self.cast = False
        self.health = 1
        self.image = pygame.image.load('misc/cards/air/testa.gif')
        Prototype.__init__(self)
class Satyr(Prototype):
    def __init__(self):        
        self.name = "Satyr"        
        self.element = "earth"
        self.level = 2
        self.power = 3
        self.cast = False
        self.info = "Increases Earth by 1 every turn. CAST: Once Satyr casts Dissolve, it dies and creature in the opposed slot suffers 5 damage. If there`s no creature, damage dealt to enemy player."
        self.health = 10
        self.image = pygame.image.load('misc/cards/earth/satyr.gif')
        Prototype.__init__(self)
class Golem(Prototype):
    def __init__(self):        
        self.name = "Golem"        
        self.element = "earth"
        self.level = 5
        self.power = 4
        self.cast = False
        self.health = 15
        self.info = ""
        self.image = pygame.image.load('misc/cards/earth/golem.gif')
        Prototype.__init__(self)
class Dryad(Prototype):
    def __init__(self):        
        self.name = "Dryad"        
        self.element = "earth"
        self.level = 4
        self.power = 4
        self.cast = False
        self.health = 12
        self.info = "Adjacent owner creatures attack increases by 1, and if it`s Earth creaure, by 2 whenever anyone casts Earth spell of summons Earth creature."
        self.image = pygame.image.load('misc/cards/earth/dryad.gif')
        Prototype.__init__(self)
class ForestSpirit(Prototype):
    def __init__(self):        
        self.name = "ForestSpirit"        
        self.element = "earth"
        self.level = 3
        self.info = "Daamge from all non-magical attacks and abilities equal to 1. CAST: Casts Youth of Forest, increasing owner player`s health by 5. Costs two Earth elements."
        self.power = 2
        self.cast = False
        self.health = 3
        self.image = pygame.image.load('misc/cards/earth/forest_spirit.gif')
        Prototype.__init__(self)
    def damage(self,damage,enemy):
        self.health-=1
        if self.health<=0:
            self.die()
class Centaur(Prototype):
    def __init__(self):        
        self.name = "Centaur"        
        self.element = "earth"
        self.level = 6
        self.info = "Attacks the same turn he was summoned(No summon sickness). CAST: Strikes magic arrow into enemy player, dealing 3 damage. Costs 1 Earth."
        self.power = 5
        self.cast = False
        self.health = 14
        self.image = pygame.image.load('misc/cards/earth/centaur.gif')
        Prototype.__init__(self)
class Elemental(Prototype):
    def __init__(self):        
        self.name = "Elemental"
        self.element = "earth"        
        self.level = 13
        self.power = 1
        self.cast = False
        self.info = "Attack equal to owner`s Earth. Increases Earth by 2 every turn. Fire spells deal additional 10 damage. CAST: Casts Stone Skin onto owner`s creature. That creature gain 1 point of defence from all attacks greater than 1."
        self.health = 45
        self.image = pygame.image.load('misc/cards/earth/elemental.gif')
        Prototype.__init__(self)
class Ent(Prototype):
    def __init__(self):        
        self.name = "Ent"
        self.element = "earth"        
        self.level = 7
        self.power = 3
        self.info = ""
        self.cast = False
        self.health = 22
        self.image = pygame.image.load('misc/cards/earth/ent.gif')
        Prototype.__init__(self)
class Echidna(Prototype):
    def __init__(self):        
        self.name = "Echidna"
        self.element = "earth"        
        self.level = 10
        self.power = 7
        self.cast = False
        self.health = 26
        self.info = "When attacks, poisons her target. This target will lose 2 health every turn. In the beginning og owner`s turn, Echidna hits all poisoned creatures for 1."
        self.image = pygame.image.load('misc/cards/earth/echidna.gif')
        Prototype.__init__(self)
class Priest(Prototype):
    def __init__(self):        
        self.name = "Priest"        
        self.element = "life"
        self.level = 4
        self.cast = False
        self.power = 1
        self.health = 9
        self.info = "Increases owner`s Life by 2 every turn, decreasing Death by the same amount. Decreases owner`s Life by 3 every time owner casts Death spells."
        self.image = pygame.image.load('misc/cards/life/priest.gif')
        Prototype.__init__(self)
class Paladin(Prototype):
    def __init__(self):        
        self.name = "Paladin"
        self.element = "life"
        self.info = "Brings 300% of damage to undead creatures. CAST: Casts Exorcism. Destroys any undead, but suffers 10 damage himself. Owner also loses 2 Life as a cost of this holy casting."
        self.cast = False
        self.level = 8
        self.power = 4
        self.health = 20
        self.image = pygame.image.load('misc/cards/life/paladin.gif')
        Prototype.__init__(self)
class Pegasus(Prototype):
    def __init__(self):        
        self.name = "Pegasus"
        self.element = "life"        
        self.level = 6
        self.power = 6
        self.health = 15
        self.info = "When summoned, each owner`s creature is healed for 3. Also, it destroys harmful spell effects from each of them. CAST: Holy Strike deals 5 damage to a target creature. If it is undead creature, Pegasus also suffer 3 damage homself. Costs 2 Life."
        self.cast = False
        self.image = pygame.image.load('misc/cards/life/pegasus.gif')
        Prototype.__init__(self)
class Unicorn(Prototype):
    def __init__(self):        
        self.name = "Unicorn"
        self.element = "life"        
        self.level = 9
        self.power = 8
        self.cast = False
        self.info = ""
        self.health = 25
        self.image = pygame.image.load('misc/cards/life/unicorn.gif')
        Prototype.__init__(self)
class Apostate(Prototype):
    def __init__(self):        
        self.name = "Apostate"
        self.element = "life"        
        self.level = 5
        self.info = ""
        self.cast = False
        self.power = 4
        self.health = 14
        self.image = pygame.image.load('misc/cards/life/apostate.gif')
        Prototype.__init__(self)
class MagicHealer(Prototype):
    def __init__(self):        
        self.name = "MagicHealer"
        self.info = "Whenever owner player loses health, Magic Healer health player by this amount, losing hit points equally."
        self.element = "life"        
        self.level = 3
        self.power = 2
        self.cast = False
        self.health = 10
        self.image = pygame.image.load('misc/cards/life/magic_healer.gif')
        Prototype.__init__(self)
class Chimera(Prototype):
    def __init__(self):        
        self.name = "Chimera"
        self.element = "life"
        self.info = ""
        self.level = 11
        self.power = 11
        self.cast = False
        self.health = 30
        self.image = pygame.image.load('misc/cards/life/chimera.gif')
        Prototype.__init__(self)
class Testl(Prototype):
    def __init__(self):        
        self.name = "Testl"
        self.element = "life"        
        self.level = 1
        self.power = 1
        self.cast = False
        self.info = ""
        self.health = 1
        self.image = pygame.image.load('misc/cards/life/testl.gif')
        Prototype.__init__(self)
class Zombie(Prototype):
    def __init__(self):        
        self.name = "Zombie"        
        self.element = "death"
        self.level = 4
        self.power = 3
        self.health = 11
        self.info = "Eats enemies corpses - every time if kills enemy creature, totally health and his health increases by 3."
        self.cast = False
        self.image = pygame.image.load('misc/cards/death/zombie.gif')
        Prototype.__init__(self)
class Ghost(Prototype):
    def __init__(self):        
        self.name = "Ghost"
        self.element = "death"
        self.info = ""
        self.level = 3
        self.cast = False
        self.power = 3
        self.health = 13
        self.image = pygame.image.load('misc/cards/death/ghost.gif')
        Prototype.__init__(self)
class Vampire(Prototype):
    def __init__(self):        
        self.name = "Vampire"
        self.element = "death"        
        self.level = 9
        self.power = 6
        self.health = 22
        self.cast = False
        self.info = "When attacks living creature, restores health equal to 50% of damage dealt. Maximum 30 health."
        self.image = pygame.image.load('misc/cards/death/vampire.gif')
        Prototype.__init__(self)
class Werewolf(Prototype):
    def __init__(self):        
        self.name = "Werewolf"
        self.cast = False
        self.element = "death"
        self.level = 6
        self.power = 6
        self.info = "When dies, becomes a ghost. CAST: Casts Blood Rage on self. Strikes twice as hard this turn, but owner loses 3 Death points on casting."
        self.health = 16
        self.image = pygame.image.load('misc/cards/death/werewolf.gif')
        Prototype.__init__(self)
class Banshee(Prototype):
    def __init__(self):        
        self.name = "Banshee"        
        self.element = "death"
        self.info = ""
        self.level = 7
        self.cast = False
        self.power = 5
        self.health = 12
        self.image = pygame.image.load('misc/cards/death/banshee.gif')
        Prototype.__init__(self)
class GrimReaper(Prototype):
    def __init__(self):                
        self.name = "GrimReaper"
        self.info = "Whenever creature dies, increases owner`s Death by one. CAST: Consumes target enemy creature of level 3 or less. Owner player loses 3 Death elements."
        self.element = "death"
        self.level = 12
        self.power = 8
        self.cast = False
        self.health = 22
        self.image = pygame.image.load('misc/cards/death/grim_reaper.gif')
        Prototype.__init__(self)
class Darklord(Prototype):
    def __init__(self):        
        self.name = "Darklord"
        self.element = "death"
        self.info = ""
        self.level = 8
        self.power = 4
        self.cast = False
        self.health = 14
        self.image = pygame.image.load('misc/cards/death/darklord.gif')
        Prototype.__init__(self)
class Lich(Prototype):
    def __init__(self):        
        self.name = "Lich"
        self.element = "death"        
        self.level = 10
        self.info = "When summoned,deals 10 damage to creature in the opposite slot and two adjacent slots. Attacks Life units with additionial 5 damage. CAST:Casts Death Bolt, hitting enemy player with 7 of damage. Owner loses 5 Death. If owner`s Death becomes zero, he suffers 10 damage himself."
        self.cast = False
        self.power = 7
        self.health = 18
        self.image = pygame.image.load('misc/cards/death/lich.gif')
        Prototype.__init__(self)
#МАГИЯ
#**************************************************************************************************************
#--------------------------------------------------------------------------------------------------------------
#1728378w7dsfhdshuifedhsghfgfhdsghjsdgfhdsgdfyugdhsghfgdhsghjlfdsghgsdujhadhujgghsdgfs
#_____________________________________________________________________________________________________________
class Magic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "magic_card"
        self.magic = True
        #self.image = ""
        self.image = self.image.convert_alpha()
        self.surface_backup = self.image.copy()
        self.font = pygame.font.Font(None,19)
    def cast(self):
        pass
    def update(self):
        pass
class Poison(Magic):
    def __init__(self):
        self.element = "water"
        self.name = "Poison"
        self.level = 3
        self.image = pygame.image.load('misc/cards/water/poison.gif')
        Magic.__init__(self)
        #Каждый ход отнимает у карты противника по 1 здоровью. Не действует на класс смерти
class SeaJustice(Magic):
    def __init__(self):
        self.element = "water"
        self.name = "Sea Justice"
        self.level = 3
        self.image = pygame.image.load('misc/cards/water/sea_justice.gif')
        Magic.__init__(self)
        #Атакует каждую карту противника с силой равной силе карты-1
class Paralyze(Magic):
    def __init__(self):
        self.element = "water"
        self.name = "Paralyze"
        self.level = 10
        self.image = pygame.image.load('misc/cards/water/paralyze.gif')
        Magic.__init__(self)
        #противник пропускает ход
        