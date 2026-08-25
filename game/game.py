from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio
from player import Player
from items import rusty_sword, sharp_sword, fire_potion
from location import Location
from enemies import rat, goblin, wizard

class Game:
    def __init__(self):
        self.player = Player()
        self.current_location = village

# locations created initially with string references
village = Location("Village", "A small village consisting of some crude huts and farmland",
                    {"North": "forest", "East": "lake", "South": "cave_mouth"}, [], [])

forest = Location("Forest", "A dense dark forest",
                   {"West": "castle", "East": "clearing", "South": "village"}, [], [])

clearing = Location("Clearing", "A sunlit forest clearing, you see a goblin wandering around",
                   {"West": "forest"}, [goblin], [])

castle = Location("Castle", "You are in a castle, you see stairs leading upwards to your right and a large heavy door to your left",
                   {"Door": "dungeon", "East": "forest", "Stairs": "tower"}, [], [])

tower = Location("Tower", "You come face to face with a wizard",
                   {"Stairs": "castle"}, [wizard], [])

dungeon = Location("Dungeon", "A gloomy damp dungeon",
                   {"Door": "castle"}, [], [sharp_sword])

lake = Location("Lake", "You are on the shore of a huge blue lake surrounded by reeds",
                   {"West": "village"}, [], [fire_potion])

cave_mouth = Location("Cave mouth", "You are at the mouth of a large dark cave",
                   {"North": "village", "Cave Entrance" : "cave"}, [], [rusty_sword])

cave = Location("Cave mouth", "You are in a large well lit cave surrounded by bones and rocks, you can see a rat wandering the clearing",
                   {"West": "village"}, [rat], [])

#location dictionary
locations = {"village": village, "forest": forest}  # add the rest here

#replace all the string values with the actual location objects
for location in locations.values():
    location.directions = {
        direction: locations[name]
        for direction, name in location.directions.items()
    }