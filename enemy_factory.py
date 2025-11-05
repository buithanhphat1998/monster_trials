from abc import ABC, abstractmethod
from entity import Entity
class EnemyFactory(ABC): 
    def create_random_enemy(self) -> Entity: 
        pass