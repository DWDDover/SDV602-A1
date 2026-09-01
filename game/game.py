from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio
from player import Player
from items import rusty_sword, sharp_sword, fire_potion
from location import Location
from enemies import rat, goblin, wizard
from combat import Combat
from item import Item

class Game:
    def __init__(self):
        self.player = Player()
        self.current_location = village
        
    def move(self, direction):
        if direction in self.current_location.directions:
            self.current_location = self.current_location.directions[direction]
            print(str(self.current_location.description))
            return str(self.current_location.description)
        else:
            return "You cannot travel there"
        
    def engage(self):
        location = self.current_location

        if not location.enemies:
            return "There is nothing here to engage."

        enemy = location.enemies[0]
        result = Combat(self.player, enemy).fight()
        message = '\n'.join(result["log"])

        if result["outcome"] == "win":
            location.enemies.remove(enemy)
            loot = enemy.loot if isinstance(enemy.loot, Item) else None
            if loot:
                self.player.inventory.add_item(loot)
                message += f"\nYou loot a {loot.name}."

        return message
    

#locations created initially with string references
village = Location("Village", "You are in a small village consisting of some crude huts and farmland",
                    {"north": "forest", "east": "lake", "south": "cave_mouth"}, [], [], "./images/village.png")

forest = Location("Forest", "You are in a dense dark forest",
                   {"west": "castle", "east": "clearing", "south": "village"}, [], [], "./images/forest.png")

clearing = Location("Clearing", "Your are in a sunlit forest clearing, you see a goblin wandering around",
                   {"west": "forest"}, [goblin], [], "./images/forest_clearing.png")

castle = Location("Castle", "You are in a castle, you see stairs leading upwards to your right and a large heavy door to your left",
                   {"door": "dungeon", "east": "forest", "stairs": "tower"}, [], [], "./images/castle.png")

tower = Location("Tower", "You come face to face with a wizard",
                   {"stairs": "castle"}, [wizard], [], "./images/tower.png")

dungeon = Location("Dungeon", "A gloomy damp dungeon",
                   {"door": "castle"}, [], [sharp_sword], "./images/dungeon.png")

lake = Location("Lake", "You are on the shore of a huge blue lake surrounded by reeds",
                   {"west": "village"}, [], [fire_potion], "./images/lake.png")

cave_mouth = Location("Cave mouth", "You are at the mouth of a large dark cave",
                   {"north": "village", "cave entrance" : "cave"}, [], [rusty_sword], "./images/cave_mouth.png")

cave = Location("Cave", "You are in a large well lit cave surrounded by bones and rocks, you can see a rat wandering the clearing",
                   {"west": "village"}, [rat], [], "./images/cave.png")

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