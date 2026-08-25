import FreeSimpleGUI as sg
from game import Game

class GUI():
    def __init__(self, game: Game):
        self.game = game
        self.window = self.create_window(self, game)
        
    def create_window(self, game):
        """Create and return the main application window.

        The left area is a coloured `sg.Graph` element used to represent the current location.
        The right area shows the description and a text input.
        """
        game = self.game
        
        sg.theme('Dark Blue 3')

        prompt_input = [
            sg.Text('Enter your command', font='Any 14'),
            sg.Input(key='-IN-', size=(20, 1), font='Any 14'),
        ]
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
        command_col = sg.Column([prompt_input, buttons], element_justification='r')

        colour = game.get_current_location().colour

        graph = sg.Graph(
            canvas_size=(100, 100),
            graph_bottom_left=(0, 0),
            graph_top_right=(100, 100),
            key='-CANV-',
            background_color=colour,
        )

        layout = [
            [graph, sg.Text('HP: ' + str(game.player.health_current) + '/' + str(game.player.health_max) +
                            ' DMG: ' + str(game.player.damage) + ' BLOCK: ' + str(game.player.block) +
                            '\n' +
                            str(game.get_current_location().story), size=(
                100, 4), font='Any 12', key='-OUTPUT-')],
            [command_col],
        ]
        return sg.Window('Adventure Game', layout, size=(400, 200))