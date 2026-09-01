from inventory import Inventory

class Player:
    def __init__(self):
        self.max_hp = 100
        self.current_hp = 100
        self.attack = 2
        self.defense = 2
        self.fire_resistant = False
        self.inventory = Inventory()
        
    def __str__(self):
        return "HP: " + str(self.current_hp) + "/" + str(self.max_hp) + "\nAttack: " + str(self.attack) + "\nDefense: " + str(self.defense) + "\n"