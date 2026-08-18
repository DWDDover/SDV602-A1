from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio

class Location:
    
    def __init__(self, name: str, directions: dict, enemies: list, items: list):
        self.name = name
        self.directions = directions
        self.enemies = enemies
        self.items = items
        
village = Location("Village", {"north": forest, "east": lake, "south": caveMouth}, "enemies" : [], "items" : [])