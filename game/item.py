class Item:
    def __init__(self, name, slot, heal=0, damage=0, block=0, ):
        self.name = name
        self.heal = heal
        self.block = block
        self.damage = damage
        self.slot = slot
        self.used = False
        self.equipped = False
