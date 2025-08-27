import TemplateSaveData
import random
Battlechoice = "None"
BattlePokemonStats = []
def battlecode(Battletype, Potions, Balls, Coins, ChosenPokemon, Name, Level, Xp, XpToNextLevel, RivalName, Rivalpokemon, Pokemontype, Pokemonstats, Rivalstats, Moves, AvaliableAttacks):
    if Battletype == "Rival":
        print("This is a battle against your Rival!")
        print("But rival battles are not implemented yet.")
        print("Returning to main game...")
        if Pokemonstats['Speed'] >= Rivalstats['Speed']:
            print(f"{ChosenPokemon} is faster and attacks first!")
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                    move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
    
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage //=2 
                            print("It's not very effective...")
                        else:
                            damage //= 1
                        Rivalstats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {Rivalpokemon}.")
                        if Rivalstats['HP'] <= 0:
                            print(f"{Rivalpokemon} fainted!")
                            return 0
                        else:
                            print(f"{Rivalpokemon} has {Rivalstats['HP']} HP left.")
                            damage_to_player = (Rivalstats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{Rivalpokemon} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                elif battlepick.lower() == "heal":
                    if Potions > 0:
                        heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                        Pokemonstats['HP'] += heal_amount
                        Potions -= 1
                        print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                    else:
                        print("No potions left!")
                elif battlepick.lower() == "run":
                    print("You ran away safely!")
                    Picking = False
                    return 1
                else:
                    print("Invalid choice. Try again.")

        elif Rivalstats['Speed'] > Pokemonstats['Speed']:
            print(f"{Rivalpokemon} is faster and attacks first!")
            damage_to_player = (Rivalstats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
            Pokemonstats['HP'] -= damage_to_player
            print(f"{Rivalpokemon} attacked and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
            if Pokemonstats['HP'] <= 0:
                print(f"{ChosenPokemon} fainted!")
                return 1
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                    move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage //=2 
                            print("It's not very effective...")
                        else:
                            damage //= 1
                        Rivalstats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {Rivalpokemon}.")
                        if Rivalstats['HP'] <= 0:
                            print(f"{Rivalpokemon} fainted!")
                            Picking = False
                            return 0
                        else:
                            print(f"{Rivalpokemon} has {Rivalstats['HP']} HP left.")
                            damage_to_player = (Rivalstats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{Rivalpokemon} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                Picking = False
                                return 1
                elif battlepick.lower() == "heal":
                    if Potions > 0:
                        heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                        Pokemonstats['HP'] += heal_amount
                        Potions -= 1
                        print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                    else:
                        print("No potions left!")
                elif battlepick.lower() == "run": 
                    print("You ran away safely!")
                    Picking = False
                    return 1
                else:
                    print("Invalid choice. Try again.")
    else:
        BattleChoice = random.choice(TemplateSaveData.BattlePokemon)
        if BattleChoice == "Pidgey":
            BattlePokemonStats = TemplateSaveData.PidgeyStats
        elif BattleChoice == "Rattata":
            BattlePokemonStats = TemplateSaveData.RattataStats
        elif BattleChoice == "Caterpie":
            BattlePokemonStats = TemplateSaveData.CaterpieStats
        elif BattleChoice == "Weedle":
            BattlePokemonStats = TemplateSaveData.WeedleStats
        else:
            BattlePokemonStats = TemplateSaveData.SpearowStats
        print(f"A wild {BattleChoice} appeared!")
        if Pokemonstats['Speed'] >= BattlePokemonStats['Speed']:
            print(f"{ChosenPokemon} is faster and attacks first!")
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                    move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage //=2 
                            print("It's not very effective...")
                        else:
                            damage //= 1
                        BattlePokemonStats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {BattleChoice}.")
                        if BattlePokemonStats['HP'] <= 0:
                            print(f"{BattleChoice} fainted!")
                            return 0
                        else:
                            print(f"{BattleChoice} has {BattlePokemonStats['HP']} HP left.")
                            damage_to_player = (BattlePokemonStats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{BattleChoice} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                elif battlepick.lower() == "heal":
                    if Potions > 0:
                        heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                        Pokemonstats['HP'] += heal_amount
                        Potions -= 1
                        print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                    else:
                        print("No potions left!")
                elif battlepick.lower() == "run":
                    print("You ran away safely!")
                    Picking = False
                    return 1

                elif battlepick.lower() == "heal":
                    if Potions > 0:
                        heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                        Pokemonstats['HP'] += heal_amount
                        Potions -= 1
                        print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                    else:
                        print("No potions left!")
                else:
                    print("Invalid action. Try again.")
        else:
            print(f"{BattleChoice} is faster and attacks first!")
            damage_to_player = (BattlePokemonStats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
            Pokemonstats['HP'] -= damage_to_player
            print(f"{BattleChoice} attacked and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
            if Pokemonstats['HP'] <= 0:
                print(f"{ChosenPokemon} fainted!")
                return 1
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                    move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage //=2 
                            print("It's not very effective...")
                        else:
                            damage //= 1
                        BattlePokemonStats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {BattleChoice}.")
                        if BattlePokemonStats['HP'] <= 0:
                            print(f"{BattleChoice} fainted!")
                            Picking = False
                            return 0
                        else:
                            print(f"{BattleChoice} has {BattlePokemonStats['HP']} HP left.")
                            damage_to_player = (BattlePokemonStats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{BattleChoice} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                Picking = False
                                return 1
                elif battlepick.lower() == "heal":
                    if Potions > 0:
                        heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                        Pokemonstats['HP'] += heal_amount
                        Potions -= 1
                        print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                    else:
                        print("No potions left!")
                elif battlepick.lower() == "run": 
                    print("You ran away safely!")
                    Picking = False
                    return 1
                else:
                    print("Invalid move choice. Try again.")
