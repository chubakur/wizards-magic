import pygame
import pygame.sprite
pygame.font.init()
font = pygame.font.Font("misc/Domestic_Manners.ttf", 10)
font2 = pygame.font.Font('misc/Domestic_Manners.ttf', 30)
group = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self, parent, rect, func, label, group_u=False):
        pygame.sprite.Sprite.__init__(self)
        self.font = font
        self.type = "button"
        self.button_image = pygame.image.load('misc/pgcontrols/button.png')
        self.button_pressed_image = pygame.image.load('misc/pgcontrols/button_pressed.png')
        self.button_image_backup = self.button_image.copy()
        self.button_pressed_image_backup = self.button_pressed_image.copy()
        self.rect = self.button_image.get_rect().move(rect)
        self.parent = parent
        self.func = func
        self.pressed = 0
        self.label_text = label
        self.color = (255, 255, 255)
        self.render_label(label)
        self.impose_label()
        if not group_u:
            self.group = group
        else:
            self.group = group_u
        self.group.add(self)
        self.shown = True
    def hide(self):
        if self.shown:
            self.shown = False
            self.group.remove(self)
        else:
            return
    def show(self):
        if not self.shown:
            self.shown = True
            self.group.add(self)
        else:
            return
    def press(self):
        self.pressed = 1
    def pull(self):
        self.pressed = 0
        self.func()
    def impose_label(self):
        self.button_image = self.button_image_backup.copy()
        self.button_pressed_image = self.button_pressed_image_backup.copy()
        self.button_image.blit(self.label, (self.button_image.get_size()[0] / 2-self.label.get_size()[0] / 2, self.button_image.get_size()[1] / 2-self.label.get_size()[1] / 2))
        self.button_pressed_image.blit(self.label, (self.button_image.get_size()[0] / 2-self.label.get_size()[0] / 2, self.button_image.get_size()[1] / 2-self.label.get_size()[1] / 2))
        #self.button_image_backup = self.button_image.copy()
        #self.button_pressed_image_backup = self.button_pressed_image.copy()
    def set_label(self, label):
        #self.label = label
        #self.button_image = self.button_image_backup.copy()
        #self.button_pressed_image = self.button_pressed_image_backup.copy()
        self.label_text = label
        self.render_label(label)
        self.impose_label()
    def render_label(self, label):
        self.label = self.font.render(label, True, self.color)
    def set_color(self, color):
        self.color = color
        self.render_label(self.label_text)
        self.impose_label()
    def draw(self):
        if not self.pressed:
            self.parent.blit(self.button_image, self.rect)
        else:
            self.parent.blit(self.button_pressed_image, self.rect)
    def update(self):
        self.draw()
class Label(pygame.sprite.Sprite):
    def __init__(self, parent, rect, label, group_u=False):
        pygame.sprite.Sprite.__init__(self)
        self.font = font2
        self.parent = parent
        self.color = (255, 255, 255)
        self.label_text = label
        #self.label = self.font.render(label, True, self.color)
        self.render_label()
        self.rect = self.label.get_rect().move(rect)
        self.shown = True
        if not group_u:
            self.group = group
        else:
            self.group = group_u
        self.group.add(self)
    def render_label(self):
        self.label = self.font.render(self.label_text, True, self.color)
    def set_color(self, color):
        self.color = color
        self.render_label()
    def set_label(self, label):
        self.label_text = label
        self.render_label()
    def show(self):
        if not self.shown:
            self.shown = True
            self.group.add(self)
        else:
            return
    def hide(self):
        if self.shown:
            self.shown = False
            self.group.remove(self)
        else:
            return
    def draw(self):
        self.parent.blit(self.label, self.rect)
    def update(self):
        self.draw()