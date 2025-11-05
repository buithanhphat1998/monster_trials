from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
import random
class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        match random.randint(0,1): 
            case 0: 
                return ExpGoblin("Angry Goblin")
            case 1: 
                return ExpTroll("Angry Troll")