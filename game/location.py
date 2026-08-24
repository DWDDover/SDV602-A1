class Location:
    
    def __init__(self, name: str, description : str, directions: dict, enemies: list, items: list):
        self.name = name
        self.description = description
        self.directions = directions
        self.enemies = enemies
        self.items = items