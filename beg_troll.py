from entity import Entity
from hero import Hero  
import random
class BegTroll(Entity):
    """
    Represents a beginner-level troll enemy in the game.
    Attributes:
    <<get>> _name: str
    The name of the troll.
    <<get>> _hp: int
    The current health points of the troll.
    """
    def __init__(self, name):
        """
        Initializes the BegTroll object with a name and random health points.

        Args:
            name (str): The name of the troll.
        """
        # Call the parent constructor with the troll's name and random HP
        super().__init__(name, random.randint(8,10))
    def melee_attack(self, enemy: Hero):
        """
        Performs a melee attack on the hero.

        Args:
            enemy (Hero): The hero being attacked.

        Returns:
            str: A message describing the melee attack and the damage dealt.
        """
        # Calculate damage
        dmg = random.randint(5,9)
        # Inflict damage
        enemy.take_damage(dmg)
        # Return a description
        return f"{self._name} slams {enemy._name} for {dmg} damage"