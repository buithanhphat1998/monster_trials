from entity import Entity
from hero import Hero
import random
class ExpTroll(Entity): 
    def __init__(self, name):
        super().__init__(name, random.randint(15,18))
    def melee_attack(self, enemy: Hero):
        dmg = random.randint(8,12)
        enemy.take_damage(dmg)
        return f"{self._name} slams {enemy._name} for {dmg} damage"