import random
from entity import Entity
from hero import Hero

class BegGoblin(Entity):
    """
    Represents a beginner-level goblin enemy in the game.
    Attributes:
    <<get>> _name: str
    The name of the goblin.
    <<get>> _hp: int
    The current health points of the goblin.
    """
    def __init__(self, name):
        """
        Initializes the BegGoblin object with a name and random health points.

        Args:
            name (str): The name of the goblin.
        """
        # Call the parent constructor with the goblin's name and random HP
        super().__init__(name, random.randint(7,9))
    def melee_attack(self, enemy: Hero):
        """
        Performs a melee attack on the hero.

        Args:
            enemy (Hero): The hero being attacked.

        Returns:
            str: A message describing the melee attack and the damage dealt.
        """
        # Calculate damage
        dmg = random.randint(4,6)
        # Inflict damage on the hero.
        enemy.take_damage(dmg)
        # Return a description
        return f"{self._name} bites {enemy._name} for {dmg} damage"