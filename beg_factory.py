import random 
from beg_goblin import BegGoblin
from beg_troll import BegTroll
from enemy_factory import EnemyFactory
class BeginnerFactory(EnemyFactory):
    """
    Represents a factory for creating beginner-level enemies.
    Inherits from:
        EnemyFactory: A base class for enemy factories.
    """
    def create_random_enemy(self):
        """
        Creates a random beginner-level enemy.

        Returns:
            BegGoblin or BegTroll: An instance of either a beginner goblin or troll.
        """
        # Randomly choose between creating a BegGoblin or BegTroll.
        match random.randint(0,1): 
            case 0: 
                # Create and return a beginner goblin with the name "Goblin".
                return BegGoblin("Goblin")
            case 1: 
                # Create and return a beginner troll with the name "Troll".
                return BegTroll("Troll")