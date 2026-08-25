from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio
from player import Player
from item import Item
from location import Location

class Game:
    def __init__(self):
        self.player = Player()
        self.current_location = village

# locations created initially with string references
village = Location("Village", "A small village consisting of some crude huts and farmland",
                    {"north": "forest", "east": "lake", "south": "cave_mouth"}, [], [])

forest = Location("Forest", "A dense dark forest",
                   {"west": "castle", "east": "clearing", "south": "village"}, [], [])


#location dictionary
all_locations = {"village": village, "forest": forest}  # add the rest here

#replace all the string values with the actual loaction objects
for location in all_locations.values():
    location.directions = {
        direction: all_locations[name]
        for direction, name in location.directions.items()
    }