from file_handler import *
from assets import Assets
import pygame

class Savegame:

    saveslot1 = [False,None,None]
    saveslot2 = [False,None,None]
    saveslot3 = [False,None,None]
    saveslot4 = [False,None,None]
    cycles = 0

    def __init__(self,surface):
        self.display_surface = surface
        self.savebg = pygame.image.load('Maze/img/savepopup_bg.png').convert()
        self.loadbg = pygame.image.load('Maze/img/loadpopup_bg.png').convert()
        self.bg_rect = self.savebg.get_rect(center = (Assets.width/2,Assets.height/2))
        self.p_originx, self.p_originy = self.bg_rect.topleft
        self.message_font = pygame.font.Font(None, 30)
             
        self.slot1 = pygame.image.load('Maze/img/save_slot_1.png').convert_alpha()
        self.slot1.set_colorkey('#000000')
        self.slot1_rect = self.slot1.get_rect(center = (self.p_originx + 152,self.p_originy + 75))
        self.slot2 = pygame.image.load('Maze/img/save_slot_2.png').convert_alpha()
        self.slot2.set_colorkey('#000000')
        self.slot2_rect = self.slot2.get_rect(center = (self.p_originx + 152,self.p_originy + 150))
        self.slot3 = pygame.image.load('Maze/img/save_slot_3.png').convert_alpha()
        self.slot3.set_colorkey('#000000')
        self.slot3_rect = self.slot3.get_rect(center = (self.p_originx + 152,self.p_originy + 225))
        self.slot4 = pygame.image.load('Maze/img/save_slot_4.png').convert_alpha()
        self.slot4.set_colorkey('#000000')
        self.slot4_rect = self.slot4.get_rect(center = (self.p_originx + 152,self.p_originy + 300))
        self.back_off = pygame.image.load('Maze/img/back.png').convert_alpha()
        self.back_off.set_colorkey('#000000')
        self.back_on = pygame.image.load('Maze/img/back_o.png').convert_alpha()
        self.back_on.set_colorkey('#000000')
        self.back_rect = self.back_off.get_rect(center = (self.p_originx + 145,self.p_originy + 410))
        self.back_mouseover = False

        self.get_savedata()

    def get_savedata(self):
        #verify save slot 1 and get summary
        cont = True 
        try:
            file = open('Maze/savegame/savegame_1.txt')
        except:
            print("Save slot 1 failed to load.")
            log_error("Savegame 1 file not found or could not be opened")
            cont = False
        if cont:
            try:
                valid = True
                for line in file:
                    line = line.split()
                    if line[0] == 'utilised' and line[2] == "0":                                     
                        Savegame.saveslot1[0] = False
                        valid = False
                    if valid:
                        Savegame.saveslot1[0] = True
                        if line[0] == "date":
                            Savegame.saveslot1[1] = line[2]
                        if line[0] == "time":
                            Savegame.saveslot1[2] = line[2]         
                file.close() 
                if Savegame.saveslot1[0]:
                    if Savegame.saveslot1[1] == None or Savegame.saveslot1[2] == None:
                        raise ValueError 
            except:
                Savegame.saveslot1 = [False,None,None]
                print("Save slot 1 corrupt")
                log_error("Save slot 1 file is corrupt or invalid.")

        #verify save slot 2 and get summary       
        cont = True
        try:
            file = open('Maze/savegame/savegame_2.txt')
        except:
            print("Save slot 2 failed to load.")
            log_error("Savegame 2 file not found or could not be opened")
            cont = False
        if cont:
            try:
                valid = True
                for line in file:
                    line = line.split()
                    if line[0] == 'utilised' and line[2] == "0":                                     
                        Savegame.saveslot2[0] = False
                        valid = False
                    if valid:
                        Savegame.saveslot2[0] = True
                        if line[0] == "date":
                            Savegame.saveslot2[1] = line[2]
                        if line[0] == "time":
                            Savegame.saveslot2[2] = line[2]           
                file.close()               
                if Savegame.saveslot2[0]:
                    if Savegame.saveslot2[1] == None or Savegame.saveslot2[2] == None:
                        raise ValueError
            except:
                Savegame.saveslot2 = [False,None,None]
                print("Save slot 2 corrupt")
                log_error("Save slot 2 file is corrupt or invalid.")

        #verify save slot 3 and get summary        
        cont = True
        try:
            file = open('Maze/savegame/savegame_3.txt')
        except:
            print("Save slot 3 failed to load.")
            log_error("Savegame 3 file not found or could not be opened")
            cont = False
        if cont:
            try:
                valid = True
                for line in file:
                    line = line.split()
                    if line[0] == 'utilised' and line[2] == "0":                                     
                        Savegame.saveslot3[0] = False
                        valid = False
                    if valid:
                        Savegame.saveslot3[0] = True
                        if line[0] == "date":
                            Savegame.saveslot3[1] = line[2]
                        if line[0] == "time":
                            Savegame.saveslot3[2] = line[2]         
                file.close()              
                if Savegame.saveslot3[0]:
                    if Savegame.saveslot3[1] == None or Savegame.saveslot3[2] == None:
                        raise ValueError
            except:
                Savegame.saveslot3 = [False,None,None]
                print("Save slot 3 corrupt")
                log_error("Save slot 3 file is corrupt or invalid.")
        cont = True

        #verify save slot 4 and get summary       
        try:
            file = open('Maze/savegame/savegame_4.txt')
        except:
            print("Save slot 4 failed to load.")
            log_error("Savegame 4 file not found or could not be opened")
            cont = False

        if cont:
            try:
                valid = True
                for line in file:
                    line = line.split()
                    if line[0] == 'utilised' and line[2] == "0":                                     
                        Savegame.saveslot4[0] = False
                        valid = False
                    if valid:
                        Savegame.saveslot4[0] = True
                        if line[0] == "date":
                            Savegame.saveslot4[1] = line[2]
                        if line[0] == "time":
                            Savegame.saveslot4[2] = line[2]       
                file.close()                
                if Savegame.saveslot4[0]:
                    if Savegame.saveslot4[1] == None or Savegame.saveslot4[2] == None:
                        raise ValueError
            except:
                Savegame.saveslot4 = [False,None,None]
                print("Save slot 4 corrupt")
                log_error("Save slot 4 file is corrupt or invalid.")
        self.text = pygame.font.Font(None, 30)
        self.slot_empty = self.text.render("EMPTY", True, '#01fffd')
        self.slot1_empty_rect = self.slot_empty.get_rect(topleft = (self.p_originx + 150,self.p_originy + 69))
        self.slot2_empty_rect = self.slot_empty.get_rect(topleft = (self.p_originx + 150,self.p_originy + 144))
        self.slot3_empty_rect = self.slot_empty.get_rect(topleft = (self.p_originx + 150,self.p_originy + 219))
        self.slot4_empty_rect = self.slot_empty.get_rect(topleft = (self.p_originx + 150,self.p_originy + 294))

        self.slot1_datetime = self.text.render(f"{Savegame.saveslot1[1]} {Savegame.saveslot1[2]}", True, '#01fffd')
        self.slot1_datetime_rect = self.slot1_datetime.get_rect(topleft = (self.p_originx + 105,self.p_originy + 69))
        self.slot2_datetime = self.text.render(f"{Savegame.saveslot2[1]} {Savegame.saveslot2[2]}", True, '#01fffd')
        self.slot2_datetime_rect = self.slot2_datetime.get_rect(topleft = (self.p_originx + 105,self.p_originy + 144))
        self.slot3_datetime = self.text.render(f"{Savegame.saveslot3[1]} {Savegame.saveslot3[2]}", True, '#01fffd')
        self.slot3_datetime_rect = self.slot3_datetime.get_rect(topleft = (self.p_originx + 105,self.p_originy + 219))
        self.slot4_datetime = self.text.render(f"{Savegame.saveslot4[1]} {Savegame.saveslot4[2]}", True, '#01fffd')
        self.slot4_datetime_rect = self.slot4_datetime.get_rect(topleft = (self.p_originx + 105,self.p_originy + 294))
    
    def save_popup(self,mouse_x,mouse_y,event_list):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list

        self.display_surface.blit(self.savebg,self.bg_rect)

        self.skip = False
        if Savegame.cycles > 1:
            if self.back_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.back_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.savemenu = False
                        if Assets.gamestate == "gameplay":
                            Assets.game_menu = True
                        Assets.sfx.click()
            else:
                self.back_mouseover = False
        
        if self.back_mouseover:
            self.display_surface.blit(self.back_on,self.back_rect)
        else:
            self.display_surface.blit(self.back_off,self.back_rect)
        
        #display slot 1 and check for clicks
        self.display_surface.blit(self.slot1,self.slot1_rect)
        if Savegame.saveslot1[0]:
            self.display_surface.blit(self.slot1_datetime,self.slot1_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot1_empty_rect)
        
        if not self.skip:
            if self.slot1_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checksave(Savegame.saveslot1,1)
                        if proceed:
                            confirm = save_game(1)
                            if confirm:
                                self.confirm_save()
                            else:
                                self.save_failed()


        #display slot 2 and check for clicks
        self.display_surface.blit(self.slot2,self.slot2_rect)
        if Savegame.saveslot2[0]:
            self.display_surface.blit(self.slot2_datetime,self.slot2_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot2_empty_rect)

        if not self.skip:        
            if self.slot2_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checksave(Savegame.saveslot2,2)
                        if proceed:
                            confirm = save_game(2)
                            if confirm:
                                self.confirm_save()
                            else:
                                self.save_failed()

        #display slot 3 and check for clicks
        self.display_surface.blit(self.slot3,self.slot3_rect)
        if Savegame.saveslot3[0]:
            self.display_surface.blit(self.slot3_datetime,self.slot3_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot3_empty_rect)

        if not self.skip:
            if self.slot3_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checksave(Savegame.saveslot3,3)
                        if proceed:
                            confirm = save_game(3)
                            if confirm:
                                self.confirm_save()
                            else:
                                self.save_failed()

        #display slot 4 and check for clicks
        self.display_surface.blit(self.slot4,self.slot4_rect)
        if Savegame.saveslot4[0]:
            self.display_surface.blit(self.slot4_datetime,self.slot4_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot4_empty_rect)
        
        if not self.skip and Savegame.cycles > 1:       
            if self.slot4_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checksave(Savegame.saveslot4,4)
                        if proceed:
                            confirm = save_game(4)
                            if confirm:
                                self.confirm_save()
                            else:
                                self.save_failed()
        Savegame.cycles += 1
    def checksave(self,slot,num):
        self.slot = slot

        if self.slot[0]:
            message1 = "Save slot already in use." 
            message2 = "Overwrite?"
        else:
            message1 = f"Game will be saved in slot {num}" 
            message2 = "Continue?"
        result = Assets.message.prompt_double(message1,message2)
        return result

    def confirm_save(self):
        self.get_savedata()
        message1 = "Game saved."
        result = Assets.message.prompt_single(message1)
        if result:
            Assets.savemenu = False
    
    def save_failed(self):
        message1 = "There was an error while saving."
        Assets.message.prompt_single(message1)
    
    def load_popup(self,mouse_x,mouse_y,event_list):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.event_list = event_list

        self.display_surface.blit(self.loadbg,self.bg_rect)

        self.skip = False
        if Savegame.cycles > 1:
            if self.back_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.back_mouseover = True
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.loadmenu = False
                        Assets.sfx.click()
            else:
                self.back_mouseover = False
        
        if self.back_mouseover:
            self.display_surface.blit(self.back_on,self.back_rect)
        else:
            self.display_surface.blit(self.back_off,self.back_rect)

        Savegame.cycles += 1

        #display slot 1 and check for clicks
        self.display_surface.blit(self.slot1,self.slot1_rect)
        if Savegame.saveslot1[0]:
            self.display_surface.blit(self.slot1_datetime,self.slot1_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot1_empty_rect)
        
        if not self.skip:
            if self.slot1_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checkload(Savegame.saveslot1,1)
                        if proceed:
                            confirm = load_game(1)
                            if confirm:
                                self.confirm_load()
                            else:
                                self.load_failed()


        #display slot 2 and check for clicks
        self.display_surface.blit(self.slot2,self.slot2_rect)
        if Savegame.saveslot2[0]:
            self.display_surface.blit(self.slot2_datetime,self.slot2_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot2_empty_rect)

        if not self.skip:        
            if self.slot2_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checkload(Savegame.saveslot2,2)
                        if proceed:
                            confirm = load_game(2)
                            if confirm:
                                self.confirm_load()
                            else:
                                self.load_failed()

        #display slot 3 and check for clicks
        self.display_surface.blit(self.slot3,self.slot3_rect)
        if Savegame.saveslot3[0]:
            self.display_surface.blit(self.slot3_datetime,self.slot3_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot3_empty_rect)

        if not self.skip:
            if self.slot3_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checkload(Savegame.saveslot3,3)
                        if proceed:
                            confirm = load_game(3)
                            if confirm:
                                self.confirm_load()
                            else:
                                self.load_failed()

        #display slot 4 and check for clicks
        self.display_surface.blit(self.slot4,self.slot4_rect)
        if Savegame.saveslot4[0]:
            self.display_surface.blit(self.slot4_datetime,self.slot4_datetime_rect)
        else:
            self.display_surface.blit(self.slot_empty,self.slot4_empty_rect)
        
        if not self.skip:       
            if self.slot4_rect.collidepoint(self.mouse_x, self.mouse_y):
                for event in self.event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        self.skip = True
                        proceed = self.checkload(Savegame.saveslot4,4)
                        if proceed:
                            confirm = load_game(4)
                            if confirm:
                                self.confirm_load()
                            else:
                                self.load_failed()
    
    def checkload(self,slot,num):
        self.slot = slot
        if not self.slot[0]:
            message1 = "This slot contains no data. Pick another!"
            Assets.message.prompt_single(message1)
        else:
            message1 = f"Game will be loaded from slot {num}. Current progress"
            message2 = "will be lost unless saved. Continue?"
            result = Assets.message.prompt_double(message1, message2)    
            return result
        
    def confirm_load(self):
        Assets.newgame = 0
        self.get_savedata()
        message1 = "Game loaded."
        result = Assets.message.prompt_single(message1)
        if result:
            Assets.loadmenu = False
                
    def load_failed(self):
        message1 = "Unable to load game."
        message2 = "Please try again."
        Assets.message.prompt_single(message1,message2)