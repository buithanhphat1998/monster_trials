import random 
from beg_goblin import BegGoblin
from beg_troll import BegTroll
from enemy_factory import EnemyFactory
class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        match random.randint(0,1): 
            case 0: 
                return BegGoblin("Goblin")
            case 1: 
                return BegTroll("Troll")