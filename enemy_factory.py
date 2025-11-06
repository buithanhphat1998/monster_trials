from abc import ABC, abstractmethod
from entity import Entity
"""
    Represents an abstract base class for enemy factories.
    This class defines the blueprint for creating enemy objects.
"""
class EnemyFactory(ABC): 
    def create_random_enemy(self) -> Entity: 
        """
        Abstract method for creating a random enemy.

        Returns:
            Entity: An instance of an enemy.
        """
        pass