import pygame
from assets import *
from gameplay import *
from overworld import *
from sfx import Slider
from savegame import Savegame



class Menu:

    def __init__(self,surface,mouse_x,mouse_y,event_list):
        self.origin_x, self.origin_y = 0,0
        self.display_surface = surface
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list
        self.bg_image_load = pygame.image.load('Maze/img/game_background.jpg').convert()
        self.refresh_bg_image()
        self.title = pygame.image.load('Maze/img/title.png').convert()
        self.title.set_colorkey('#000000')
        self.title_rect = self.title.get_rect(center = (Assets.width/2,150))

        self.divider = pygame.image.load('Maze/img/divider.png').convert()
        self.divider.set_colorkey('#000000')
        self.divider_rect = self.divider.get_rect(center = (Assets.width/2, 450))
        
        self.start_off = pygame.image.load('Maze/img/continue.png')
        self.start_off.set_colorkey('#000000')
        self.start_on = pygame.image.load('Maze/img/continue_o.png')
        self.start_on.set_colorkey('#000000')
        self.btn_start_rect = self.start_off.get_rect(center = (Assets.width/2,Assets.height/2 - 60))
        self.btn_start_mouseover = False

        self.new_off = pygame.image.load('Maze/img/newgame.png')
        self.new_off.set_colorkey('#000000')
        self.new_on = pygame.image.load('Maze/img/newgame_o.png')
        self.new_on.set_colorkey('#000000')
        self.btn_new_rect = self.new_off.get_rect(center = (Assets.width/2,Assets.height/2))
        self.btn_new_mouseover = False

        self.settings_off = pygame.image.load('Maze/img/settings.png')
        self.settings_off.set_colorkey('#000000')
        self.settings_on = pygame.image.load('Maze/img/settings_o.png')
        self.settings_on.set_colorkey('#000000')
        self.btn_settings_rect = self.settings_off.get_rect(center = (Assets.width/2,Assets.height/2 + 60))
        self.btn_settings_mouseover = False

        self.save_off = pygame.image.load('Maze/img/savegame.png')
        self.save_off.set_colorkey('#000000')
        self.save_on = pygame.image.load('Maze/img/savegame_o.png')
        self.save_on.set_colorkey('#000000')
        self.btn_save_rect = self.save_off.get_rect(center = (Assets.width/2,Assets.height/2 + 120))
        self.btn_save_mouseover = False

        self.load_off = pygame.image.load('Maze/img/loadgame.png')
        self.load_off.set_colorkey('#000000')
        self.load_on = pygame.image.load('Maze/img/loadgame_o.png')
        self.load_on.set_colorkey('#000000')
        self.btn_load_rect = self.load_off.get_rect(center = (Assets.width/2,Assets.height/2 + 180))
        self.btn_load_mouseover = False

        self.back_off = pygame.image.load('Maze/img/back.png')
        self.back_off.set_colorkey('#000000')
        self.back_on = pygame.image.load('Maze/img/back_o.png')
        self.back_on.set_colorkey('#000000')
        self.btn_back_rect = self.back_off.get_rect(center = (Assets.width/2,640))
        self.btn_back_mouseover = False

        self.fullscreen_off = pygame.image.load('Maze/img/full_screen.png')
        self.fullscreen_off.set_colorkey('#000000')
        self.fullscreen_on = pygame.image.load('Maze/img/full_screen_o.png')
        self.fullscreen_on.set_colorkey('#000000')
        self.fullscreen_rect = self.fullscreen_off.get_rect(center = (Assets.width*0.75 - 130 ,280))
        self.fullscreen_mouseover = False

        self.windowed_off = pygame.image.load('Maze/img/windowed.png')
        self.windowed_off.set_colorkey('#000000')
        self.windowed_on = pygame.image.load('Maze/img/windowed_o.png')
        self.windowed_on.set_colorkey('#000000')
        self.windowed_rect = self.windowed_off.get_rect(center = (Assets.width*0.75 + 130 ,280))
        self.windowed_mouseover = False

        self.music_label = pygame.image.load('Maze/img/music_volume_label.png').convert_alpha()
        self.music_label.set_colorkey('#000000')
        self.music_label_rect = self.music_label.get_rect(center = (Assets.width * 0.25,280))  
        self.sfx_label = pygame.image.load('Maze/img/sfx_volume_label.png').convert_alpha()
        self.sfx_label.set_colorkey('#000000')
        self.sfx_label_rect = self.sfx_label.get_rect(center = (Assets.width * 0.25 ,380)) 
        self.origin_x,self.origin_y = Assets.width * 0.25 - 160,270
        self.maze_wall = pygame.image.load('Maze/img/maze_walls_label.png').convert_alpha()
        self.maze_wall.set_colorkey('#000000')
        self.maze_wall_rect = self.maze_wall.get_rect(center = (self.origin_x + 160,self.origin_y + 210))  
        self.player_icon = pygame.image.load('Maze/img/player_icon_label.png').convert_alpha()
        self.player_icon.set_colorkey('#000000')
        self.player_icon_rect = self.player_icon.get_rect(center = (self.origin_x + 160,self.origin_y + 300))        

        self.activedot = pygame.image.load('Maze/img/dot_active.png').convert_alpha()
        self.activedot.set_colorkey('#000000')
        self.purpdot = pygame.image.load('Maze/img/player_0.png').convert_alpha()
        self.purpdot.set_colorkey('#000000')
        self.reddot = pygame.image.load('Maze/img/player_1.png').convert_alpha()
        self.reddot.set_colorkey('#000000')
        self.greendot = pygame.image.load('Maze/img/player_2.png').convert_alpha()
        self.greendot.set_colorkey('#000000')
        self.pinkdot = pygame.image.load('Maze/img/player_3.png').convert_alpha()
        self.pinkdot.set_colorkey('#000000')
        self.bluedot = pygame.image.load('Maze/img/player_4.png').convert_alpha()
        self.bluedot.set_colorkey('#000000')
        self.ltbluedot = pygame.image.load('Maze/img/player_5.png').convert_alpha()
        self.ltbluedot.set_colorkey('#000000')
        self.orangedot = pygame.image.load('Maze/img/player_6.png').convert_alpha()
        self.orangedot.set_colorkey('#000000')

    
        self.purpdotwalls_rect = self.purpdot.get_rect(topleft = (self.origin_x + 55, self.origin_y + 230))
        self.reddotwalls_rect = self.reddot.get_rect(topleft = (self.origin_x + 85, self.origin_y + 230))
        self.greendotwalls_rect = self.greendot.get_rect(topleft = (self.origin_x + 115, self.origin_y + 230))
        self.pinkdotwalls_rect = self.pinkdot.get_rect(topleft = (self.origin_x + 145, self.origin_y + 230))
        self.bluedotwalls_rect = self.bluedot.get_rect(topleft = (self.origin_x + 175, self.origin_y + 230))
        self.ltbluedotwalls_rect = self.ltbluedot.get_rect(topleft = (self.origin_x + 205, self.origin_y + 230))
        self.orangedotwalls_rect = self.orangedot.get_rect(topleft = (self.origin_x + 235, self.origin_y + 230))
        self.update_active_color("walls",Assets.img_set)

        self.purpdotplayer_rect = self.purpdot.get_rect(topleft = (self.origin_x + 55, self.origin_y + 320))
        self.reddotplayer_rect = self.reddot.get_rect(topleft = (self.origin_x + 85, self.origin_y + 320))
        self.greendotplayer_rect = self.greendot.get_rect(topleft = (self.origin_x + 115, self.origin_y + 320))
        self.pinkdotplayer_rect = self.pinkdot.get_rect(topleft = (self.origin_x + 145, self.origin_y + 320))
        self.bluedotplayer_rect = self.bluedot.get_rect(topleft = (self.origin_x + 175, self.origin_y + 320))
        self.ltbluedotplayer_rect = self.ltbluedot.get_rect(topleft = (self.origin_x + 205, self.origin_y + 320))
        self.orangedotplayer_rect = self.orangedot.get_rect(topleft = (self.origin_x + 235, self.origin_y + 320))
        self.update_active_color("icon",Assets.player_icon)
#background for all home menu screens           

    def refresh_bg_image(self):
        self.bg_image = pygame.transform.scale(self.bg_image_load,(Assets.width,Assets.height))

    def background(self):
        self.display_surface.blit(self.bg_image,(0,0))
        self.display_surface.blit(self.title,self.title_rect)

#title menu screen
    def main_menu(self):
        self.background()
        self.skip = 0
#start game button display and functionality
        if not Assets.savemenu and not Assets.loadmenu:
            
            if self.btn_start_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_start_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.gamestate = "overworld"
                        Assets.overworld.open_overworld()
                        Assets.overworld.redraw_tiles()
                        Assets.sfx.click()
            else:
                self.btn_start_mouseover = False   

            if self.btn_new_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_new_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        if Assets.max_level > 1 and Assets.newgame == 0:
                            message1 = "Are you sure you want to start a new game?"
                            message2 = "Unsaved progress will be lost!"
                            if Assets.message.prompt_double(message1,message2):
                                Assets.lvl = 1
                                Assets.max_level = 1
                                Assets.gamestate = "overworld"
                                Assets.overworld.open_overworld()
                                Assets.overworld.redraw_tiles()
                                Assets.newgame = 1
                                self.skip = 1
                            else:
                                self.skip = 1
                        else:
                            Assets.lvl = 1
                            Assets.max_level = 1
                            Assets.gamestate = "overworld"
                            Assets.overworld.open_overworld()
                            Assets.overworld.redraw_tiles()
                        
            else:
                self.btn_new_mouseover = False   
                    
            if self.btn_settings_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_settings_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP and self.skip == 0:
                        Assets.gamestate = "settings"
                        Assets.sfx.click()
            else:
                self.btn_settings_mouseover = False

            if self.btn_save_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_save_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.savemenu = True
                        Savegame.cycles = 0
                        Assets.sfx.click()
            else:
                self.btn_save_mouseover = False

            if self.btn_load_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_load_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.loadmenu = True
                        Savegame.cycles = 0
                        Assets.sfx.click()
            else:
                self.btn_load_mouseover = False

#print buttons onto menu
        if Assets.gamestate == "menu":
            
            if Assets.newgame != 1:
                if self.btn_start_mouseover:
                    self.display_surface.blit(self.start_on,self.btn_start_rect)
                else:
                    self.display_surface.blit(self.start_off,self.btn_start_rect)     
            
            if self.btn_new_mouseover:
                self.display_surface.blit(self.new_on,self.btn_new_rect)
            else:
                self.display_surface.blit(self.new_off,self.btn_new_rect)

            if self.btn_settings_mouseover:
                self.display_surface.blit(self.settings_on,self.btn_settings_rect)
            else:
                self.display_surface.blit(self.settings_off,self.btn_settings_rect)

            if self.btn_save_mouseover:
                self.display_surface.blit(self.save_on,self.btn_save_rect)
            else:
                self.display_surface.blit(self.save_off,self.btn_save_rect)

            if self.btn_load_mouseover:
                self.display_surface.blit(self.load_on,self.btn_load_rect)
            else:
                self.display_surface.blit(self.load_off,self.btn_load_rect)
    
    
    def settings_menu(self):
        self.background()
        self.display_surface.blit(self.divider,self.divider_rect)
        self.col_1_x = Assets.width * 0.25 - 115
        self.col_2_x = Assets.width * 0.75 - 115
        self.display_surface.blit(self.music_label, self.music_label_rect)
        Assets.music_slider.draw_slider(Assets.music_volume,self.col_1_x,300,self.display_surface)
        Assets.music_slider.check_clicks('music',self.mouse_x,self.mouse_y,self.event_list)

        self.display_surface.blit(self.sfx_label, self.sfx_label_rect)
        Assets.sfx_slider.draw_slider(Assets.sfx_volume,self.col_1_x,400,self.display_surface)
        Assets.sfx_slider.check_clicks('sfx',self.mouse_x,self.mouse_y,self.event_list)  

        self.check_clicks()

        self.display_surface.blit(self.maze_wall, self.maze_wall_rect)
        self.display_surface.blit(self.purpdot,self.purpdotwalls_rect)
        self.display_surface.blit(self.reddot,self.reddotwalls_rect)
        self.display_surface.blit(self.greendot,self.greendotwalls_rect)
        self.display_surface.blit(self.pinkdot,self.pinkdotwalls_rect)
        self.display_surface.blit(self.bluedot,self.bluedotwalls_rect)
        self.display_surface.blit(self.ltbluedot,self.ltbluedotwalls_rect)
        self.display_surface.blit(self.orangedot,self.orangedotwalls_rect)
        self.display_surface.blit(self.activedot,self.activeset_rect)

        self.display_surface.blit(self.player_icon, self.player_icon_rect)
        self.display_surface.blit(self.purpdot,self.purpdotplayer_rect)
        self.display_surface.blit(self.reddot,self.reddotplayer_rect)
        self.display_surface.blit(self.greendot,self.greendotplayer_rect)
        self.display_surface.blit(self.pinkdot,self.pinkdotplayer_rect)
        self.display_surface.blit(self.bluedot,self.bluedotplayer_rect)
        self.display_surface.blit(self.ltbluedot,self.ltbluedotplayer_rect)
        self.display_surface.blit(self.orangedot,self.orangedotplayer_rect)
        self.display_surface.blit(self.activedot,self.activeicon_rect)
        
        if self.btn_back_mouseover:
            self.display_surface.blit(self.back_on,self.btn_back_rect)
        else:
            self.display_surface.blit(self.back_off,self.btn_back_rect)

        if self.fullscreen_mouseover:
            self.display_surface.blit(self.fullscreen_on,self.fullscreen_rect)
        elif Assets.fullscreen:
            self.display_surface.blit(self.fullscreen_on,self.fullscreen_rect)
        else:
            self.display_surface.blit(self.fullscreen_off,self.fullscreen_rect)

        if self.windowed_mouseover:
            self.display_surface.blit(self.windowed_on,self.windowed_rect)
        elif not Assets.fullscreen:
            self.display_surface.blit(self.windowed_on,self.windowed_rect)
        else:
            self.display_surface.blit(self.windowed_off,self.windowed_rect)

    def check_clicks(self):
        if self.purpdotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",0)
                    Assets.sfx.click()
        if self.reddotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",1)
                    Assets.sfx.click()
        if self.greendotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",2) 
                    Assets.sfx.click()
        if self.pinkdotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",3)
                    Assets.sfx.click()
        if self.bluedotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",4)
                    Assets.sfx.click()
        if self.ltbluedotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",5)
                    Assets.sfx.click()
        if self.orangedotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("walls",6)
                    Assets.sfx.click()

        if self.purpdotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",0)
                    Assets.sfx.click()
        if self.reddotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",1)
                    Assets.sfx.click()
        if self.greendotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",2) 
                    Assets.sfx.click()
        if self.pinkdotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",3)
                    Assets.sfx.click()
        if self.bluedotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",4) 
                    Assets.sfx.click()   
        if self.ltbluedotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",5) 
                    Assets.sfx.click()
        if self.orangedotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_active_color("icon",6) 
                    Assets.sfx.click() 
        
        if self.btn_back_rect.collidepoint(self.mouse_x, self.mouse_y):
            self.btn_back_mouseover = True
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    Assets.gamestate = "menu"
                    Assets.sfx.click()
        else:
            self.btn_back_mouseover = False
        
        if self.fullscreen_rect.collidepoint(self.mouse_x, self.mouse_y):
            self.fullscreen_mouseover = True
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    Assets.sfx.click()
                    if not Assets.fullscreen:
                        Assets.toggle = True
        else:
            self.fullscreen_mouseover = False

        if self.windowed_rect.collidepoint(self.mouse_x, self.mouse_y):
            self.windowed_mouseover = True
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    Assets.sfx.click()
                    if Assets.fullscreen:
                        Assets.toggle = True
        else:
            self.windowed_mouseover = False
    
    def update_active_color(self,type,num):
        
        self.type = type
        self.num = num
        if self.type == "walls":
            Assets.img_set = num
            if Assets.img_set == 0:
                self.posx,self.posy = self.purpdotwalls_rect.center
            if Assets.img_set == 1:
                self.posx,self.posy = self.reddotwalls_rect.center
            if Assets.img_set == 2:
                self.posx,self.posy = self.greendotwalls_rect.center
            if Assets.img_set == 3:
                self.posx,self.posy = self.pinkdotwalls_rect.center
            if Assets.img_set == 4:
                self.posx,self.posy = self.bluedotwalls_rect.center
            if Assets.img_set == 5:
                self.posx,self.posy = self.ltbluedotwalls_rect.center
            if Assets.img_set == 6:
                self.posx,self.posy = self.orangedotwalls_rect.center
            self.activeset_rect = self.activedot.get_rect(center = (self.posx,self.posy))
            Assets.prompt = True

        if self.type == "icon":
            Assets.player_icon = num
            if Assets.player_icon == 0:
                self.posx,self.posy = self.purpdotplayer_rect.center
            if Assets.player_icon == 1:
                self.posx,self.posy = self.reddotplayer_rect.center
            if Assets.player_icon == 2:
                self.posx,self.posy = self.greendotplayer_rect.center
            if Assets.player_icon == 3:
                self.posx,self.posy = self.pinkdotplayer_rect.center
            if Assets.player_icon == 4:
                self.posx,self.posy = self.bluedotplayer_rect.center
            if Assets.player_icon == 5:
                self.posx,self.posy = self.ltbluedotplayer_rect.center
            if Assets.player_icon == 6:
                self.posx,self.posy = self.orangedotplayer_rect.center
            self.activeicon_rect = self.activedot.get_rect(center = (self.posx,self.posy))
            Assets.prompt = True
#determine which menu screen to open
    def run(self,mouse_x,mouse_y,event_list):

        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list

        if Assets.gamestate == "settings":
            self.settings_menu()
        else:
            self.main_menu()
            if Assets.savemenu:
                Assets.savegame.save_popup(self.mouse_x,self.mouse_y,self.event_list)
            if Assets.loadmenu:
                Assets.savegame.load_popup(self.mouse_x,self.mouse_y,self.event_list)
            
class Popmenu:

    def __init__(self,surface,mouse_x,mouse_y,event_list):
        self.display_surface = surface
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list
        self.container = pygame.image.load('Maze/img/popup_bg.png').convert_alpha()
        self.container_rect = self.container.get_rect(center = (Assets.width/2,Assets.height/2))
        self.load_buttons()
        Assets.music_slider = Slider()
        Assets.sfx_slider = Slider()

    def load_buttons(self):
        self.origin_x, self.origin_y = self.container_rect.topleft
        self.resume_off = pygame.image.load('Maze/img/resume.png').convert_alpha()
        self.resume_off.set_colorkey('#000000')
        self.resume_on = pygame.image.load('Maze/img/resume_o.png').convert_alpha()
        self.resume_on.set_colorkey('#000000')
        self.resume_rect = self.resume_off.get_rect(center = (self.origin_x + 145,self.origin_y + 90)) 
        self.resume_mouseover = False 
        self.restart_off = pygame.image.load('Maze/img/restart.png').convert_alpha()
        self.restart_off.set_colorkey('#000000')
        self.restart_on = pygame.image.load('Maze/img/restart_o.png').convert_alpha()
        self.restart_on.set_colorkey('#000000')
        self.restart_rect = self.restart_off.get_rect(center = (self.origin_x + 145,self.origin_y + 165))  
        self.restart_mouseover = False
        self.settings_off = pygame.image.load('Maze/img/settings.png').convert_alpha()
        self.settings_off.set_colorkey('#000000')
        self.settings_on = pygame.image.load('Maze/img/settings_o.png').convert_alpha()
        self.settings_on.set_colorkey('#000000')
        self.settings_rect = self.settings_off.get_rect(center = (self.origin_x + 145,self.origin_y + 240)) 
        self.settings_mouseover = False
        self.save_off = pygame.image.load('Maze/img/savegame.png').convert_alpha()
        self.save_off.set_colorkey('#000000')
        self.save_on = pygame.image.load('Maze/img/savegame_o.png').convert_alpha()
        self.save_on.set_colorkey('#000000')
        self.save_rect = self.save_off.get_rect(center = (self.origin_x + 145,self.origin_y + 315)) 
        self.save_mouseover = False
        self.quit_off = pygame.image.load('Maze/img/menu.png').convert_alpha()
        self.quit_off.set_colorkey('#000000')
        self.quit_on = pygame.image.load('Maze/img/menu_o.png').convert_alpha()
        self.quit_on.set_colorkey('#000000')
        self.quit_rect = self.quit_off.get_rect(center = (self.origin_x + 145,self.origin_y + 390))
        self.quit_mouseover = False
        self.back_off = pygame.image.load('Maze/img/back.png').convert_alpha()
        self.back_off.set_colorkey('#000000')
        self.back_on = pygame.image.load('Maze/img/back_o.png').convert_alpha()
        self.back_on.set_colorkey('#000000')
        self.back_rect = self.back_off.get_rect(center = (self.origin_x + 145,self.origin_y + 410))
        self.back_mouseover = False
        self.font = pygame.font.Font(None, 24)
        self.text1 = self.font.render("To apply colour changes,",False,'red')
        self.text2 = self.font.render("restart or complete the level",False,'red')
        self.textrect1 = self.text1.get_rect(center = (self.origin_x + 155,self.origin_y + 340))
        self.textrect2 = self.text2.get_rect(center = (self.origin_x + 155,self.origin_y + 355))

        self.music_label = pygame.image.load('Maze/img/music_volume_label.png').convert_alpha()
        self.music_label.set_colorkey('#000000')
        self.music_label_rect = self.music_label.get_rect(center = (self.origin_x + 160,self.origin_y + 60))  
        self.sfx_label = pygame.image.load('Maze/img/sfx_volume_label.png').convert_alpha()
        self.sfx_label.set_colorkey('#000000')
        self.sfx_label_rect = self.sfx_label.get_rect(center = (self.origin_x + 160,self.origin_y + 135))  
        self.maze_wall = pygame.image.load('Maze/img/maze_walls_label.png').convert_alpha()
        self.maze_wall.set_colorkey('#000000')
        self.maze_wall_rect = self.maze_wall.get_rect(center = (self.origin_x + 160,self.origin_y + 210))  
        self.player_icon = pygame.image.load('Maze/img/player_icon_label.png').convert_alpha()
        self.player_icon.set_colorkey('#000000')
        self.player_icon_rect = self.player_icon.get_rect(center = (self.origin_x + 160,self.origin_y + 280))        

        self.activedot = pygame.image.load('Maze/img/dot_active.png').convert_alpha()
        self.activedot.set_colorkey('#000000')
        self.purpdot = pygame.image.load('Maze/img/player_0.png').convert_alpha()
        self.purpdot.set_colorkey('#000000')
        self.reddot = pygame.image.load('Maze/img/player_1.png').convert_alpha()
        self.reddot.set_colorkey('#000000')
        self.greendot = pygame.image.load('Maze/img/player_2.png').convert_alpha()
        self.greendot.set_colorkey('#000000')
        self.pinkdot = pygame.image.load('Maze/img/player_3.png').convert_alpha()
        self.pinkdot.set_colorkey('#000000')
        self.bluedot = pygame.image.load('Maze/img/player_4.png').convert_alpha()
        self.bluedot.set_colorkey('#000000')
        self.ltbluedot = pygame.image.load('Maze/img/player_5.png').convert_alpha()
        self.ltbluedot.set_colorkey('#000000')
        self.orangedot = pygame.image.load('Maze/img/player_6.png').convert_alpha()
        self.orangedot.set_colorkey('#000000')

    
        self.purpdotwalls_rect = self.purpdot.get_rect(topleft = (self.origin_x + 55, self.origin_y + 230))
        self.reddotwalls_rect = self.reddot.get_rect(topleft = (self.origin_x + 85, self.origin_y + 230))
        self.greendotwalls_rect = self.greendot.get_rect(topleft = (self.origin_x + 115, self.origin_y + 230))
        self.pinkdotwalls_rect = self.pinkdot.get_rect(topleft = (self.origin_x + 145, self.origin_y + 230))
        self.bluedotwalls_rect = self.bluedot.get_rect(topleft = (self.origin_x + 175, self.origin_y + 230))
        self.ltbluedotwalls_rect = self.ltbluedot.get_rect(topleft = (self.origin_x + 205, self.origin_y + 230))
        self.orangedotwalls_rect = self.orangedot.get_rect(topleft = (self.origin_x + 235, self.origin_y + 230))
        self.update_active_color("walls",Assets.img_set)

        self.purpdotplayer_rect = self.purpdot.get_rect(topleft = (self.origin_x + 55, self.origin_y + 300))
        self.reddotplayer_rect = self.reddot.get_rect(topleft = (self.origin_x + 85, self.origin_y + 300))
        self.greendotplayer_rect = self.greendot.get_rect(topleft = (self.origin_x + 115, self.origin_y + 300))
        self.pinkdotplayer_rect = self.pinkdot.get_rect(topleft = (self.origin_x + 145, self.origin_y + 300))
        self.bluedotplayer_rect = self.bluedot.get_rect(topleft = (self.origin_x + 175, self.origin_y + 300))
        self.ltbluedotplayer_rect = self.ltbluedot.get_rect(topleft = (self.origin_x + 205, self.origin_y + 300))
        self.orangedotplayer_rect = self.orangedot.get_rect(topleft = (self.origin_x + 235, self.origin_y + 300))
        self.update_active_color("icon",Assets.player_icon)
        
        Assets.prompt = False

    def update_active_color(self,type,num):
        
        self.type = type
        self.num = num
        if self.type == "walls":
            Assets.img_set = num
            if Assets.img_set == 0:
                self.posx,self.posy = self.purpdotwalls_rect.center
            if Assets.img_set == 1:
                self.posx,self.posy = self.reddotwalls_rect.center
            if Assets.img_set == 2:
                self.posx,self.posy = self.greendotwalls_rect.center
            if Assets.img_set == 3:
                self.posx,self.posy = self.pinkdotwalls_rect.center
            if Assets.img_set == 4:
                self.posx,self.posy = self.bluedotwalls_rect.center
            if Assets.img_set == 5:
                self.posx,self.posy = self.ltbluedotwalls_rect.center
            if Assets.img_set == 6:
                self.posx,self.posy = self.orangedotwalls_rect.center
            self.activeset_rect = self.activedot.get_rect(center = (self.posx,self.posy))
            Assets.prompt = True

        if self.type == "icon":
            Assets.player_icon = num
            if Assets.player_icon == 0:
                self.posx,self.posy = self.purpdotplayer_rect.center
            if Assets.player_icon == 1:
                self.posx,self.posy = self.reddotplayer_rect.center
            if Assets.player_icon == 2:
                self.posx,self.posy = self.greendotplayer_rect.center
            if Assets.player_icon == 3:
                self.posx,self.posy = self.pinkdotplayer_rect.center
            if Assets.player_icon == 4:
                self.posx,self.posy = self.bluedotplayer_rect.center
            if Assets.player_icon == 5:
                self.posx,self.posy = self.ltbluedotplayer_rect.center
            if Assets.player_icon == 6:
                self.posx,self.posy = self.orangedotplayer_rect.center
            self.activeicon_rect = self.activedot.get_rect(center = (self.posx,self.posy))
            Assets.prompt = True

    def buttons_clicked(self):
        if Assets.popsettings:
            if self.back_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.back_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Assets.popsettings = False
                        Assets.sfx.click()
            else:
                self.back_mouseover = False

            if self.purpdotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",0)
                        Assets.sfx.click()
            if self.reddotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",1)
                        Assets.sfx.click()
            if self.greendotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",2) 
                        Assets.sfx.click()
            if self.pinkdotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",3)
                        Assets.sfx.click()
            if self.bluedotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",4)
                        Assets.sfx.click()
            if self.ltbluedotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",5)
                        Assets.sfx.click()
            if self.orangedotwalls_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("walls",6)
                        Assets.sfx.click()

            if self.purpdotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",0)
                        Assets.sfx.click()
            if self.reddotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",1)
                        Assets.sfx.click()
            if self.greendotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",2) 
                        Assets.sfx.click()
            if self.pinkdotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",3)
                        Assets.sfx.click()
            if self.bluedotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",4) 
                        Assets.sfx.click()   
            if self.ltbluedotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",5) 
                        Assets.sfx.click()
            if self.orangedotplayer_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.update_active_color("icon",6) 
                        Assets.sfx.click() 

        elif Assets.game_menu:
            if self.resume_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.resume_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.game_menu = False
                        Assets.sfx.click()
            else:
                self.resume_mouseover = False

            if self.restart_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.restart_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.game_menu = False
                        Assets.sfx.click()
                        Assets.map = Level(level_list.get(Assets.lvl), level_assets[Assets.lvl], self.display_surface)
                        Assets.map.print_level()
            else:
                self.restart_mouseover = False

            if self.settings_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.settings_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        Assets.popsettings = True
            else:
                self.settings_mouseover = False

            if self.quit_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.quit_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        Assets.gamestate = "overworld" 
                        pygame.mixer.music.fadeout(500)  
                        Assets.overworld.redraw_tiles()
                        Assets.game_menu = False  
                        Assets.music.__init__()
            else:
                self.quit_mouseover = False

            if self.save_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.save_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        Assets.game_menu = False
                        Assets.savemenu = True
                        Savegame.cycles = 0
            else:
                self.save_mouseover = False
            
    def open_menu(self,mouse_x,mouse_y,event_list):

        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list        
        self.display_surface.blit(self.container,self.container_rect)
        if Assets.popsettings:
            self.display_surface.blit(self.music_label, self.music_label_rect)
            self.musicx,self.musicy = self.origin_x + 40, self.origin_y + 80
            Assets.music_slider.draw_slider(Assets.music_volume,self.musicx,self.musicy,self.display_surface)
            Assets.music_slider.check_clicks('music',self.mouse_x,self.mouse_y,event_list)

            self.display_surface.blit(self.sfx_label, self.sfx_label_rect)
            self.sfxx,self.sfxy = self.origin_x + 40, self.origin_y + 160
            Assets.sfx_slider.draw_slider(Assets.sfx_volume,self.sfxx,self.sfxy,self.display_surface)
            Assets.sfx_slider.check_clicks('sfx',self.mouse_x,self.mouse_y,event_list)

            self.display_surface.blit(self.maze_wall, self.maze_wall_rect)
            self.display_surface.blit(self.purpdot,self.purpdotwalls_rect)
            self.display_surface.blit(self.reddot,self.reddotwalls_rect)
            self.display_surface.blit(self.greendot,self.greendotwalls_rect)
            self.display_surface.blit(self.pinkdot,self.pinkdotwalls_rect)
            self.display_surface.blit(self.bluedot,self.bluedotwalls_rect)
            self.display_surface.blit(self.ltbluedot,self.ltbluedotwalls_rect)
            self.display_surface.blit(self.orangedot,self.orangedotwalls_rect)
            self.display_surface.blit(self.activedot,self.activeset_rect)

            self.display_surface.blit(self.player_icon, self.player_icon_rect)
            self.display_surface.blit(self.purpdot,self.purpdotplayer_rect)
            self.display_surface.blit(self.reddot,self.reddotplayer_rect)
            self.display_surface.blit(self.greendot,self.greendotplayer_rect)
            self.display_surface.blit(self.pinkdot,self.pinkdotplayer_rect)
            self.display_surface.blit(self.bluedot,self.bluedotplayer_rect)
            self.display_surface.blit(self.ltbluedot,self.ltbluedotplayer_rect)
            self.display_surface.blit(self.orangedot,self.orangedotplayer_rect)
            self.display_surface.blit(self.activedot,self.activeicon_rect)
            
            if Assets.prompt:
                self.display_surface.blit(self.text1,self.textrect1)
                self.display_surface.blit(self.text2,self.textrect2)

            if self.back_mouseover:
                self.display_surface.blit(self.back_on,self.back_rect)
            else:
                self.display_surface.blit(self.back_off,self.back_rect)
       
        else:
            if self.resume_mouseover:
                self.display_surface.blit(self.resume_on, self.resume_rect)
            else:
                self.display_surface.blit(self.resume_off,self.resume_rect)

            if self.restart_mouseover:
                self.display_surface.blit(self.restart_on, self.restart_rect)
            else:
                self.display_surface.blit(self.restart_off,self.restart_rect)

            if self.settings_mouseover:
                self.display_surface.blit(self.settings_on, self.settings_rect)
            else:
                self.display_surface.blit(self.settings_off,self.settings_rect)

            if self.quit_mouseover:
                self.display_surface.blit(self.quit_on, self.quit_rect)
            else:
                self.display_surface.blit(self.quit_off,self.quit_rect)

            if self.save_mouseover:
                self.display_surface.blit(self.save_on, self.save_rect)
            else:
                self.display_surface.blit(self.save_off,self.save_rect)

        self.buttons_clicked()
