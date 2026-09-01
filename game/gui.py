import FreeSimpleGUI as sg
from game import Game
from command_parser import Command_parser

# Reference text for the "Commands" popup, sourced from the design spec.
COMMANDS_HELP = [
    ("travel <direction>", "Move to another location"),
    ("search", "Search the location and pick up any items you find"),
    ("equip <item>", "Equip a valid item from your inventory"),
    ("engage", "If the location has a monster, engage it and start combat"),
    ("use <item>", "Use a consumable item from your inventory"),
    ("exit", "Exit the application from any screen"),
]


class GUI:
    def __init__(self, game: Game):
        self.game = game
        self.game_over = False
        self.window = self.create_window(game)
        self.draw_location_image()
        self.refresh_display()

    def create_window(self, game):
        """Create and return the main application window.

        The left area is an `sg.Graph` element showing the current location's image.
        The right area shows the description, available directions, and inventory.
        Below that is the command input, and a button that opens a command reference popup.
        """
        sg.theme('Dark Blue 3')

        graph = sg.Graph(
            canvas_size=(260, 260),
            graph_bottom_left=(0, 0),
            graph_top_right=(260, 260),
            key='-CANV-',
            background_color="#FFFFFF",
        )
        #Player stats
        stats_output = sg.Multiline(
            default_text='', size=(50, 12), font='Any 12', key='-OUTPUT-',
            disabled=True, autoscroll=True,
        )
        #list of available directions
        directions_list = sg.Listbox(
            values=[], size=(20, 5), key='-DIRECTIONS-', font='Any 11',
            no_scrollbar=True,
        )
        #player inventory
        inventory_list = sg.Listbox(
            values=[], size=(20, 5), key='-INVENTORY-', font='Any 11',
            no_scrollbar=True,
        )

        side_panels = sg.Column([
            [sg.Frame('Directions', [[directions_list]])],
            [sg.Frame('Inventory', [[inventory_list]])],
        ])

        prompt_input = [
            sg.Text('Enter your command', font='Any 14'),
            sg.Input(key='-IN-', size=(20, 1), font='Any 14'),
        ]
        buttons = [
            sg.Button('Enter', bind_return_key=True),
            sg.Button('Commands'),
            sg.Button('Exit'),
        ]
        command_col = sg.Column([prompt_input, buttons], element_justification='r')

        layout = [
            [graph, stats_output, side_panels],
            [command_col],
        ]
        return sg.Window('Declans Game', layout, finalize=True)

    def draw_location_image(self):
        #draw the image of the curent location
        graph = self.window['-CANV-']
        graph.erase()
        image_path = self.game.current_location.image
        try:
            graph.draw_image(filename=image_path, location=(0, 260))
        except Exception:
           #draw a balnk square if image is not found
            graph.draw_rectangle((10, 10), (250, 250), fill_color='#DDDDDD', line_color='black')
            graph.draw_text(self.game.current_location.name, (130, 130), font='Any 14')

    def refresh_display(self, message=None):
        #update the GUI
        player = self.game.player
        location = self.game.current_location
        text = message if message is not None else location.description

        self.window['-OUTPUT-'].update(value=str(player) + '\n' + text)
        self.window['-DIRECTIONS-'].update(values=sorted(location.directions.keys()))
        equipped_items = {player.equipment.weapon, player.equipment.head, player.equipment.armor}
        self.window['-INVENTORY-'].update(
            values=[f"{item.name} (equipped)" if item in equipped_items else item.name for item in player.inventory.items]
        )
    #show the command list popup
    def show_commands_popup(self):
        lines = [f"{cmd:<20} {desc}" for cmd, desc in COMMANDS_HELP]
        sg.popup_scrolled(
            '\n'.join(lines),
            title='Available Commands',
            size=(60, len(COMMANDS_HELP) + 2),
            font='Any 11',
        )

    def end_game(self):
        #if the player loses disable all inputs except exit
        self.game_over = True
        self.window['-IN-'].update(disabled=True)
        self.window['Enter'].update(disabled=True)
        self.window['Commands'].update(disabled=True)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == 'Enter' and not self.game_over:
                output_message = None
                command = values['-IN-'].lower().strip()
                cp = Command_parser()
                output_message = cp.parse(command)

                if output_message is not None:
                    self.draw_location_image()
                    self.refresh_display(message=output_message)
                    self.window['-IN-'].update(value='')

                    if self.game.player.current_hp <= 0:
                        self.end_game()

            elif event == 'Commands':
                self.show_commands_popup()

            elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
                break

        self.window.close()