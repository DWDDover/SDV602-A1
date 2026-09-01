from inventory import Inventory
from loadout import Loadout

class Player:
    def __init__(self):
        self.max_hp = 100
        self.current_hp = 100
        self.attack = 2
        self.defense = 2
        self.fire_resistant = False
        self.inventory = Inventory()
        self.equipment = Loadout()

    def __str__(self):
        gear = ', '.join(
            f"{slot}: {item.name}" if item else f"{slot}: (empty)"
            for slot, item in (
                ("weapon", self.equipment.weapon),
                ("head", self.equipment.head),
                ("armor", self.equipment.armor),
            )
        )
        return (
            "HP: " + str(self.current_hp) + "/" + str(self.max_hp) +
            "\nAttack: " + str(self.attack) + "\nDefense: " + str(self.defense) +
            "\n" + gear + "\n"
        )