class Player:
    def __init__(self):
        self.max_hp = 100
        self.current_hp = 100
        self.attack = 1
        self.defense = 1
        
    def __str__(self):
        return "HP: " + str(self.current_hp) + "/" + str(self.max_hp) + "\nAttack: " + str(self.attack) + "\nDefense: " + str(self.defense) + "\n"