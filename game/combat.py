from player import Player
from enemy import Enemy

class Combat:
    def __init__(self, player : Player, enemy : Enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        combat_log = [f"You engage the {self.enemy.name}"]
        
        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            self.enemy.current_hp = self.enemy.current_hp - self.player.attack
            combat_log.append(f"You hit for {self.player.attack} damage. the enemy has {self.enemy.current_hp} HP")
            
            if self.enemy.current_hp <= 0:
                break
            
            self.player.current_hp = self.player.current_hp - self.enemy.damage
            combat_log.append(f"The enemy hits you for {self.enemy.damage} damage you have {self.player.current_hp} HP")
            
            if self.player.current_hp <= 0:
                combat_log.append("You have died")
                outcome = "lose"
                
            else:
                combat_log.append("You have defeated the enemy")
                outcome = "win"
                
            return {"log": combat_log, "outcome" : outcome}