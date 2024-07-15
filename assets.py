from maps import *


tile_size = 16              # size of tiles in grid. Default 16.



screen_width = 1200         # Default height and width on game loading. Min 1200 x 688
screen_height = 688


class Assets:
    #----------global variables and settings
    music_volume = 2
    sfx_volume = 2

    #----------screen size
    width = 1200            # actual screen height and width taken from system and variable
    height = 688
    fullscreen = False      # fullscreen active or not
    toggle = False          # toggle fullscreen on this pass
    
    #----------game state and level settings
    clock = None            # game clock = initialisted as startup
    gamestate = "menu"      # key gamestate
    game_menu = False       # popup menu toggle in game
    popsettings = False     # popup settings menu toggle in game
    savemenu = False        # popup toggle for savegame
    loadmenu = False        # popup toggle for load game
    debug_on = False        # activates debugger
    prompt = False          # toggle "restart level to change colour" message on in game menu
    max_level = 16          # highest unlocked level
    lvl = 0                 # current loaded level
    newgame = 1             # has a savegame been loaded or a game started?
    port_locked = False     # Locks and unlocks teleports


    #----------Gameplay variables
    img_set = 4             # boundary wall colour scheme default (select 0 - 6)
    player_icon = 3         # player icol colour default (select 0 - 6)
    movement_speed = 2      # player start speed before acceleration
    max_speed = 4           # player top speed after acceleration
    enemy_speed = 3
    
    #----------game objects  
    map = None              # object containing level map and maze data from Level class
    overworld = None        # object containing Overworld from Overworld Class
    menu = None             # object containint Main menu and settings screen from Menu class
    music = None            # object controlling Background music
    sfx = None              # object controlling Sound effects
    music_slider = None     # object creates the sliders for music volume
    sfx_slider = None       # object creates the sliders for SFX volume
    popmenu = None          # object containing in game menu and settings screen
    debug = None            # object controlling debugger
    savegame = None         # Save/load handler object
    message = None          # object displays messages and user prompts.




