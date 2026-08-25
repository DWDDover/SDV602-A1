from player import Player
from game import Game
from gui import GUI

if __name__ == "__main__":
    player = Player()
    game = Game()

    gui = GUI(game)
    gui.run()