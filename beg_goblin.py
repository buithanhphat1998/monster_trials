import random
from entity import Entity
from hero import Hero

class BegGoblin(Entity): 
    def __init__(self, name):
        super().__init__(name, random.randint(7,9))
    def melee_attack(self, enemy: Hero):
        dmg = random.randint(4,6)
        enemy.take_damage(dmg)
        return f"{self._name} bites {enemy._name} for {dmg} damage"