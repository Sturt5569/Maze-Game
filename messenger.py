import pygame
from assets import Assets

class Prompt:
    def __init__(self,surface):
        self.display_surface = surface
        self.message_font = pygame.font.Font(None, 30)
        self.dialogue = pygame.image.load('Maze/img/dialogue_bg.png').convert()
        self.dialogue_rect = self.dialogue.get_rect(center = (Assets.width/2,Assets.height/2))
        self.d_originx, self.d_originy = self.dialogue_rect.topleft
        self.cancel_off = pygame.image.load('Maze/img/btn_cancel.png').convert_alpha()
        self.cancel_off.set_colorkey('#000000')
        self.cancel_on = pygame.image.load('Maze/img/btn_cancel_o.png').convert_alpha()
        self.cancel_on.set_colorkey('#000000')
        self.cancel_rect = self.cancel_off.get_rect(center = (self.d_originx + 145,self.d_originy + 170))
        self.confirm_off = pygame.image.load('Maze/img/btn_confirm.png').convert_alpha()
        self.confirm_off.set_colorkey('#000000')
        self.confirm_on = pygame.image.load('Maze/img/btn_confirm_o.png').convert_alpha()
        self.confirm_on.set_colorkey('#000000')
        self.confirm_rect = self.confirm_off.get_rect(center = (self.d_originx + 455,self.d_originy + 170))
        self.confirmmiddle_rect = self.confirm_off.get_rect(center = (self.d_originx + 300,self.d_originy + 170))


    def prompt_single(self,message1="",message2=""):
        prompt = True
        self.message1 = message1
        self.message2 = message2
        while prompt:

            self.message = self.message_font.render(message1,True,'white')
            self.message_rect = self.message.get_rect(center = (self.d_originx + 300, self.d_originy + 60))
            self.message2 = self.message_font.render(message2,True,'white')
            self.message2_rect = self.message2.get_rect(center = (self.d_originx + 300, self.d_originy + 120))
            self.display_surface.blit(self.dialogue,self.dialogue_rect)
            self.display_surface.blit(self.message,self.message_rect)
            self.display_surface.blit(self.message2,self.message2_rect)
            self.events = pygame.event.get()
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

            if self.confirmmiddle_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.confirm_mouseover = True
                for event in self.events:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        prompt = False
                        return True
            else:
                self.confirm_mouseover = False

            if self.confirm_mouseover:
                self.display_surface.blit(self.confirm_on,self.confirmmiddle_rect)
            else:
                self.display_surface.blit(self.confirm_off,self.confirmmiddle_rect)
            pygame.display.update()
            Assets.clock.tick(60)

    def prompt_double(self,message1="",message2=""):
        self.message1 = message1
        self.message2 = message2
        prompt = True
        while prompt:

            self.message1 = self.message_font.render(message1,True,'white')
            self.message1_rect = self.message1.get_rect(center = (self.d_originx + 300, self.d_originy+ 60))
            self.message2 = self.message_font.render(message2,True,'white')
            self.message2_rect = self.message2.get_rect(center = (self.d_originx + 300, self.d_originy+ 120))
            self.display_surface.blit(self.dialogue,self.dialogue_rect)

            self.display_surface.blit(self.message1,self.message1_rect)
            self.display_surface.blit(self.message2,self.message2_rect)
            self.events = pygame.event.get()
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

            if self.confirm_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_confirm_mouseover = True
                for event in self.events:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        prompt = False
                        return True
            else:
                self.btn_confirm_mouseover = False

            if self.cancel_rect.collidepoint(self.mouse_x, self.mouse_y):
                self.btn_cancel_mouseover = True
                for event in self.events:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Assets.sfx.click()
                        prompt = False
                        return False
            else:
                self.btn_cancel_mouseover = False

            if self.btn_confirm_mouseover:
                self.display_surface.blit(self.confirm_on,self.confirm_rect)
            else:
                self.display_surface.blit(self.confirm_off,self.confirm_rect)

            if self.btn_cancel_mouseover:
                self.display_surface.blit(self.cancel_on,self.cancel_rect)
            else:
                self.display_surface.blit(self.cancel_off,self.cancel_rect)

            pygame.display.update()
            Assets.clock.tick(60)