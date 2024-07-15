import pygame
from assets import *


class Player(pygame.sprite.Sprite):

    xsnap = False                               #x and y axis grid snaps toggle on and off with key press
    ysnap = False                               #-------------------------------------------------------------#
    timer_start = 0                             #timer start time for snap activation                         #
    timer_end = 0                               #used to track time since no keys pressed.                    #
    timer_lock = False                          #output timer_ticks used in Level class to activate grid_snap #
    timer_ticks = 0                             #-------------------------------------------------------------#
    accel = 0

#----------list of available player icons----------#
    icons =['Maze/img/player_0.png',
            'Maze/img/player_1.png',
            'Maze/img/player_2.png',
            'Maze/img/player_3.png',
            'Maze/img/player_4.png',
            'Maze/img/player_5.png',
            'Maze/img/player_6.png']
    

           
#----------define player appearance----------#
    def __init__(self, pos):
        super().__init__()
        self.set_icon(Assets.player_icon)
        self.image = pygame.image.load(self.icon)
        self.image.set_colorkey('#000000')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
#----------obtain icon from list----------#
    def set_icon(self,num):
        self.icon = Player.icons[num]

#----------chec for key pressed and control snap----------#   
    def get_input(self):
        keys = pygame.key.get_pressed()
        Player.xsnap = True
        Player.ysnap = True
        if keys[pygame.K_RIGHT]:
            Player.xsnap = False
            Player.ysnap = True
            self.acceleration()
            self.direction.x = Assets.movement_speed
            Player.timer_lock = False
        if keys[pygame.K_LEFT]:
            Player.xsnap = False
            Player.ysnap = True
            self.acceleration()
            self.direction.x = -Assets.movement_speed
            Player.timer_lock = False
        if keys[pygame.K_UP]:
            Player.ysnap = False
            Player.xsnap = True
            self.acceleration()
            self.direction.y = -Assets.movement_speed
            Player.timer_lock = False
        if keys[pygame.K_DOWN]:
            Player.ysnap = False
            Player.xsnap = True
            self.acceleration()
            self.direction.y = Assets.movement_speed
            Player.timer_lock = False
#----------count ticks from no key pressed----------#
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                Assets.movement_speed = 2
                Player.accel = 0
                if not Player.timer_lock:
                    Player.timer_start = pygame.time.get_ticks()
                    Player.timer_lock = True
                Player.timer_end = pygame.time.get_ticks()
                Player.timer_ticks = Player.timer_end - Player.timer_start
                
    def acceleration(self):
        if Player.accel >=7:
            if Assets.movement_speed < Assets.max_speed:
               Assets.movement_speed += 0.5 
        else:
            Player.accel += 1
            
#----------adds to the superclass update method to call get_input function----------#
    def update(self):
        self.get_input()

