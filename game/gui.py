import FreeSimpleGUI as sg
from game import Game

class GUI:
    def __init__(self, game: Game):
        self.game = game
        self.window = self.create_window(game)
        
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

        image = self.game.current_location.image

        graph = sg.Graph(
            canvas_size=(100, 100),
            graph_bottom_left=(0, 0),
            graph_top_right=(100, 100),
            key='-CANV-',
            background_color="#FFFFFF",
        )

        layout = [
            [graph, sg.Text(str(game.player) + str(game.current_location.description), size=(100, 4), font='Any 12', key='-OUTPUT-')],
            [command_col],
        ]
        return sg.Window('Declans Game', layout, size=(800, 400))
    
    def run(self):
        while True:
            event, values = self.window.read()
            
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            
        self.window.close()