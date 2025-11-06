from entity import Entity
import random

class Hero(Entity):
    """
    Represents the hero character controlled by the player.
    Attributes:
    <<get>> _name: str
    The name of the hero.
    <<get>> _hp: int
    The current health points of the hero.
    """    
    def __init__(self, name):
        """
        Initializes the Hero object.

        Args:
            name (str): The name of the hero.
        """
        # Call the parent constructor with the hero's name and set HP
        super().__init__(name, 20)
    
    def melee_attack(self, enemy):
        """
        Performs a melee attack on an enemy.

        Args:
            enemy (Entity): The enemy being attacked.

        Returns:
            str: A message describing the melee attack and the damage dealt.
        """
        # Calculate damage
        dmg = random.randint(1,6) + random.randint(1,6)
        # Inflict damage on the enemy.
        enemy.take_damage(dmg)
        # Return a description of the attack.
        return f"{self._name} slashes a {enemy.name} with a sword for {dmg} damage"
    
    def ranged_attack(self,enemy): 
        """
        Performs a ranged attack on an enemy.

        Args:
            enemy (Entity): The enemy being attacked.

        Returns:
            str: A message describing the ranged attack and the damage dealt.
        """
        # Calculate damage as a random roll between 1 and 12.
        dmg = random.randint(1,12)
        # Inflict damage on the enemy.
        enemy.take_damage(dmg)
        # Return a description of the attack.
        return f"{self._name} pierces a {enemy.name} with an arrow for {dmg} damage"