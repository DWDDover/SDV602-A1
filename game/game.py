from player import Player
from items import rusty_sword, sharp_sword, fire_potion, health_potion
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
            return str(self.current_location.description)
        else:
            return "You cannot travel there"
        
    def search(self):
        location = self.current_location

        if not location.items:
            return "You don't find anything"
        
        else:
            item = location.items[0]
            self.player.inventory.add_item(item)
            return(f"You have found a {item.name}")
        
    def equip(self, item_name):
        item = self.player.inventory.get_item_by_name(item_name)

        if item is None:
            return f"You don't have a {item_name}."

        if not hasattr(self.player.equipment, item.slot):
            return f"{item.name} cannot be equipped."

        previous = getattr(self.player.equipment, item.slot)
        if previous is not None:
            # remove the old item's stat bonus before applying the new one
            self.player.attack -= previous.damage
            self.player.defense -= previous.block

        setattr(self.player.equipment, item.slot, item)
        self.player.attack += item.damage
        self.player.defense += item.block

        if previous:
            return f"You equip the {item.name} in your {item.slot} slot, replacing the {previous.name}."
        return f"You equip the {item.name} in your {item.slot} slot."
        
    def use(self, item_name):
        
        item = self.player.inventory.get_item_by_name(item_name)
        
        if self.player.inventory.has_item(item):
            if item == health_potion:
                self.player.current_hp = min(self.player.current_hp + item.heal, self.player.max_hp)
                return f"You heal for {item.heal} HP"
            elif item == fire_potion:
                self.player.fire_resistant = True
                return "You are now fire resistant"
            else:
                return "That item is not a consumable"
            
        if not item:
            return "Cannot use that item"
        
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
                   {"west": "castle", "east": "clearing", "south": "village"}, [], [health_potion], "./images/forest.png")

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