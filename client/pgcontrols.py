import pygame.sprite
#PGControls 
#Copyright (C) 2011 chubakur@gmail.com
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
import pygame
pygame.font.init()
font = pygame.font.Font("misc/Domestic_Manners.ttf", 10)
group = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self,parent,rect,func,label,group_u = False,):
        pygame.sprite.Sprite.__init__(self)
        self.type = "button"
        self.button_image = pygame.image.load('misc/pgcontrols/button.png')
        self.button_pressed_image = pygame.image.load('misc/pgcontrols/button_pressed.png')
        self.button_image_backup = self.button_image.copy()
        self.button_pressed_image_backup = self.button_pressed_image.copy()
        self.rect = self.button_image.get_rect().move(rect)
        self.parent = parent
        self.func = func
        self.pressed = 0
        self.render_label(label)
        self.impose_label()
        if not group_u:
            self.group = group
        else:
            self.group = group_u
        self.group.add(self)
        self.shown = True
    def hide(self):
        self.shown = False
        self.group.remove(self)
    def show(self):
        self.shown = True
        self.group.add(self)
    def press(self):
        self.pressed = 1
    def pull(self):
        self.pressed = 0
        self.func()
    def impose_label(self):
        self.button_image.blit(self.label,(self.button_image.get_size()[0]/2-self.label.get_size()[0]/2,self.button_image.get_size()[1]/2-self.label.get_size()[1]/2))
        self.button_pressed_image.blit(self.label,(self.button_image.get_size()[0]/2-self.label.get_size()[0]/2,self.button_image.get_size()[1]/2-self.label.get_size()[1]/2))
        #self.button_image_backup = self.button_image.copy()
        #self.button_pressed_image_backup = self.button_pressed_image.copy()
    def change_label(self, label):
        #self.label = label
        self.button_image = self.button_image_backup.copy()
        self.button_pressed_image = self.button_pressed_image_backup.copy()
        self.render_label(label)
        self.impose_label()
    def render_label(self, label):
        self.label = font.render(label,True,(255,255,255))
    def draw(self):
        if not self.pressed:
            self.parent.blit(self.button_image,self.rect)
        else:
            self.parent.blit(self.button_pressed_image,self.rect)
    def update(self):
        self.draw()