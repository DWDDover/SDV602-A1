class Location:
    
    def __init__(self, name: str, directions: dict, enemies: list, items: list):
        self.name = name
        self.directions = directions
        self.enemies = enemies
        self.items = items