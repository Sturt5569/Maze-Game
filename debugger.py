import pygame


class Debug:
    tick1 = 0
    tick2 = 0
    tickdelay = 0

    def __init__(self,screen):
        self.display_surface = screen
        self.fps_font = pygame.font.Font(None, 20)
        self.fps_text = self.fps_font.render(" ",False,'White')
        self.fps_rect = self.fps_text.get_rect(topleft = (60,5))  
        self.frames = []     


    def fps(self):  
        self.total = 0
        self.frames.append(Debug.tick2-Debug.tick1)
        if len(self.frames) == 20:
            del self.frames[0]        
        for x in self.frames:
            self.total += x
        self.averagetick = int(self.total / 20)
        self.fps_text = self.fps_font.render(f"tick: {self.averagetick}",False,'White')
        self.display_surface.blit(self.fps_text,self.fps_rect)

    def run_debugger(self):
        self.fps()