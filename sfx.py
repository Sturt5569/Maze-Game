import pygame  
from assets import Assets
from file_handler import log_error

class Music:
#----------list of background tracks----------#
    def __init__(self):
        self.menu = 'Maze/audio/music/bgmus_1.wav'
        self.game = ['Maze/audio/music/bgmus_2.wav',
                      'Maze/audio/music/bgmus_3.wav',
                      'Maze/audio/music/bgmus_4.wav',
                      'Maze/audio/music/bgmus_5.wav']  
        self.tracks = len(self.game) - 1

#----------initialise mixer. Plays active track indefinitely----------#
        pygame.mixer.init()
        pygame.mixer.music.set_volume(Assets.music_volume/10)
        self.menu_music()
        pygame.mixer.music.play(loops = -1, fade_ms = 2000)

#----------assign menu as active track----------#
    def menu_music(self):
        path = self.menu
        pygame.mixer.music.load(path)

#----------set track and playlist to game music----------#
    def start_game_music(self):
        pygame.mixer.music.fadeout(1000)
        self.next_track = 1
        self.current_track = self.next_track - 1
        self.current_track_path = self.game[self.current_track]
        self.next_track_path = self.game[self.next_track]
        pygame.mixer.music.load(self.current_track_path)
        pygame.mixer.music.play(loops = -1, fade_ms = 2000)
        pygame.mixer.music.queue(self.next_track_path)
        self.track_timer = pygame.time.get_ticks()
        self.fade_offset = 0
        self.game_music()

#----------play game music, advance track every 2 minutes----------#
    def game_music(self):
        if pygame.mixer.music.get_busy():
            self.play_time = pygame.time.get_ticks()
            self.elapsed = self.play_time - self.track_timer
            if self.elapsed >= 120000:
                self.advance = False
                self.music_fadeout()
                if self.advance:
                    self.track_advance()
        else:
            self.current_track = 0
            pygame.mixer.music.load(self.current_track_path)
            pygame.mixer.music.play(loops = -1)
            pygame.mixer.music.queue(self.next_track_path)

#----------load next track and update queue ----------#
    def track_advance(self):

        if self.next_track == self.tracks:
            self.next_track = 0
            self.current_track = self.tracks
        elif self.next_track == 0:
            self.next_track += 1
            self.current_track = self.next_track - 1 
        else:
            self.next_track += 1
            self.current_track = self.next_track - 1

        self.current_track_path = self.game[self.current_track]
        self.next_track_path = self.game[self.next_track]
        pygame.mixer.music.load(self.current_track_path)
        pygame.mixer.music.play(loops = -1, fade_ms=2000)
        pygame.mixer.music.queue(self.next_track_path) 
        self.track_timer = pygame.time.get_ticks()              
#---------- music fadeout loop that runs alongside game loop----------#   
    def music_fadeout(self):
        self.fade_offset += 0.001
        new_vol = Assets.music_volume/10 - self.fade_offset
        pygame.mixer.music.set_volume(new_vol)
        if new_vol <= 0:
            self.advance = True
            self.fade_offset = 0
            pygame.mixer.music.set_volume(Assets.music_volume/10)


#----------create and update the sliders for volume controls----------#
class Slider:
    def __init__(self):
        self.less = pygame.image.load('Maze/img/slider_decrease.png').convert_alpha()
        self.less.set_colorkey('#000000')
        self.slider_1 = pygame.image.load('Maze/img/slider_1.png').convert_alpha()
        self.slider_1.set_colorkey('#000000')
        self.slider_2 = pygame.image.load('Maze/img/slider_2.png').convert_alpha()
        self.slider_2.set_colorkey('#000000')
        self.slider_3 = pygame.image.load('Maze/img/slider_3.png').convert_alpha()
        self.slider_3.set_colorkey('#000000')
        self.slider_4 = pygame.image.load('Maze/img/slider_4.png').convert_alpha()
        self.slider_4.set_colorkey('#000000')
        self.slider_5 = pygame.image.load('Maze/img/slider_5.png').convert_alpha()
        self.slider_5.set_colorkey('#000000')
        self.more = pygame.image.load('Maze/img/slider_increase.png').convert_alpha()
        self.more.set_colorkey('#000000')
 
#----------#blit slider images in given position based on current volume----------#
    def draw_slider(self,target,posx,posy,surface):
        self.value = target
        self.display_surface = surface
        if target == 2:
            self.display_surface.blit(self.slider_1,(posx + 32,posy)) 
        elif target == 4:
            self.display_surface.blit(self.slider_2,(posx + 32,posy)) 
        elif target == 6:
            self.display_surface.blit(self.slider_3,(posx + 32,posy)) 
        elif target == 8:
            self.display_surface.blit(self.slider_4,(posx + 32,posy)) 
        elif target == 10:
            self.display_surface.blit(self.slider_5,(posx + 32,posy))  

        self.less_rect = self.less.get_rect(topleft = (posx + 5,posy))
        self.display_surface.blit(self.less,self.less_rect)
        self.more_rect = self.more.get_rect(topleft = ((posx + 195),posy))
        self.display_surface.blit(self.more,self.more_rect)

#----------check for + or - button clicks on sliders----------#
    def check_clicks(self,target,mousex,mousey,event_list):
        self.event_list = event_list
        self.mouse_x = mousex
        self.mouse_y = mousey
        if self.less_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if target == "music" and Assets.music_volume > 0:
                        Assets.music_volume -= 2
                        if Assets.music_volume % 2 != 0:
                            Assets.music_volume += 1
                            log_error("Music volume value not an even number. Corrected by Slider action")
                    if target == "sfx" and Assets.sfx_volume > 0:
                        Assets.sfx_volume -= 2
                        if Assets.sfx_volume % 2 != 0:
                            Assets.sfx_volume += 1
                            log_error("Sfx volume value not an even number. Corrected by Slider action")
                    pygame.mixer.music.set_volume(Assets.music_volume/10)
                    Assets.sfx.click()

        if self.more_rect.collidepoint(self.mouse_x, self.mouse_y):
            for event in self.event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if target == "music" and Assets.music_volume < 10:
                        Assets.music_volume += 2
                        if Assets.music_volume % 2 != 0:
                            Assets.music_volume -= 1
                            log_error("Music volume value not an even number. Corrected by Slider action")
                    if target == "sfx" and Assets.sfx_volume < 10:
                        Assets.sfx_volume += 2
                        if Assets.sfx_volume % 2 != 0:
                            Assets.sfx_volume -= 1
                            log_error("Sfx volume value not an even number. Corrected by Slider action")
                    pygame.mixer.music.set_volume(Assets.music_volume/10)
                    Assets.sfx.click()

                    
#----------sound effects (collect item, button click etc)----------#
class Sounds:
    def __init__(self):
        self.clicks = pygame.mixer.Sound('Maze/audio/sounds/click.wav')
        self.clicks.set_volume(Assets.sfx_volume/10)

    def click(self):
        self.clicks.set_volume(Assets.sfx_volume/10)
        self.clicks.play(0)