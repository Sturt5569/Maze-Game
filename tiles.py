import pygame
from assets import Assets
from maps import *

#----------define tiles which cause wall collisions. Impassable.----------#
class Boundary(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        img_set = get_imgset(Assets.img_set)
        self.type = type
        if type == 0:
            self.image = pygame.image.load(img_set[0]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 1:
            self.image = pygame.image.load(img_set[1]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 2:
            self.image = pygame.image.load(img_set[2]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 3:
            self.image = pygame.image.load(img_set[3]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 4:
            self.image = pygame.image.load(img_set[4]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 5:
            self.image = pygame.image.load(img_set[5]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 8:
            self.image = pygame.image.load(img_set[6]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 9:
            self.image = pygame.image.load(img_set[7]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 10:
            self.image = pygame.image.load(img_set[8]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 11:
            self.image = pygame.image.load(img_set[9]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 12:
            self.image = pygame.image.load(img_set[10]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 13:
            self.image = pygame.image.load(img_set[11]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 14:
            self.image = pygame.image.load(img_set[12]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 15:
            self.image = pygame.image.load(img_set[13]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)
        if type == 16:
            self.image = pygame.image.load(img_set[14]).convert_alpha()
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)

       
#----------define tiles the player can move over - no collision.----------#
class Path(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.type = type
        if type == 6:
            self.image = pygame.image.load('Maze/img/path.png')
            self.image.set_colorkey('#000000')
            self.rect = self.image.get_rect(topleft = pos)

class Grass(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.type = type
        if type == 7:
            self.image = pygame.image.load('Maze/img/grass.png')
            self.rect = self.image.get_rect(topleft = pos)

#----------Position the end target----------#
class Target(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('Maze/img/target.png').convert()
        self.rect = self.image.get_rect(topleft = pos)

#----------position keys ----------#
class Collectables(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.type = type
        if type == "yellowkey": 
            path = 'Maze/img/yellow_key.png'
        if type == "redkey":
            path = 'Maze/img/red_key.png'
        if type == 'bluekey':
            path = 'Maze/img/blue_key.png'
    
        self.image = pygame.image.load(path).convert_alpha()
        self.image.set_colorkey('#000000')
        self.rect = self.image.get_rect(topleft = pos)

#----------position locked doors----------#
class Doors(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.type = type
        if type == "yellowdoor": 
            self.image = pygame.image.load('Maze/img/yellow_door.png').convert_alpha()
            self.image.set_colorkey('#000000')
        if type == "reddoor":
            self.image = pygame.image.load('Maze/img/red_door.png').convert_alpha()
            self.image.set_colorkey('#000000')
        if type == 'bluedoor':
            self.image = pygame.image.load('Maze/img/blue_door.png').convert_alpha()
            self.image.set_colorkey('#000000')
    
        self.rect = self.image.get_rect(topleft = pos)

class Teleport(pygame.sprite.Sprite):

    def __init__(self,pos,id,target):
        super().__init__()
        self.id = id
        self.target = target
        self.image = pygame.image.load('Maze/img/tp1.png').convert_alpha()
        self.image.set_colorkey('#000000')
        self.rect = self.image.get_rect(topleft = pos)

