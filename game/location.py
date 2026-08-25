class Location:
    
    def __init__(self, name: str, description : str, directions: dict, enemies: list, items: list, image: str):
        self.name = name
        self.description = description
        self.directions = directions
        self.enemies = enemies
        self.items = items
        self.image = image