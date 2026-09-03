from game import Game
from gui import GUI
import sys
from testing import run_headless_tests

#This fixes the display of the window on my home PC for some reason.
#AI found the solution for me
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

##add --headless to the run command for testing
HEADLESS = '--headless' in sys.argv

if __name__ == "__main__":
    
    if not HEADLESS:
        game = Game()
        gui = GUI(game)
        gui.run()
        
    else:
        results = run_headless_tests()
        print(results)