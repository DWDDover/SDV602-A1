from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio
from player import Player
from item import Item
from location import Location

        
village = Location("Village", {"north": forest, "east": lake, "south": caveMouth}, "enemies" : [], "items" : [])