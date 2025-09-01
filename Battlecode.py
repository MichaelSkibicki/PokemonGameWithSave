import TemplateSaveData
import random
import time
# Add Oppenents to have moves intead of fixed damage, each with their own moves
Battlechoice = "None"
ChosenBattlePokemonStats = []
def battlecode(Battletype, Potions, Balls, Coins, ChosenPokemon, Name, Level, Xp, XpToNextLevel, RivalName, Rivalpokemon, Pokemontype, Pokemonstats, Rivalstats, Moves, AvaliableAttacks, PokemonOnTeam, SecondPokemon, SecondPokemonStats, SecondPokemonMoves):
    print("We havent added the ability to switch out pokemon yet, but it will be added")
    print("These Are Your Availiable Pokemon To Pick For Battle:")
    Picking = True
    while Picking:
        for i, pokemon in enumerate(PokemonOnTeam):
            print(f"  {i + 1}. {pokemon}")
            time.sleep(0.5)
        ChosenBattlePokemon = input("Which Pokemon do you want? Enter the number corresponding to the pokemon. ")
        if ChosenBattlePokemon.isdigit():
            index = int(ChosenBattlePokemon) - 1 # Convert to integer and adjust for 0-based indexing
            if 0 <= index < len(PokemonOnTeam):
                chosen_pokemon = PokemonOnTeam[index]
                print(f"You chose {chosen_pokemon}!")
                if PokemonOnTeam[index] == ChosenPokemon:
                    ChosenBattlePokemonStats = Pokemonstats
                    ChosenBattlePokemon = ChosenPokemon
                    ChosenBattlePokemonMoves = AvaliableAttacks
                elif PokemonOnTeam[index] == SecondPokemon:
                    ChosenBattlePokemonStats = SecondPokemonStats
                    ChosenBattlePokemon = SecondPokemon
                    ChosenBattlePokemonMoves = SecondPokemonMoves
                Picking = False # Exit the loop after a valid choice
            else:
                print("Invalid number. Please choose a number from the list.")
        else:
            print("Invalid input. Please enter a number.")
            
    if Battletype == "Rival":
        if ChosenBattlePokemonStats['Speed'] >= Rivalstats['Speed']:
            time.sleep(0.5)
            print(f"{ChosenBattlePokemon} is faster and attacks first!")
            time.sleep(0.5)
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(ChosenBattlePokemonMoves):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                        time.sleep(0.5)
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                    if 0 <= move_choice < len(ChosenBattlePokemonMoves):
                        chosen_move = ChosenBattlePokemonMoves[move_choice]
                        time.sleep(0.5)
    
                        damage = chosen_move['Power']//10 + (ChosenBattlePokemonStats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
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
                        print(f"{ChosenBattlePokemon} used {chosen_move['Name']}! It dealt {damage} damage to {Rivalpokemon}.")
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
                            damage_to_player = (Rivalstats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
                            ChosenBattlePokemonStats['HP'] -= damage_to_player
                            print(f"{Rivalpokemon} attacked back and dealt {damage_to_player} damage! {ChosenBattlePokemon} now has {ChosenBattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            if ChosenBattlePokemonStats['HP'] <= 0:
                                print(f"{ChosenBattlePokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                            
                    else:
                        print("Invalid move choice. Try again.")
                elif battlepick.lower() == "heal":
                    if ChosenBattlePokemonStats["HP"] <= 0:
                        print(f"{ChosenBattlePokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    elif ChosenBattlePokemonStats['HP'] == ChosenBattlePokemonStats['MaxHP']:
                        print(f"{ChosenBattlePokemon} is a full health and cannot be healed")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, ChosenBattlePokemonStats['MaxHP'] - ChosenBattlePokemonStats['HP'])
                            ChosenBattlePokemonStats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenBattlePokemon} healed for {heal_amount} HP and now has {ChosenBattlePokemonStats['HP']} HP. Potions left: {Potions}")
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

        elif Rivalstats['Speed'] > ChosenBattlePokemonStats['Speed']:
            print(f"{Rivalpokemon} is faster and attacks first!")
            time.sleep(0.5)
            damage_to_player = (Rivalstats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
            ChosenBattlePokemonStats['HP'] -= damage_to_player
            print(f"{Rivalpokemon} attacked and dealt {damage_to_player} damage! {ChosenBattlePokemon} now has {ChosenBattlePokemonStats['HP']} HP left.")
            time.sleep(0.5)
            if ChosenBattlePokemonStats['HP'] <= 0:
                print(f"{ChosenBattlePokemon} fainted!")
                time.sleep(0.5)
                return 1
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(ChosenBattlePokemonMoves):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                        time.sleep(0.5)
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                    if 0 <= move_choice < len(ChosenBattlePokemonMoves):
                        chosen_move = ChosenBattlePokemonMoves[move_choice]
                        damage = chosen_move['Power']//10 + (ChosenBattlePokemonStats['Attack'] // 3) - (Rivalstats['Defense'] // 5)
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
                        print(f"{ChosenBattlePokemon} used {chosen_move['Name']}! It dealt {damage} damage to {Rivalpokemon}.")
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
                            damage_to_player = (Rivalstats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
                            ChosenBattlePokemonStats['HP'] -= damage_to_player
                            print(f"{Rivalpokemon} attacked back and dealt {damage_to_player} damage! {ChosenBattlePokemon} now has {ChosenBattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            if ChosenBattlePokemonStats['HP'] <= 0:
                                print(f"{ChosenBattlePokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                        time.sleep(0.5)
                elif battlepick.lower() == "heal":
                    if ChosenBattlePokemonStats["HP"] <= 0:
                        print(f"{ChosenBattlePokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    elif ChosenBattlePokemonStats['HP'] == ChosenBattlePokemonStats['MaxHP']:
                        print(f"{ChosenBattlePokemon} is a full health and cannot be healed")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, ChosenBattlePokemonStats['MaxHP'] - ChosenBattlePokemonStats['HP'])
                            ChosenBattlePokemonStats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenBattlePokemon} healed for {heal_amount} HP and now has {ChosenBattlePokemonStats['HP']} HP. Potions left: {Potions}")
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
            ChosenBattlePokemonStats = TemplateSaveData.PidgeyStats
        elif BattleChoice == "Rattata":
            ChosenBattlePokemonStats = TemplateSaveData.RattataStats
        elif BattleChoice == "Caterpie":
            ChosenBattlePokemonStats = TemplateSaveData.CaterpieStats
        elif BattleChoice == "Weedle":
            ChosenBattlePokemonStats = TemplateSaveData.WeedleStats
        else:
            ChosenBattlePokemonStats = TemplateSaveData.SpearowStats
        print(f"A wild {BattleChoice} appeared!")
        time.sleep(0.5)
        if ChosenBattlePokemonStats['Speed'] >= ChosenBattlePokemonStats['Speed']:
            print(f"{ChosenBattlePokemon} is faster and attacks first!")
            time.sleep(0.5)
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(ChosenBattlePokemonMoves):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                
                    if 0 <= move_choice < len(ChosenBattlePokemonMoves):
                        chosen_move = ChosenBattlePokemonMoves[move_choice]
                        damage = chosen_move['Power']//10 + (ChosenBattlePokemonStats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
                        if isinstance(ChosenBattlePokemonStats['Weakness'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Weakness']:
                                damage *= 2
                             
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Weakness']:
                            damage *= 2
                       

                        # Check for resistance
                        if isinstance(ChosenBattlePokemonStats['Resistance'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Resistance']:
                                damage //= 2
                       
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Resistance']:
                            damage //= 2
                         
                        else:
                            damage //= 1
                        ChosenBattlePokemonStats['HP'] -= damage
                        print(f"{ChosenBattlePokemon} used {chosen_move['Name']}! It dealt {damage} damage to {BattleChoice}.")
                        time.sleep(0.5)
                        if isinstance(ChosenBattlePokemonStats['Weakness'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Weakness']:
                                print("It's super effective!")
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Weakness']:
                            print("It's super effective!")

                        # Check for resistance
                        if isinstance(ChosenBattlePokemonStats['Resistance'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Resistance']:

                                print("It's not very effective...")
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Resistance']:
                            
                            print("It's not very effective...")
                        time.sleep(0.5)
                        if ChosenBattlePokemonStats['HP'] <= 0:
                            print(f"{BattleChoice} fainted!")
                            time.sleep(0.5)
                            return 0
                        else:
                            print(f"{BattleChoice} has {ChosenBattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            damage_to_player = (ChosenBattlePokemonStats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
                            ChosenBattlePokemonStats['HP'] -= damage_to_player
                            print(f"{BattleChoice} attacked back and dealt {damage_to_player} damage! {ChosenBattlePokemon} now has {ChosenBattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            if ChosenBattlePokemonStats['HP'] <= 0:
                                print(f"{ChosenBattlePokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                        time.sleep(0.5)
                elif battlepick.lower() == "heal":
                    if ChosenBattlePokemonStats["HP"] <= 0:
                        print(f"{ChosenBattlePokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    elif ChosenBattlePokemonStats['HP'] == ChosenBattlePokemonStats['MaxHP']:
                        print(f"{ChosenBattlePokemon} is a full health and cannot be healed")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, ChosenBattlePokemonStats['MaxHP'] - ChosenBattlePokemonStats['HP'])
                            ChosenBattlePokemonStats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenBattlePokemon} healed for {heal_amount} HP and now has {ChosenBattlePokemonStats['HP']} HP. Potions left: {Potions}")
                            
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
                    if ChosenBattlePokemonStats["HP"] <= 0:
                        print(f"{ChosenBattlePokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    elif ChosenBattlePokemonStats['HP'] == ChosenBattlePokemonStats['MaxHP']:
                        print(f"{ChosenBattlePokemon} is a full health and cannot be healed")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, ChosenBattlePokemonStats['MaxHP'] - ChosenBattlePokemonStats['HP'])
                            ChosenBattlePokemonStats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenBattlePokemon} healed for {heal_amount} HP and now has {ChosenBattlePokemonStats['HP']} HP. Potions left: {Potions}")
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
            damage_to_player = (ChosenBattlePokemonStats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
            ChosenBattlePokemonStats['HP'] -= damage_to_player
            print(f"{BattleChoice} attacked and dealt {damage_to_player} damage! {ChosenBattlePokemon} now has {ChosenBattlePokemonStats['HP']} HP left.")
            time.sleep(0.5)
            if ChosenBattlePokemonStats['HP'] <= 0:
                print(f"{ChosenBattlePokemon} fainted!")
                time.sleep(0.5)
                return 1
            Picking = True
            while Picking:
                battlepick = input("What will you do? (Attack, Heal, Run) ")
                time.sleep(0.5)
                if battlepick.lower() == "attack":
                    print("Choose your move:")
                    time.sleep(0.5)
                    for i, move in enumerate(ChosenBattlePokemonMoves):
                        print(f"{i + 1}. {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                        time.sleep(0.5)
                    
                    try:
                        move_choice = int(input("Enter the number of the move you want to use: ")) - 1
                        time.sleep(0.5)
                    except ValueError:
                        print("Please enter a valid number.")
                        time.sleep(0.5)
                        continue
                    if 0 <= move_choice < len(ChosenBattlePokemonMoves):
                        chosen_move = ChosenBattlePokemonMoves[move_choice]
                        damage = chosen_move['Power']//10 + (ChosenBattlePokemonStats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
                        if isinstance(ChosenBattlePokemonStats['Weakness'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Weakness']:
                                damage *= 2
                
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Weakness']:
                            damage *= 2
                

                        # Check for resistance
                        if isinstance(ChosenBattlePokemonStats['Resistance'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Resistance']:
                                damage //= 2
                            
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Resistance']:
                            damage //= 2

                        else:
                            damage //= 1
                        ChosenBattlePokemonStats['HP'] -= damage
                        
                        print(f"{ChosenBattlePokemon} used {chosen_move['Name']}! It dealt {damage} damage to {BattleChoice}.")
                        if isinstance(ChosenBattlePokemonStats['Weakness'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Weakness']:
                                print("It's super effective!")
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Weakness']:
                            print("It's super effective!")

                        # Check for resistance
                        if isinstance(ChosenBattlePokemonStats['Resistance'], list):
                            if chosen_move['Type'] in ChosenBattlePokemonStats['Resistance']:

                                print("It's not very effective...")
                        elif chosen_move['Type'] == ChosenBattlePokemonStats['Resistance']:
                            
                            print("It's not very effective...")
                        time.sleep(0.5)
                        if ChosenBattlePokemonStats['HP'] <= 0:
                            print(f"{BattleChoice} fainted!")
                            time.sleep(0.5)
                            Picking = False
                            return 0
                        else:
                            print(f"{BattleChoice} has {ChosenBattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            damage_to_player = (ChosenBattlePokemonStats['Attack'] // 3) - (ChosenBattlePokemonStats['Defense'] // 5)
                            ChosenBattlePokemonStats['HP'] -= damage_to_player
                            print(f"{BattleChoice} attacked back and dealt {damage_to_player} damage! {ChosenBattlePokemon} now has {ChosenBattlePokemonStats['HP']} HP left.")
                            time.sleep(0.5)
                            if ChosenBattlePokemonStats['HP'] <= 0:
                                print(f"{ChosenBattlePokemon} fainted!")
                                time.sleep(0.5)
                                Picking = False
                                return 1
                    else:
                        print("Invalid move choice. Try again.")
                        time.sleep(0.5)
                elif battlepick.lower() == "heal":
                    if ChosenBattlePokemonStats["HP"] <= 0:
                        print(f"{ChosenBattlePokemon} has fainted and cannot be healed!")
                        time.sleep(0.5)
                    elif ChosenBattlePokemonStats['HP'] == ChosenBattlePokemonStats['MaxHP']:
                        print(f"{ChosenBattlePokemon} is a full health and cannot be healed")
                        time.sleep(0.5)
                    else:
                        if Potions > 0:
                            heal_amount = min(20, ChosenBattlePokemonStats['MaxHP'] - ChosenBattlePokemonStats['HP'])
                            ChosenBattlePokemonStats['HP'] += heal_amount
                            Potions -= 1
                            print(f"Used a potion! {ChosenBattlePokemon} healed for {heal_amount} HP and now has {ChosenBattlePokemonStats['HP']} HP. Potions left: {Potions}")
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
