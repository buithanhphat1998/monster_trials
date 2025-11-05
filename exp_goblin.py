from entity import Entity
from hero  import Hero
import random
class ExpGoblin(Entity): 
    def __init__(self, name):
        super().__init__(name, random.randint(12,15))
    def melee_attack(self, enemy: Hero):
        dmg = random.randint(5,8)
        enemy.take_damage(dmg)
        return f"{self._name} bites {enemy._name} for {dmg} damage"