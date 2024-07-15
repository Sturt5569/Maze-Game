import pygame, sys
from assets import *
from gameplay import *
from maps import * 
from menu import Menu, Popmenu
from vfx import Fader
from sfx import Music,Sounds
from debugger import Debug
from overworld import *
from file_handler import *
from savegame import *
from messenger import Prompt


pygame.init()
screen = pygame.display.set_mode ((screen_width,screen_height))
pygame.display.set_caption('Maze')
Assets.clock = pygame.time.Clock()

#initialise loading screen
screen.fill('#000000')

loading_font = pygame.font.Font(None, 100)
loading_text = loading_font.render("Loading...",False,'White')
loading_rect = loading_text.get_rect(center = (screen_width/2, screen_height/2))
screen.blit(loading_text,loading_rect)

pygame.display.update()
settings_load() 

#----------preload all game objects to allow them to be ready to utilise.
mouse_x, mouse_y, event_list = 0,0,0
Assets.sfx = Sounds()
Assets.map = Level(level_list.get(Assets.lvl),level_assets[Assets.lvl], screen)
Assets.menu = Menu(screen,mouse_x,mouse_y,event_list)
Assets.overworld = Overworld(screen,mouse_x,mouse_y,event_list)
Assets.popmenu = Popmenu(screen,mouse_x,mouse_y,event_list)
Assets.music = Music()
Assets.debug = Debug(screen)
Assets.savegame = Savegame(screen)
Assets.message = Prompt(screen)


#----------Main game loop----------#
while True:
    Debug.tick1 = pygame.time.get_ticks()

    #----------Main Event loop----------#
    event_list = pygame.event.get()
    key = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in event_list:
        if event.type == pygame.QUIT:
            settings_save()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            settings_save()
            pygame.quit()
            sys.exit()
        if key[pygame.K_LCTRL] and key[pygame.K_LSHIFT]:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                if Assets.debug_on:
                    Assets.debug_on = False
                else:
                    Assets.debug_on = True   
        #----------toggle fullscreen----------#
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            Assets.toggle = True
        #----------function of ESC key depending on gamestate----------#
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if Assets.gamestate == "settings":
                Assets.gamestate = "menu"    
            if Assets.gamestate == "gameplay" and not Assets.game_menu:
                Assets.game_menu = True
            else:
                Assets.game_menu = False
                Assets.popsettings = False
            if Assets.gamestate == "overworld":
                Assets.gamestate = "menu"
            if Assets.savemenu:
                Assets.savemenu = False
                if Assets.gamestate == "gameplay":
                    Assets.game_menu = True
            if Assets.loadmenu:
                Assets.loadmenu = False
    #----------check whether fullscreen toggle is active and adjust display mode---------#
    if Assets.toggle:    
        if Assets.fullscreen == False:
            screen = pygame.display.set_mode ((0,0),pygame.FULLSCREEN)
            Assets.fullscreen = True
        else:
            screen = pygame.display.set_mode ((screen_width,screen_height))
            Assets.fullscreen = False   
    #----------Rescale maze and assets to or from full screen----------#
        Assets.width, Assets.height = Assets.map.define_size(screen)
        loading_rect = loading_text.get_rect(center = (Assets.width/2,Assets.height/2))
        screen.blit(loading_text,loading_rect)
        pygame.display.update()
        Assets.menu = Menu(screen,mouse_x,mouse_y,event_list)
        Assets.savegame = Savegame(screen)
        Assets.popmenu = Popmenu(screen,mouse_x,mouse_y,event_list)
        Assets.overworld = Overworld(screen,mouse_x,mouse_y,event_list)
        Assets.map = Level(level_list.get(Assets.lvl), level_assets[Assets.lvl], screen)
        Assets.message = Prompt(screen)
        if Assets.gamestate == "gameplay":
            Assets.map.print_level() #----------redraw maze to the screen
        Assets.toggle = False
#----------check gamestate and call menu or game processes----------#
    if Assets.gamestate == "menu" or Assets.gamestate == "settings":
        Assets.menu.run(mouse_x,mouse_y,event_list)
    if Assets.gamestate == "overworld":
        Assets.overworld.run(mouse_x,mouse_y,event_list)
    if Assets.gamestate == "gameplay":
        Assets.map.run(mouse_x,mouse_y,event_list) 
#----------level advance process----------#
        if Assets.map.checkwin():
            if Fader.start_fadeout == False:
                Fader.start_fadeout = True
                fade = Fader(screen)
        if Fader.start_fadeout:
            if fade.fade_out():
                Fader.start_fadeout = False
                Assets.lvl += 1
                Assets.newgame = 0
                if Assets.lvl > Assets.max_level:
                    Assets.max_level = Assets.lvl
                screen.blit(loading_text,loading_rect)
                pygame.display.update()
                Assets.map = Level(level_list.get(Assets.lvl),level_assets[Assets.lvl], screen)
                Fader.start_fadein = True 
                  
        if Fader.start_fadein:
            if fade.fade_in():
                Fader.start_fadein = False
    
    Debug.tick2 = pygame.time.get_ticks()
    
    if Assets.debug_on:
        Assets.debug.run_debugger()

    pygame.display.update()
      
    Assets.clock.tick(60)
