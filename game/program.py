from player import Player
from game import Game
from gui import GUI
from command_parser import Command_parser

#This fixes the display of the window on my home PC for some reason
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

HEADLESS = True

if __name__ == "__main__":
    game = Game()
    
    if not HEADLESS:
        gui = GUI(game)
        gui.run()
        
    else:
        cp = Command_parser(game)
        print(game.player)
        print(game.current_location.description)
        print(cp.parse("travel north"))
        print(cp.parse("travel east"))
        print(cp.parse("engage"))
        print(game.player)
        print(game.player.inventory.items[0].name)