from assets import Assets
from datetime import datetime

def settings_load():
    try:
        file = open('Maze/settings.txt', "rt")
        
        for line in file:
            value = line.split()
            if value[0] == "music_volume":
                Assets.music_volume = int(value[2])
            if value[0] == "sfx_volume":
                Assets.sfx_volume = int(value[2])
            if value[0] == "img_set":
                Assets.img_set = int(value[2])
            if value[0] == "player_icon":
                Assets.player_icon = int(value[2])
        file.close()    
    except:
        print("Settings file load error.")
        log_error("Setting load error. Settings not loaded - default values applied")

def settings_save():
    try:
        file = open('Maze/settings.txt', "wt")
        file.write("music_volume = " + str(Assets.music_volume) + "\n")
        file.write("sfx_volume = " + str(Assets.sfx_volume) + "\n")
        file.write("img_set = " + str(Assets.img_set) + "\n")
        file.write("player_icon = " + str(Assets.player_icon) + "\n")
        file.close()
    except:
        print("Settings file save error.")
        log_error("Setting save error: settings not saved on exit")

def save_game(slot):
    try:
        path = "Maze/savegame/savegame_" + str(slot) + ".txt"
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M")
        file = open(path, "wt")
        file.write("utilised = 1 \n")
        file.write("date = " + date + "\n")
        file.write("time = " + time + "\n")
        file.write("img_set = " + str(Assets.img_set) + "\n")
        file.write("player_icon = " + str(Assets.player_icon) + "\n")
        file.write("active_lvl = " + str(Assets.lvl) + "\n")
        file.write("max_lvl = " + str(Assets.max_level) + "\n")
        file.close()
        return True
    except:
        error = "Save game failed for slot " + str(slot)
        log_error(error)
        return False
    
def load_game(slot):
    try:
        path = "Maze/savegame/savegame_" + str(slot) + ".txt"
        file = open(path, "rt")
        
        for line in file:
            value = line.split()
            if value[0] == "active_lvl":
                Assets.lvl = int(value[2])
            if value[0] == "max_lvl":
                Assets.max_level = int(value[2])
            if value[0] == "img_set":
                Assets.img_set = int(value[2])
            if value[0] == "player_icon":
                Assets.player_icon = int(value[2])
        file.close() 
        return True
    except:
        print(f"failed to load from Save Slot {slot}")
        error = "Failed to load game from slot " + str(slot)
        log_error(error)
        return False

def log_error(value):
    timestamp = datetime.now()
    file = open('Maze/errorlog.txt', "a")
    file.write("\n\n" + str(timestamp) + "\n\n")
    file.write(str(value))
    file.close
    print("Error logged.")