from abc import ABC, abstractmethod

class Entity(ABC):
    """
    Represents an abstract base class for all entities in the game.
    Attributes:
    <<get>> _name: str
    The name of the entity.
    <<get>> _hp: int
    The current health points of the entity.
    """
    def __init__(self, name, hp):
        """
        Initializes the Entity object.

        Args:
            name (str): The name of the entity.
            hp (int): The initial health points of the entity.
        """
        self._name = name # Set the name of the entity.
        self._hp = hp # Set the initial health points of the entity.
    
    @property
    def name(self):
        """
        Returns the name of the entity.

        Returns:
            str: The name of the entity.
        """
        return self._name
    
    @property
    def hp(self):
        """
        Returns the current health points of the entity.

        Returns:
            int: The current health points.
        """
        return self._hp
    
    def take_damage(self, dmg):
        """
        Reduces the entity's health points by the specified damage amount.

        Args:
            dmg (int): The amount of damage to inflict.
        """
        self._hp -= dmg # Subtract the damage from the entity's health points.
        if(self._hp < 0): 
            self._hp = 0 # Ensure health points do not drop below zero

    def __str__(self):
        """
        Returns a string representation of the entity.

        Returns:
            str: A string showing the entity's name and current health points.
        """
        return f"{self._name} HP: {self._hp}"

    @abstractmethod
    def melee_attack(self,enemy) -> str: 
        """
        Abstract method for performing a melee attack on another entity.

        Args:
            enemy (Entity): The entity being attacked.

        Returns:
            str: A message describing the attack.
        """
        pass