from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio
from player import Player
from items import rusty_sword, sharp_sword, fire_potion
from location import Location
from enemies import rat, goblin, wizard

class Game:
    def __init__(self):
        self.player = Player()
        self.current_location = village
        
    def move(self, direction):
        self.current_location = self.current_location[direction]

# locations created initially with string references
village = Location("Village", "You are in a small village consisting of some crude huts and farmland",
                    {"North": "forest", "East": "lake", "South": "cave_mouth"}, [], [], "./images/village.png")

forest = Location("Forest", "You are in a dense dark forest",
                   {"West": "castle", "East": "clearing", "South": "village"}, [], [], "./images/village.png")

clearing = Location("Clearing", "Your are in a sunlit forest clearing, you see a goblin wandering around",
                   {"West": "forest"}, [goblin], [], "./images/village.png")

castle = Location("Castle", "You are in a castle, you see stairs leading upwards to your right and a large heavy door to your left",
                   {"Door": "dungeon", "East": "forest", "Stairs": "tower"}, [], [], "./images/village.png")

tower = Location("Tower", "You come face to face with a wizard",
                   {"Stairs": "castle"}, [wizard], [], "./images/village.png")

dungeon = Location("Dungeon", "A gloomy damp dungeon",
                   {"Door": "castle"}, [], [sharp_sword], "./images/village.png")

lake = Location("Lake", "You are on the shore of a huge blue lake surrounded by reeds",
                   {"West": "village"}, [], [fire_potion], "./images/village.png")

cave_mouth = Location("Cave mouth", "You are at the mouth of a large dark cave",
                   {"North": "village", "Cave Entrance" : "cave"}, [], [rusty_sword], "./images/village.png")

cave = Location("Cave mouth", "You are in a large well lit cave surrounded by bones and rocks, you can see a rat wandering the clearing",
                   {"West": "village"}, [rat], [], "./images/village.png")

#location dictionary
locations = {
    "village": village, 
    "forest": forest,
    "clearing": clearing,
    "castle": castle,
    "tower": tower,
    "dungeon": dungeon,
    "lake": lake,
    "cave_mouth": cave_mouth,
    "cave": cave 
    }

#replace all the string values with the actual location objects
for location in locations.values():
    location.directions = {
        direction: locations[name]
        for direction, name in location.directions.items()
    }