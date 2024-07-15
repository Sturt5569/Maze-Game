import pygame
from tiles import *
from player import Player
from assets import *
from maps import import_csv_layout,level_assets
from vfx import Mask
from enemy import Enemy

#---------- Displays the bar across the top of the game screen----------#
class HUD:
    def __init__(self,surface):
        self.display_surface = surface
        #---------- load image components of HUD bar ----------#
        self.menubar = pygame.image.load('Maze/img/menubar_bg.png').convert()
        self.menubar = pygame.transform.scale(self.menubar,(Assets.width,32))
        self.menubar_rect = self.menubar.get_rect(topleft = (0,0))
        self.menucent = pygame.image.load('Maze/img/menubar_center.png').convert()
        self.menucent_rect = self.menucent.get_rect(center = (Assets.width/2,16))
        self.menubutt = pygame.image.load('Maze/img/menubar_menubutton.png').convert()
        self.menubutt_rect = self.menubutt.get_rect(topleft = (0,0))
        self.menuinventory = pygame.image.load('Maze/img/menubar_inventory.png').convert()
        self.menuinventory_rect = self.menuinventory.get_rect(topright = (Assets.width,0))

        #---------- Load images for inventory tray on HUD ----------#
        self.inventory_x = self.menuinventory_rect.x
        self.yellowcollected = pygame.image.load('Maze/img/yellow_key.png').convert_alpha()
        self.yellowcollected.set_colorkey('#000000')
        self.yellowrect = self.yellowcollected.get_rect(center = (self.inventory_x+24,17))
        self.bluecollected = pygame.image.load('Maze/img/blue_key.png').convert_alpha()
        self.bluecollected.set_colorkey('#000000')
        self.bluerect = self.bluecollected.get_rect(center = (self.inventory_x+50,17))
        self.redcollected = pygame.image.load('Maze/img/red_key.png').convert_alpha()
        self.redcollected.set_colorkey('#000000')
        self.redrect = self.redcollected.get_rect(center = (self.inventory_x+77,17))

        self.create_menu_bar()

#---------- prints all HUD elements to a separate surface ----------#
    def create_menu_bar(self):                   
        self.hud_surface = pygame.Surface((Assets.width,32))
        self.hud_surface.blit(self.menubar,self.menubar_rect)
        self.hud_surface.blit(self.menubutt,self.menubutt_rect)
        self.hud_surface.blit(self.menucent,self.menucent_rect)
        self.hud_surface.blit(self.menuinventory,self.menuinventory_rect)
        self.level_number()

#---------- generates the level number in the center of the HUD ----------#
    def level_number(self): 
        self.leveltext = pygame.image.load('Maze/img/level.png').convert_alpha()
        self.leveltext.set_colorkey('#000000')
        level_number = str(Assets.lvl)
        self.digits = len(level_number)
        self.x_offset = ((self.digits * 13) + (self.digits * 5) + 62)//2
        self.xpos = Assets.width/2 - self.x_offset
        self.hud_surface.blit(self.leveltext,(self.xpos,6))
#---------- Displays the level number in the centre ----------#
        for dig in level_number:
            path = "Maze/img/" + dig + ".png"
            image = pygame.image.load(path).convert_alpha()
            image.set_colorkey('#000000')
            xpos = self.xpos + 60 
            self.hud_surface.blit(image,(xpos,6))
            self.xpos += 11

#---------- print the HUD to the display surface ----------#
    def display_hud(self,surface,event_list,mousex, mousey): 
        self.display_surface = surface
        self.mouse_x = mousex
        self.mouse_y = mousey
        self.event_list = event_list
        self.display_surface.blit(self.hud_surface,(0,0)) 

    #---------- Menu button event handler ----------#
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menubutt_rect.collidepoint(self.mouse_x,self.mouse_y):
                    Assets.game_menu = True
                    Assets.sfx.click()

    #---------- Check if keys are collected and display if true ----------#
        for item in level_assets[Assets.lvl]:
            if item.get('item') == 'yellowkey' and Level.yellowunlocked:
                self.hud_surface.blit(self.yellowcollected,self.yellowrect)
            if item.get('item') == 'bluekey' and Level.blueunlocked:
                self.hud_surface.blit(self.bluecollected,self.bluerect)
            if item.get('item') == 'redkey' and Level.redunlocked:
                self.hud_surface.blit(self.redcollected,self.redrect)        


class Level:
    
    #---------- variables for level-wide use ----------#
    yellowunlocked = False
    redunlocked = False
    blueunlocked = False
    mask = False
    tick1 = 0
    tick2 = 0
    averagetick = 0
    fps = []
    tickdelay = 0

#---------- initialise level ----------#
    def __init__(self,level_data,items,surface):
        self.display_surface = surface
        self.level_data = import_csv_layout(level_data)
        self.define_size(surface)
        self.setup_level(self.level_data,items)
        self.hud = HUD(self.display_surface)    
        self.wall_image_load = pygame.image.load('Maze/img/game_background.jpg').convert()
        self.wall_image = pygame.transform.scale(self.wall_image_load,(Assets.width,Assets.height))

#----------get current screen size and write to global variables----------#
    def define_size(self,surface): 
        Assets.width = surface.get_width()
        Assets.height = surface.get_height()
        return (Assets.width, Assets.height)

#----------generates game map, collectables and objects----------#    
    def setup_level(self,layout,items): 
        Level.yellowunlocked = False
        Level.redunlocked = False
        Level.blueunlocked = False  
        Assets.prompt = False 
        Assets.port_locked = False       
        self.boundary = pygame.sprite.Group()
        self.path = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.target = pygame.sprite.Group()
        self.yellowkey = pygame.sprite.GroupSingle()
        self.bluekey = pygame.sprite.GroupSingle()
        self.redkey = pygame.sprite.GroupSingle()
        self.yellowdoor = pygame.sprite.Group()
        self.bluedoor = pygame.sprite.Group()
        self.reddoor = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.ports = pygame.sprite.Group()


#---------- generate grid the map is based on ----------#
        for row_index, row in enumerate(layout):        
            for col_index, cell in enumerate(row):
                x_offset = (Assets.width - (len(row) * tile_size))/2
                y_offset = (Assets.height - (len(layout) * tile_size))/2             
                x = col_index * tile_size + x_offset
                y = row_index * tile_size + 16 + y_offset
                cell = int(cell)
                if cell != 6 and cell !=7:                          
                    tile = Boundary((x,y),cell)
                    self.boundary.add(tile)
                if cell == 7:
                    grass = Grass((x,y),cell)
                    self.grass.add(grass)
                if cell == 6:
                    path = Path((x,y),cell)
                    self.path.add(path)
                    
        
#---------- place doors and keys on map. ----------#
        for item in items:
            type = item.get('item')
            x = item.get('location_x') * tile_size + x_offset
            y = (item.get('location_y') * tile_size) + 16 + y_offset
            if type == "yellowkey":
                create_object = Collectables((x,y),type)
                self.yellowkey.add(create_object)
            if type == "bluekey":
                create_object = Collectables((x,y),type)
                self.bluekey.add(create_object)
            if type == "redkey":
                create_object = Collectables((x,y),type)
                self.redkey.add(create_object)
            if type == "yellowdoor":
                create_object = Doors((x,y),type)
                self.yellowdoor.add(create_object)
            if type == "bluedoor":
                create_object = Doors((x,y),type)
                self.bluedoor.add(create_object)
            if type == "reddoor":
                create_object = Doors((x,y),type)
                self.reddoor.add(create_object)
            if type == 'target':
                create_object = Target((x,y))
                self.target.add(create_object)
            if type == 'player':
                player_sprite = Player((x,y))
                self.player.add(player_sprite)
            if type == 'vertical_enemy' or type == 'horizontal_enemy':
                enemy_sprite = Enemy((x,y),type)
                self.enemies.add(enemy_sprite)
            if type == 'random_enemy':
                enemy_sprite = Enemy((x,y),type)
                self.enemies.add(enemy_sprite)
            if type == 'mask':
                if item.get('active') == True:
                    Level.mask = True
                    self.drawmask = Mask(self.display_surface,(Assets.width,Assets.height))
                else:
                    Level.mask = False
            if type == 'teleport':
                id =  item.get('id')
                target = item.get('target')
                port = Teleport((x,y),id,target)
                self.ports.add(port)

    def horizontal_movement_collision(self):
         player = self.player.sprite
         player.rect.x += player.direction.x
         for sprite in self.boundary.sprites():
             if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                   player.rect.right = sprite.rect.left
         for sprite in self.reddoor.sprites():
             if sprite.rect.colliderect(player.rect):
                if Level.redunlocked:
                    sprite.kill()
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                   player.rect.right = sprite.rect.left

         for sprite in self.yellowdoor.sprites():
             if sprite.rect.colliderect(player.rect):
                if Level.yellowunlocked:
                    sprite.kill()
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                   player.rect.right = sprite.rect.left

         for sprite in self.bluedoor.sprites():
             if sprite.rect.colliderect(player.rect):
                if Level.blueunlocked:
                    sprite.kill()
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                   player.rect.right = sprite.rect.left
                                
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y  
        for sprite in self.boundary.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                   player.rect.bottom = sprite.rect.top
        for sprite in self.yellowdoor.sprites():
            if sprite.rect.colliderect(player.rect):
                if Level.yellowunlocked:
                    sprite.kill()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                   player.rect.bottom = sprite.rect.top
        for sprite in self.reddoor.sprites():
            if sprite.rect.colliderect(player.rect):
                if Level.redunlocked:
                    sprite.kill()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                   player.rect.bottom = sprite.rect.top
        for sprite in self.bluedoor.sprites():
            if sprite.rect.colliderect(player.rect):
                if Level.blueunlocked:
                    sprite.kill()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                   player.rect.bottom = sprite.rect.top

    def enemy_movement(self):
        for enemy in self.enemies.sprites():
            enemy.movement()

    def enemy_collision(self):
        player = self.player.sprite
        for enemy in self.enemies.sprites():
            enemy_rect = enemy.rect
            if enemy.rect.colliderect(player.rect):
                message1 = "You were caught!"
                message2 = "Click Confirm to restart"
                next = Assets.message.prompt_single(message1, message2)
                if next:
                    Assets.sfx.click()
                    Assets.map = Level(level_list.get(Assets.lvl), level_assets[Assets.lvl], self.display_surface)
                    Assets.map.print_level()
                else:
                    Assets.gamestate = "overworld"

            for sprite in self.boundary.sprites():
                if sprite.rect.colliderect(enemy_rect):
                    if enemy.type != "random_enemy":
                        enemy.speed *= -1
                    else:
                        if enemy.direction == 1:
                            enemy.rect.bottom = sprite.rect.top
                        elif enemy.direction == 2:
                            enemy.rect.top = sprite.rect.bottom
                        elif enemy.direction == 3:
                            enemy.rect.right = sprite.rect.left
                        elif enemy.direction == 4:
                            enemy.rect.left = sprite.rect.right
                        enemy.change_direction()

#----------player is captured if going off grid and pulled to nearest ref after 40ms----------#
    def grid_snap(self): 
        player = self.player.sprite
        player_center = player.rect.center
        playerx,playery = player.rect.center
        if Player.xsnap == True:
            for sprite in self.path.sprites():
                if sprite.rect.collidepoint(player_center):
                    snapx,snapy = sprite.rect.center
            if playerx == snapx:
                player.direction.x = 0
        if Player.ysnap == True:
            for sprite in self.path.sprites():
                if sprite.rect.collidepoint(player_center):
                    snapx,snapy = sprite.rect.center
            if playery == snapy:
                player.direction.y = 0  
        if Player.timer_ticks >= 40 and Player.xsnap and Player.ysnap:
            player.direction.x = 0
            player.direction.y = 0
            for sprite in self.path.sprites():
                if sprite.rect.collidepoint(player_center):
                    if player.rect.center != sprite.rect.center:
                        player.rect.center = sprite.rect.center
                        if Assets.debug_on:
                            #----------used for debugging only. Prints to console.----------#
                            print("player captured by grid_snap") 

#---------- Handles key item collection and door unlocks. ----------#
    def key_collect(self):
        player = self.player.sprite
        for sprite in self.yellowkey.sprites():
            if sprite.rect.colliderect(player.rect):
                for item in level_assets[Assets.lvl]:
                    if item.get('item') == 'yellowkey':
                        Level.yellowunlocked = True
                sprite.kill()
        for sprite in self.bluekey.sprites():
            if sprite.rect.colliderect(player.rect):
                for item in level_assets[Assets.lvl]:
                    if item.get('item') == 'bluekey':
                        Level.blueunlocked = True
                sprite.kill()
        for sprite in self.redkey.sprites():
            if sprite.rect.colliderect(player.rect):
                for item in level_assets[Assets.lvl]:
                    if item.get('item') == 'redkey':
                        Level.redunlocked = True
                sprite.kill()   

#---------- Handle teleport items ----------#
    def teleport(self):
        player = self.player.sprite
        px,py = player.rect.center
        self.check_port_lock(px,py)
        for sprite in self.ports:
            if not Assets.port_locked:
                if sprite.rect.collidepoint(px,py):
                    target = sprite.target
                    newx,newy = self.get_port(target)
                    player.rect.center = (newx, newy)
                    Assets.port_locked = True 

    def check_port_lock(self,x,y):
        for sprite in self.ports:
            if sprite.rect.collidepoint(x,y): # If the player touches any ports, remain locked
                return
        Assets.port_locked = False # if player is not in contact with any teleports, this will be reached

    def get_port(self, target):
        for sprite in self.ports:
            if sprite.id == target:
                newx,newy = sprite.rect.center
                return newx,newy
                    

#---------- Handles level end. Called in main loop and triggers level advancement ----------#         
    def checkwin(self):        
        player = self.player.sprite
        for sprite in self.target.sprites():
             if sprite.rect.colliderect(player.rect):
                sprite.kill()
                return True

    def move_mask(self):
        if Level.mask:
            player = self.player.sprite
            player_pos = player.rect.center
            self.drawmask.update_mask(player_pos)

#---------- Refresh level map when called. Prevents this being required every cycle ----------#
    def print_level(self):
        self.map_surface = pygame.surface.Surface((Assets.width,Assets.height))
        self.map_surface.blit(self.wall_image,(0,0))
        self.boundary.draw(self.map_surface)
        self.grass.draw(self.map_surface)
        self.path.draw(self.map_surface)
        self.target.draw(self.map_surface)
        self.ports.draw(self.map_surface)

#---------- Called once per loop and activates level elements. ----------#
    def run(self,mouse_x, mouse_y, event_list):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list
        self.display_surface.blit(self.map_surface,(0,0))
        self.hud.display_hud(self.display_surface,self.event_list,self.mouse_x, self.mouse_y)
        self.yellowkey.draw(self.display_surface)
        self.bluekey.draw(self.display_surface)
        self.redkey.draw(self.display_surface)
        self.yellowdoor.draw(self.display_surface)
        self.bluedoor.draw(self.display_surface)
        self.reddoor.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        
        self.key_collect()
        self.teleport()
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.enemy_movement()
        self.enemy_collision()
        self.grid_snap()
        self.player.draw(self.display_surface)
        self.move_mask()
        Assets.music.game_music()
        if Assets.game_menu:
            Assets.popmenu.open_menu(self.mouse_x,self.mouse_y,self.event_list) 
        if Assets.savemenu:
            Assets.savegame.save_popup(self.mouse_x,self.mouse_y,self.event_list)
    

        