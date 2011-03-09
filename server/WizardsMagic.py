# -*- coding: utf-8 -*-
import json
#import pygame.sprite
#Wizards Magic Server
#Copyright (C) 2011  сhubakur
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# To change this template, choose Tools | Templates
# and open the template in the editor.
#import pygame.sprite
#Внимание!! Для того, чтоsбы слои не наслаивались, я использую объект surface_backup , который является копией изображения. После этого они заменяются
#__author__ = "chubakur"
#__date__ = "$12.02.2011 12:11:42$"
#import pygame
#from pygame.locals import *
#Коды answ
#100 - NO
#200 - OK
#300 - ping package
import sys
import player
import globals
#import elementbutton
#import cards
import socket
import json
import threading
host = "192.168.1.100"
port = 7712
sockets = []
class Connect(threading.Thread):
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        global connections
        if players>=2:
            self.sock.send(json.dumps({"answ":100, "petuh":len(connections)}))
            return
        sockets.append(self.sock)
        threading.Thread.__init__(self)
    def query(self, query):
        query = json.dumps(query)
        self.sock.send(query)
    def run(self):
        while True:
            data = self.sock.recv(1024)
            query = json.loads(data)
            if query['action'] == "join":
                global players
                players+=1
                globals.players.append(player.Player())
                id = len(globals.players) - 1
                globals.players[id].id = players
                #массив игроки. Элемент 0 - 1 игрок , элемент 1 - второй игрок
                #Отправляем сообщение , что все прошло Гуд, id игрока
                self.query({"answ":200, "id":globals.players[id].id})
                if players == 2:
                    for socket in sockets:
                        socket.send(json.dumps({"asd":"fuck"}))
            else:
                self.query({"answ":300})
        self.sock.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
players = 0
while True:
    sock, addr = s.accept()
    Connect(sock, addr).start()