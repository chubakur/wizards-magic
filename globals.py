# -*- coding: utf-8 -*-
import pygame
pygame.font.init()
panels = pygame.sprite.Group() #Нижний уровень
interface = pygame.sprite.Group() #Уровень кнопок
cards_in_deck = pygame.sprite.Group() #Уровень дополнительный
ccards_1 = pygame.sprite.Group() #  Карты, которые вывел первый игрок
ccards_2 = pygame.sprite.Group() # Карты, которые вывел второй игрок
cards_of_element_shower_element = "" #какой элемент показывать
selected_card = False #Выбранная карта
card_info_group = pygame.sprite.Group() #  Группа, которая содержит спрайт, содержащий панель вывода информации о карте
font = pygame.font.Font(None, 20)
screen = None
player = None
player1 = None
player2 = None