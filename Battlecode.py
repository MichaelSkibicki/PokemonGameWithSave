import TemplateSaveData
import random
import time
# Add Oppenents to have moves intead of fixed damage, each with their own moves
Battlechoice = "None"
BattlePokemonStats = []
def battlecode(Battletype, Potions, Balls, Coins, ChosenPokemon, Name, Level, Xp, XpToNextLevel, RivalName, Rivalpokemon, Pokemontype, Pokemonstats, Rivalstats, Moves, AvaliableAttacks):
    if Battletype == "Rival":
        if Pokemonstats['Speed'] >= Rivalstats['Speed']:
            time.sleep(0.5)
            print(f"{ChosenPokemon} is faster and attacks first!")
            time.sleep(0.5)
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                        time.sleep(0.5)
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        time.sleep(0.5)
    
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                  
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage *= 2
                     

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:
                                damage //= 2
                        
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            damage //= 2
                  
                        else:
                            damage //= 1
                        Rivalstats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {Rivalpokemon}.")
                        time.sleep(0.5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                print("It's super effective!")

                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            print("It's super effective!")

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:

                                print("It's not very effective...")
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            
                            print("It's not very effective...")
                        time.sleep(0.5)
                        if Rivalstats['HP'] <= 0:
                            print(f"{Rivalpokemon} fainted!")
                            time.sleep(0.5)
                            return 0
                        else:
                            print(f"{Rivalpokemon} has {Rivalstats['HP']} HP left.")
                            time.sleep(0.5)
                            damage_to_player = (Rivalstats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{Rivalpokemon} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            time.sleep(0.5)
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                            
                    else:
                        print("Invalid move choice. Try again.")
                elif battlepick.lower() == "heal":
                    if Pokemonstats["HP"] <= 0:
                        print(f"{ChosenPokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                            Pokemonstats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                            time.sleep(0.5)
                        else:
                            print("No potions left!")
                            time.sleep(0.5)
                elif battlepick.lower() == "run":
                    print("You ran away safely!")
                    time.sleep(0.5)
                    Picking = False
                    return 1
                else:
                    print("Invalid choice. Try again.")

        elif Rivalstats['Speed'] > Pokemonstats['Speed']:
            print(f"{Rivalpokemon} is faster and attacks first!")
            time.sleep(0.5)
            damage_to_player = (Rivalstats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
            Pokemonstats['HP'] -= damage_to_player
            print(f"{Rivalpokemon} attacked and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
            time.sleep(0.5)
            if Pokemonstats['HP'] <= 0:
                print(f"{ChosenPokemon} fainted!")
                time.sleep(0.5)
                return 1
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                        time.sleep(0.5)
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                            
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage *= 2
                           
                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:
                                damage //= 2
                         
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            damage //= 2
                       
                        else:
                            damage //= 1
                        Rivalstats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {Rivalpokemon}.")
                        time.sleep(0.5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            print("It's super effective!")

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:

                                print("It's not very effective...")
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                        
                            print("It's not very effective...")
                        time.sleep(0.5)
                        if Rivalstats['HP'] <= 0:
                            print(f"{Rivalpokemon} fainted!")
                            time.sleep(0.5)
                            Picking = False
                            return 0
                    
                        else:
                            print(f"{Rivalpokemon} has {Rivalstats['HP']} HP left.")
                            time.sleep(0.5)
                            damage_to_player = (Rivalstats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{Rivalpokemon} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            time.sleep(0.5)
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                        time.sleep(0.5)
                elif battlepick.lower() == "heal":
                    if Pokemonstats["HP"] <= 0:
                        print(f"{ChosenPokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                            Pokemonstats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                            time.sleep(0.5)
                        else:
                            print("No potions left!")
                            time.sleep(0.5)
                elif battlepick.lower() == "run": 
                    print("You ran away safely!")
                    time.sleep(0.5)
                    Picking = False
                    return 1
                else:
                    print("Invalid choice. Try again.")
                    time.sleep(0.5)
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
        time.sleep(0.5)
        if Pokemonstats['Speed'] >= BattlePokemonStats['Speed']:
            print(f"{ChosenPokemon} is faster and attacks first!")
            time.sleep(0.5)
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                             
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage *= 2
                       

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:
                                damage //= 2
                       
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            damage //= 2
                         
                        else:
                            damage //= 1
                        BattlePokemonStats['HP'] -= damage
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {BattleChoice}.")
                        time.sleep(0.5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            print("It's super effective!")

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:

                                print("It's not very effective...")
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            
                            print("It's not very effective...")
                        time.sleep(0.5)
                        if BattlePokemonStats['HP'] <= 0:
                            print(f"{BattleChoice} fainted!")
                            time.sleep(0.5)
                            return 0
                        else:
                            print(f"{BattleChoice} has {BattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            damage_to_player = (BattlePokemonStats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{BattleChoice} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            time.sleep(0.5)
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                        time.sleep(0.5)
                elif battlepick.lower() == "heal":
                    if Pokemonstats["HP"] <= 0:
                        print(f"{ChosenPokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                            Pokemonstats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                            
                            time.sleep(0.5)
                        else:
                            print("No potions left!")
                            time.sleep(0.5)
                elif battlepick.lower() == "run":
                    print("You ran away safely!")
                    time.sleep(0.5)
                    Picking = False
                    return 1

                elif battlepick.lower() == "heal":
                    if Pokemonstats["HP"] <= 0:
                        print(f"{ChosenPokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                            Pokemonstats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                            time.sleep(0.5)
                        else:
                            print("No potions left!")
                            time.sleep(0.5)
                else:
                    print("Invalid action. Try again.")
                    time.sleep(0.5)
        else:
            print(f"{BattleChoice} is faster and attacks first!")
            time.sleep(0.5)
            damage_to_player = (BattlePokemonStats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
            Pokemonstats['HP'] -= damage_to_player
            print(f"{BattleChoice} attacked and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
            time.sleep(0.5)
            if Pokemonstats['HP'] <= 0:
                print(f"{ChosenPokemon} fainted!")
                time.sleep(0.5)
                return 1
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(AvaliableAttacks):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                        time.sleep(0.5)
                    
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                    if 0 <= move_choice < len(AvaliableAttacks):
                        chosen_move = AvaliableAttacks[move_choice]
                        damage = chosen_move['Power']//10 + (Pokemonstats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                damage *= 2
                
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            damage *= 2
                

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:
                                damage //= 2
                            
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            damage //= 2

                        else:
                            damage //= 1
                        BattlePokemonStats['HP'] -= damage
                        
                        print(f"{ChosenPokemon} used {chosen_move['Name']}! It dealt {damage} damage to {BattleChoice}.")
                        if isinstance(Rivalstats['Weakness'], list):
                            if chosen_move['Type'] in Rivalstats['Weakness']:
                                print("It's super effective!")
                        elif chosen_move['Type'] == Rivalstats['Weakness']:
                            print("It's super effective!")

                        # Check for resistance
                        if isinstance(Rivalstats['Resistance'], list):
                            if chosen_move['Type'] in Rivalstats['Resistance']:

                                print("It's not very effective...")
                        elif chosen_move['Type'] == Rivalstats['Resistance']:
                            
                            print("It's not very effective...")
                        time.sleep(0.5)
                        if BattlePokemonStats['HP'] <= 0:
                            print(f"{BattleChoice} fainted!")
                            time.sleep(0.5)
                            Picking = False
                            return 0
                        else:
                            print(f"{BattleChoice} has {BattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            damage_to_player = (BattlePokemonStats['Attack'] // 3) - (Pokemonstats['Defense'] // 5)
                            Pokemonstats['HP'] -= damage_to_player
                            print(f"{BattleChoice} attacked back and dealt {damage_to_player} damage! {ChosenPokemon} now has {Pokemonstats['HP']} HP left.")
                            time.sleep(0.5)
                            if Pokemonstats['HP'] <= 0:
                                print(f"{ChosenPokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                        time.sleep(0.5)
                elif battlepick.lower() == "heal":
                    if Pokemonstats["HP"] <= 0:
                        print(f"{ChosenPokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, Pokemonstats['MaxHP'] - Pokemonstats['HP'])
                            Pokemonstats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenPokemon} healed for {heal_amount} HP and now has {Pokemonstats['HP']} HP. Potions left: {Potions}")
                            time.sleep(0.5)
                        else:
                            print("No potions left!")
                            time.sleep(0.5)
                elif battlepick.lower() == "run": 
                    print("You ran away safely!")
                    time.sleep(0.5)
                    Picking = False
                    return 1
                else:
                    print("Invalid move choice. Try again.")
                    time.sleep(0.5)
