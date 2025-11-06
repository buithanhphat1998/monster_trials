from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
import random
class ExpertFactory(EnemyFactory):
    """
    Represents a factory for creating advanced enemies (Expert level).
    Inherits from:
        EnemyFactory: A base class for enemy factories.
    """
    def create_random_enemy(self):
        """
        Creates a random expert-level enemy.

        Returns:
            ExpGoblin or ExpTroll: An instance of either an advanced goblin or troll.
        """
        # Randomly choose between creating an ExpGoblin or ExpTroll.
        match random.randint(0,1): 
            case 0: 
            # Create and return an advanced goblin with the name "Angry Goblin".
                return ExpGoblin("Angry Goblin")
            case 1:
            # Create and return an advanced troll with the name "Angry Troll".
                return ExpTroll("Angry Troll")