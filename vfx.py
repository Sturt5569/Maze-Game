import pygame
from assets import Assets

class Fader(pygame.sprite.Sprite):
    start_fadeout = False
    start_fadein = False
#----------define fader start and end values----------#
    def __init__(self, surface):
        super().__init__()
        self.display_surface = surface
        self.alpha_out = 0
        self.alpha_in = 300
    
#----------apply a black screen and increase alpha each----------#
    def fade_out(self):
        fade = pygame.Surface((Assets.width,Assets.height))
        fade.fill('#000000')
        self.alpha_out += 8
        fade.set_alpha(self.alpha_out)
        Assets.map.print_level()
        self.display_surface.blit(fade,(0,0))
        if self.alpha_out >= 300:
            Fader.start_fadeout = False
            self.alpha_out = 0
            self.kill()
            return True
        
#----------apply black screen and decrease alpha each cycle----------#
    def fade_in(self):
        fade = pygame.Surface((Assets.width,Assets.height))
        fade.fill('#000000')
        self.alpha_in -= 8
        fade.set_alpha(self.alpha_in)
        Assets.map.print_level()
        self.display_surface.blit(fade,(0,0))
        if self.alpha_in <= 10:
            Fader.start_fadein = False
            self.alpha = 300
            self.kill()
            return True

class Mask:
    def __init__(self,surface,screen_size):
        self.display_surface = surface
        self.display_size = screen_size
        self.mask = pygame.Surface(screen_size)
        self.mask.fill('black')
        self.mask.set_colorkey('white')
        self.mask_rect = self.mask.get_rect()
        
#----------draw mask overlay, locked to player position.----------#
#----------           called from Level class           ----------#
    def update_mask(self, pos):
        self.mask.fill('#000000')
        self.circle = pygame.draw.circle(self.mask, 'white', pos, 100)
        self.display_surface.blit(self.mask,self.mask_rect)