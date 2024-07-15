import pygame
from maps import *
from gameplay import Level
from assets import *

class Overworld:

    page = 0
    max_page = None


    def __init__(self,surface,mouse_x,mouse_y,event_list):
        self.display_surface = surface
        Overworld.max_page = len(level_list) // 9 + 1
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list
        self.open_overworld()
        self.bg_image_load = pygame.image.load('Maze/img/game_background.jpg').convert()
        self.refresh_bg_image()
        self.nav_font = pygame.font.Font(None, 50)

        self.back_off = pygame.image.load('Maze/img/back.png')
        self.back_off.set_colorkey('#000000')
        self.back_on = pygame.image.load('Maze/img/back_o.png')
        self.back_on.set_colorkey('#000000')
        self.btn_back_rect = self.back_off.get_rect(center = (Assets.width/2,Assets.height/2 + 300))
        self.btn_back_mouseover = False

        self.nav_back_off = pygame.image.load('Maze/img/btn_back.png').convert()
        self.nav_back_off.set_colorkey('#000000')
        self.nav_back_on = pygame.image.load('Maze/img/btn_back_o.png').convert()
        self.nav_back_on.set_colorkey('#000000')        
        self.nav_back_rect = self.nav_back_off.get_rect(center = (Assets.width/2 - 545, Assets.height/2-30))
        self.nav_back_mouseover = False

        self.nav_next_off = pygame.image.load('Maze/img/btn_next.png').convert()
        self.nav_next_off.set_colorkey('#000000')
        self.nav_next_on = pygame.image.load('Maze/img/btn_next_o.png').convert()
        self.nav_next_on.set_colorkey('#000000')
        self.nav_next_rect = self.nav_next_off.get_rect(center = (Assets.width/2 + 545, Assets.height/2-30))
        self.nav_next_mouseover = False
    def refresh_bg_image(self):
        self.bg_image = pygame.transform.scale(self.bg_image_load,(Assets.width,Assets.height))

    def background(self):
        self.display_surface.blit(self.bg_image,(0,0))     

    def open_overworld(self):
        Overworld.page = (Assets.lvl // 9)
        self.redraw_tiles()

    def redraw_tiles(self):

        self.loading_font = pygame.font.Font(None, 100)
        self.loading_text = self.loading_font.render("Loading...",False,'White')
        self.loading_rect = self.loading_text.get_rect(center = (Assets.width/2, Assets.height/2))

        self.tile_1 = pygame.sprite.GroupSingle()
        self.tile_2 = pygame.sprite.GroupSingle()
        self.tile_3 = pygame.sprite.GroupSingle()
        self.tile_4 = pygame.sprite.GroupSingle()
        self.tile_5 = pygame.sprite.GroupSingle()
        self.tile_6 = pygame.sprite.GroupSingle()
        self.tile_7 = pygame.sprite.GroupSingle()
        self.tile_8 = pygame.sprite.GroupSingle()
        self.tile_9 = pygame.sprite.GroupSingle()

        for item in overworld_tiles:
            if item.get('page') == Overworld.page:
                self.x = Assets.width/2 + item.get('location_x')
                self.y = Assets.height/2 + item.get('location_y')
                self.path = item.get('path')
                self.level = item.get('level')

                if Assets.max_level >= self.level:
                    unlocked = True
                else:
                    unlocked = False

                tile = DrawTile((self.x,self.y),self.path,unlocked)
                if self.level % 9 == 1:
                    self.tile_1.add(tile)
                if self.level % 9 == 2:
                    self.tile_2.add(tile)
                if self.level % 9 == 3:
                    self.tile_3.add(tile)
                if self.level % 9 == 4:
                    self.tile_4.add(tile)
                if self.level % 9 == 5:
                    self.tile_5.add(tile)
                if self.level % 9 == 6:
                    self.tile_6.add(tile)
                if self.level % 9== 7:
                    self.tile_7.add(tile)
                if self.level % 9 == 8:
                    self.tile_8.add(tile)
                if self.level % 9 == 0:
                    self.tile_9.add(tile)
    
    def draw_nav(self):

        
        if self.nav_back_rect.collidepoint(self.mouse_x,self.mouse_y):
            self.nav_back_mouseover = True
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP and Overworld.page > 0:
                    Overworld.page -= 1
                    Assets.sfx.click()
                    self.redraw_tiles()
        else:
            self.nav_back_mouseover = False

        if self.nav_next_rect.collidepoint(self.mouse_x, self.mouse_y):
            self.nav_next_mouseover = True
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if Overworld.page < Overworld.max_page - 1:
                        Overworld.page += 1
                        Assets.sfx.click()
                        self.redraw_tiles()
        else:
            self.nav_next_mouseover = False

        if self.btn_back_rect.collidepoint(self.mouse_x, self.mouse_y):
            self.btn_back_mouseover = True
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if Assets.gamestate == "overworld":
                        Assets.sfx.click()
                        Assets.gamestate = "menu"
        else:
            self.btn_back_mouseover = False

        if self.btn_back_mouseover:
            self.display_surface.blit(self.back_on,self.btn_back_rect)
        else:
            self.display_surface.blit(self.back_off,self.btn_back_rect)  
        
        if self.nav_back_mouseover:
            self.display_surface.blit(self.nav_back_on,self.nav_back_rect)
        else:                     
            self.display_surface.blit(self.nav_back_off,self.nav_back_rect)

        if self.nav_next_mouseover:
            self.display_surface.blit(self.nav_next_on,self.nav_next_rect)
        else:                     
            self.display_surface.blit(self.nav_next_off,self.nav_next_rect)

    def check_clicks(self):
        for sprite in self.tile_1.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 1:
                            Assets.lvl = (9 * Overworld.page) + 1
                            self.clicked()
        for sprite in self.tile_2.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 2:
                            Assets.lvl = (9 * Overworld.page) + 2
                            self.clicked()    
        for sprite in self.tile_3.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 3:
                            Assets.lvl = (9 * Overworld.page) + 3
                            self.clicked()
        for sprite in self.tile_4.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 4:
                            Assets.lvl = (9 * Overworld.page) + 4
                            self.clicked()
        for sprite in self.tile_5.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 5:
                            Assets.lvl = (9 * Overworld.page) + 5
                            self.clicked()
        for sprite in self.tile_6.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 6:
                            Assets.lvl = (9 * Overworld.page) + 6
                            self.clicked()
        for sprite in self.tile_7.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 7:
                            Assets.lvl = (9 * Overworld.page) + 7
                            self.clicked()
        for sprite in self.tile_8.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 8:
                            Assets.lvl = (9 * Overworld.page) + 8
                            self.clicked()
        for sprite in self.tile_9.sprites():
             if sprite.rect.collidepoint(self.mouse_x,self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Assets.max_level >= (9 * Overworld.page) + 9:
                            Assets.lvl = (9 * Overworld.page) + 9
                            self.clicked()
        

    def clicked(self):
        self.display_surface.fill('#000000')
        Assets.sfx.click()
        self.loading_rect = self.loading_text.get_rect(center = (Assets.width/2,Assets.height/2))
        self.display_surface.blit(self.loading_text,self.loading_rect)
        pygame.display.update()
        Assets.map = Level(level_list.get(Assets.lvl), level_assets[Assets.lvl], self.display_surface)
        Assets.map.print_level()
        Assets.gamestate = "gameplay"
        Assets.music.start_game_music()
    
    def run(self,mouse_x,mouse_y,event_list):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list
        self.background()
        self.draw_nav()
        
        self.tile_1.draw(self.display_surface)
        self.tile_2.draw(self.display_surface)
        self.tile_3.draw(self.display_surface)
        self.tile_4.draw(self.display_surface)
        self.tile_5.draw(self.display_surface)
        self.tile_6.draw(self.display_surface)
        self.tile_7.draw(self.display_surface)
        self.tile_8.draw(self.display_surface)
        self.tile_9.draw(self.display_surface)
        self.check_clicks()

class DrawTile(pygame.sprite.Sprite):
    def __init__(self,pos,path,unlocked):
        super().__init__() 
        if unlocked:     
            self.image = pygame.image.load(f'{path}').convert()
        else:
            self.image = pygame.image.load(f'{path}').convert_alpha()
            self.image.set_alpha(150)
        self.rect = self.image.get_rect(center = pos)