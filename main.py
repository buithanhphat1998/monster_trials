from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory
import check_input
def main():
    print("Monster Trials")
    name = input("What is your name? ")
    player = Hero(name)
    
    print(f"You will face a series of 3 monsters, {player.name}.")
    print("Defeat them all to win")
    monsters = [BeginnerFactory().create_random_enemy(), BeginnerFactory().create_random_enemy(), ExpertFactory().create_random_enemy()]

    while player.hp > 0 and len(monsters) > 0: 
        print("Choose an enemy to attack:")
        for index, value in enumerate(monsters):
            print(f"{index+1}. {value}")
        option = check_input.get_int_range("Enter choice: ",1,len(monsters))
        option -= 1

        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        weapon = check_input.get_int_range("Enter choice: ",1,2)
        print()

        match weapon: 
            case 1: 
                print(player.melee_attack(monsters[option]))
            case 2: 
                print(player.ranged_attack(monsters[option]))
        if(not monsters[option].hp):
            print(f"You have slain the {monsters[option].name}")
            print()
            monsters.pop(option)
        else:
            print(monsters[option].melee_attack(player))
    if(not player.hp):
        print("Sorry, you lose...")
    else: 
        print("Congratulations! You defeated all three monsters")
    print("Game Over")

if __name__ == "__main__":
    main()