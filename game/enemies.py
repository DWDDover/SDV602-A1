from enemy import Enemy
from items import helmet, key, magic_orb

rat = Enemy("Rat", "Rat with a helmet on", 20, 20, 2, helmet, "./images/rat.png")

goblin = Enemy("Goblin", "Goblin with a key around its neck", 30, 30, 4, key, "./images/goblin.png")

wizard = Enemy("Wizard", "Wizard surrounded by swirling fire", 70, 70, 100, magic_orb, "./images/wizard.png")