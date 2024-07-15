import pygame
from assets import Assets
from random import randint

class Enemy(pygame.sprite.Sprite):

#----------define enemy appearance----------#
    def __init__(self,pos,type):
        super().__init__()
        self.image = pygame.image.load('img/enemy.png').convert()
        self.rect = self.image.get_rect(topleft = pos)
        self.type = type
        self.speed = Assets.enemy_speed
        self.change_direction()

#----------define vertical or horizontal movement per enemy----------#
    def movement(self):
        if self.type == "vertical_enemy":
            self.rect.y += self.speed
        if self.type == "horizontal_enemy":
            self.rect.x += self.speed
        if self.type == "random_enemy":
            if self.direction == 1:
                self.rect.y += self.speed
            if self.direction == 2:
                self.rect.y -= self.speed
            if self.direction == 3:
                self.rect.x += self.speed
            if self.direction == 4:
                self.rect.x -= self.speed

    def change_direction(self):
        self.direction = randint(1,4)
        
            
