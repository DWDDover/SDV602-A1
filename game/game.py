from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio
from player import Player
from item import Item
from location import Location

class Game:
    def __init__(self):
        self.player = Player()
        self.current_location = village

village = Location("Village", "A small village consisting of some crude huts and farmland", {"north": forest, "east": lake, "south": cave_mouth}, "enemies" : [], "items" : [],)