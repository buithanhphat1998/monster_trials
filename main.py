"""
CECS 277 – Lab 11 – Factory
11/05/2025

Group 4
Group members:
Thanh Phat Bui
Ha Gia Bao Hoang

Description: 
Monster Trials
Create a game where the user must defeat three monsters to pass the trials. Use the following
UML diagram and the method descriptions below to create your program.
"""
from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory
import check_input
def main():
    # Display the game title.
    print("Monster Trials")

    # Prompt the player for their name and create a Hero object.
    name = input("What is your name? ")
    player = Hero(name)
    
     # Inform the player about the game objective.
    print(f"You will face a series of 3 monsters, {player.name}.")
    print("Defeat them all to win")

    # Create a list of monsters
    monsters = [BeginnerFactory().create_random_enemy(), BeginnerFactory().create_random_enemy(), ExpertFactory().create_random_enemy()]

    # Game loop: Continue while the player is alive and monsters remain.
    while player.hp > 0 and len(monsters) > 0: 
        # Display the list of monsters and prompt the player to choose one to attack.
        print("Choose an enemy to attack:")
        for index, value in enumerate(monsters):
            print(f"{index+1}. {value}")
        option = check_input.get_int_range("Enter choice: ",1,len(monsters))
        option -= 1 # Adjust for zero-based indexing.

        # Display the player's status and attack options.
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        weapon = check_input.get_int_range("Enter choice: ",1,2)
        print()

        # Handle the player's attack based on their weapon choice.
        match weapon: 
            case 1: 
                print(player.melee_attack(monsters[option]))
            case 2: 
                print(player.ranged_attack(monsters[option]))
        # Check if the attacked monster is defeated.
        if(not monsters[option].hp):
            print(f"You have slain the {monsters[option].name}")
            print()
            monsters.pop(option) # Remove the defeated monster from the list.
        else:
            # The monster attacks the player if it is still alive.
            print(monsters[option].melee_attack(player))
    # Check the game outcome and display the appropriate message.
    if(not player.hp):
        print("Sorry, you lose...")
    else: 
        print("Congratulations! You defeated all three monsters")
     # End the game.
    print("Game Over")

if __name__ == "__main__":
    main()