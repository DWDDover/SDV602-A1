from game import Game

class GUI():
    def __init__(self, game: Game):
        self.game = game
        self.window = self.create_window(self, game)