from player import Player
from enemy import Enemy
import random

class Combat:
    def __init__(self, player : Player, enemy : Enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        block_chance = self.player.defense * 0.10
        #start combat lg to be returned at the end
        combat_log = [f"You engage the {self.enemy.name}"]
        #loops until either player or enemy dead
        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            #player attacks first
            self.enemy.current_hp = self.enemy.current_hp - self.player.attack
            combat_log.append(f"You hit for {self.player.attack} damage. the enemy has {self.enemy.current_hp} HP")
            
            if self.enemy.current_hp <= 0:
                break
            #check for block based on player defense
            if random.random() < block_chance:
                combat_log.append(f"You block the {self.enemy.name}'s attack! You take no damage.")
            else:
                self.player.current_hp = self.player.current_hp - self.enemy.damage
                combat_log.append(f"The enemy hits you for {self.enemy.damage} damage. you have {self.player.current_hp} HP")
        #combat continues until player wins or dies
        if self.player.current_hp <= 0:
            combat_log.append("You have died")
            outcome = "lose"
        else:
            combat_log.append("You have defeated the enemy")
            outcome = "win"

        return {"log": combat_log, "outcome": outcome}