from player import Player
from game import Game
from gui import GUI

#This fixes the display of the window on my PC for some reason
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

if __name__ == "__main__":
    player = Player()
    game = Game()

    gui = GUI(game)
    gui.run()