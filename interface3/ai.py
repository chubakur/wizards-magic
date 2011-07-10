# -*- coding: utf-8 -*-
import globals
import cards
import random
def select_cardbox():
    s_cardboxes = []
    if globals.player.id == 1:
        for cardbox in globals.cardboxes[0:5]:
            if cardbox.card.name is "player": #если есть карта
                s_cardboxes.append(cardbox)
    else:
        for cardbox in globals.cardboxes[5:10]:
            if cardbox.card.name is "player":
                s_cardboxes.append(cardbox)
    e_cardboxes = []
    if globals.player.id == 2:
        for cardbox in globals.cardboxes[0:5]:
            if cardbox.card.name != "player": #если есть карта
                e_cardboxes.append(cardbox)
    else:
        for cardbox in globals.cardboxes[5:10]:
            if cardbox.card.name != "player":
                e_cardboxes.append(cardbox)
    e_strongest = None
    e_strongest_power = 0
    if not len(e_cardboxes):
        return s_cardboxes[0]
    while True:
        for cardbox in e_cardboxes:
            if cardbox.card.power > e_strongest_power:
                e_strongest_cardbox = cardbox
                e_strongest_power = cardbox.card.power
        if e_strongest_power:
            if e_strongest_cardbox.get_opposite_cardbox() not in s_cardboxes:
                e_cardboxes.remove(e_strongest_cardbox)
                e_strongest = None
                e_strongest_power = 0
            else:
                return  e_strongest_cardbox.get_opposite_cardbox()
        else:
            return s_cardboxes[0]
def select_card(enemy_card):
    player = globals.player
    self_cards = player.water_cards.values() + player.fire_cards.values() + player.air_cards.values() + player.earth_cards.values() + player.life_cards.values() + player.death_cards.values()
    random.shuffle(self_cards)
    item = None
    max_eff = 0
    for card in self_cards:
        if card.type is 'warrior_card':
            eff = card.ai('summon',enemy_card)
            if eff>=max_eff:
                max_eff = eff
                item = card
    return item.__class__