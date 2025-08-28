import TemplateSaveData
import json
import sys
import time
import pickle
from TemplateSaveData import PokemonChoices
from Battlecode import battlecode
import Battlecode
from LevelUpCode import level_up
Battletype = "None"
savefile = input("What was your save file name? ")

try:
    with open(savefile, 'rb') as f:
        print(f"File {savefile} Found")
        ChosenPokemon = pickle.load(f)
        Pointinggame = pickle.load(f)
        RivalName = pickle.load(f)
        Rivalpokemon = pickle.load(f)
        Pokemontype = pickle.load(f)
        Pokemonstats = pickle.load(f)
        Rivalstats = pickle.load(f)
        Moves = pickle.load(f)
        AvaliableAttacks = pickle.load(f)
        Level = pickle.load(f)
        Xp = pickle.load(f)
        XpToNextLevel = pickle.load(f)
        Potions = pickle.load(f)
        Balls = pickle.load(f)
        Coins = pickle.load(f)
        Name = pickle.load(f)
        Location = pickle.load(f)
        AccessableLocations = pickle.load(f)
        half_length = pickle.load(f)
        print(f"Welcome Back! You last saved with {ChosenPokemon} at level {Level}.")

        print(f"{ChosenPokemon}'s stats are:")
        time.sleep(0.5)
        for stat, value in Pokemonstats.items():
            if stat not in ["Weakness", "Resistance"]:
                if stat != "MaxHP":
                    print(f"  {stat}: {value}")
                    time.sleep(0.5)

        if isinstance(Pokemonstats["Weakness"], list):
            print("  Weakness:", ", ".join(Pokemonstats["Weakness"]))
        else:
            print("  Weakness:", Pokemonstats["Weakness"])
        time.sleep(0.5)
        if isinstance(Pokemonstats["Resistance"], list):
            print("  Resistance:", ", ".join(Pokemonstats["Resistance"]))
        
        else:
            print("  Resistance:", Pokemonstats["Resistance"])
        time.sleep(0.5)
        print("Available Attacks:")
        time.sleep(0.5)
        for move in AvaliableAttacks:
            print(f"  {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
            time.sleep(0.5)
        print(f"You have {Potions} Potions, {Balls} Pokeballs and {Coins} Coins.")
        time.sleep(0.5)
        print("Returning to most recent save point...")
        time.sleep(0.5)
        
except EOFError:
    print(f"Error: The pickle file is outdated or corrupted. Initializing {savefile} to a default value.")
    ChosenPokemon = TemplateSaveData.Stats[0]
    Pointinggame = TemplateSaveData.Stats[1]
    RivalName = TemplateSaveData.Stats[2]
    Rivalpokemon = TemplateSaveData.Stats[3]
    Pokemontype = TemplateSaveData.Stats[4]
    Pokemonstats = TemplateSaveData.PokemonStats
    Rivalstats = TemplateSaveData.RivalStats
    Moves = TemplateSaveData.Moves
    AvaliableAttacks = TemplateSaveData.AvaliableAttacks
    Level = TemplateSaveData.Stats[5]
    Xp = TemplateSaveData.Stats[6]
    XpToNextLevel = TemplateSaveData.Stats[7]
    Potions = TemplateSaveData.Stats[8]
    Balls = TemplateSaveData.Stats[9]
    Coins = TemplateSaveData.Stats[10]
    Name = TemplateSaveData.Stats[11]
    Location = TemplateSaveData.Stats[12]
    AccessableLocations = TemplateSaveData.Stats[13]
    half_length = len(AccessableLocations) // 2
except FileNotFoundError:
    
    print("No File Found")
    # Define your template data
    Stats = TemplateSaveData.Stats
    ChosenPokemon = TemplateSaveData.Stats[0]
    Pointinggame = TemplateSaveData.Stats[1]
    RivalName = TemplateSaveData.Stats[2]
    Rivalpokemon = TemplateSaveData.Stats[3]
    Pokemontype = TemplateSaveData.Stats[4]
    Pokemonstats = TemplateSaveData.PokemonStats
    Rivalstats = TemplateSaveData.RivalStats
    Moves = TemplateSaveData.Moves
    AvaliableAttacks = TemplateSaveData.AvaliableAttacks
    Level = TemplateSaveData.Stats[5]
    Xp = TemplateSaveData.Stats[6]
    XpToNextLevel = TemplateSaveData.Stats[7]
    Potions = TemplateSaveData.Stats[8]
    Balls = TemplateSaveData.Stats[9]
    Coins = TemplateSaveData.Stats[10]
    Name = TemplateSaveData.Stats[11]
    Location = TemplateSaveData.Stats[12]
    AccessableLocations = TemplateSaveData.Stats[13]
    half_length = len(AccessableLocations) // 2
    with open(savefile, 'wb') as f:
        pickle.dump(ChosenPokemon, f)
        pickle.dump(Pointinggame, f)
        pickle.dump(RivalName, f)
        pickle.dump(Rivalpokemon, f)
        pickle.dump(Pokemontype, f)
        pickle.dump(Pokemonstats, f)
        pickle.dump(Rivalstats, f)
        pickle.dump(Moves, f)  
        pickle.dump(AvaliableAttacks, f)
        pickle.dump(Level, f)
        pickle.dump(Xp, f)
        pickle.dump(XpToNextLevel, f)
        pickle.dump(Potions, f)
        pickle.dump(Balls, f)
        pickle.dump(Coins, f)
        pickle.dump(Name, f)
        pickle.dump(Location, f)
        pickle.dump(AccessableLocations, f)
        pickle.dump(half_length, f)
   # Assign the template data to 'data' for immediate use
    print(f"New file created with name {savefile}") # Handle case where file doesn't exist yet
def save():
    with open(savefile, 'wb') as f:
        pickle.dump(ChosenPokemon, f)
        pickle.dump(Pointinggame, f)
        pickle.dump(RivalName, f)
        pickle.dump(Rivalpokemon, f)
        pickle.dump(Pokemontype, f)
        pickle.dump(Pokemonstats, f)
        pickle.dump(Rivalstats, f)
        pickle.dump(Moves, f)
        pickle.dump(AvaliableAttacks, f)
        pickle.dump(Level, f)
        pickle.dump(Xp, f)
        pickle.dump(XpToNextLevel, f)
        pickle.dump(Potions, f)
        pickle.dump(Balls, f)
        pickle.dump(Coins, f)
        pickle.dump(Name, f)
        pickle.dump(Location, f)
        pickle.dump(AccessableLocations, f)
        pickle.dump(half_length, f)
Playing = True
while Playing:       
    if Pointinggame == 1:
        Name = input("What is your name? ")

        print(f"Hello {Name}, Welcome to the world of Pokemon!")
        time.sleep(0.5)
        picking = True          
        while picking:  
            PickedPokemon = input("Choose a pokemon: Charmander, Squirtle or Bulbasaur ")
            valid_choices = [p.lower() for p in PokemonChoices]
            if PickedPokemon.lower() in valid_choices:
                ChosenPokemon = PokemonChoices[valid_choices.index(PickedPokemon.lower())]
                print(f"You chose {ChosenPokemon}!")
                time.sleep(0.5)
                if ChosenPokemon == "Charmander":
                    Pokemontype = "Fire"
                    Pokemonstats = TemplateSaveData.CharmanderStats
                elif ChosenPokemon == "Bulbasaur":
                    Pokemontype = "Grass"
                    Pokemonstats = TemplateSaveData.BulbasaurStats
                else:
                    Pokemontype = "Water"
                    Pokemonstats = TemplateSaveData.SquirtleStats
                save()
                print(f"{ChosenPokemon}'s stats are:")
                time.sleep(0.5)
                for stat, value in Pokemonstats.items():
                    if stat not in ["Weakness", "Resistance"]:
                        if stat != "MaxHP":
                            print(f"  {stat}: {value}")
                            time.sleep(0.5)

                if isinstance(Pokemonstats["Weakness"], list):
                    print("  Weakness:", ", ".join(Pokemonstats["Weakness"]))
                else:
                    print("  Weakness:", Pokemonstats["Weakness"])
                time.sleep(0.5)
                if isinstance(Pokemonstats["Resistance"], list):
                    print("  Resistance:", ", ".join(Pokemonstats["Resistance"]))
                else:
                    print("  Resistance:", Pokemonstats["Resistance"])
                time.sleep(0.5)

                AvaliableAttacks.append(Moves["Tackle"])
                print("Available Attacks:")
                time.sleep(0.5)
                for move in AvaliableAttacks:
                    print(f"  {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
                time.sleep(0.5)
                Pointinggame = 2
                save()
                picking = False
                
            else:
                print("Ivalid Choice, please pick 'Charmander', 'Squirtle', or 'Bulbasaur'")
                time.sleep(0.5)
                continue
    elif Pointinggame == 2:

        RivalName = input("What is your rival's name? ")
        print(f"Your rival's name is {RivalName}")
        time.sleep(0.5)
        Pointinggame = 3
        save()
    elif Pointinggame == 3:
        if ChosenPokemon == "Charmander":
            Rivalpokemon = "Bulbasaur"
            Rivalstats = TemplateSaveData.BulbasaurStats
        elif ChosenPokemon == "Bulbasaur":
            Rivalpokemon = "Squirtle"
            Rivalstats = TemplateSaveData.SquirtleStats
        else:
            Rivalpokemon = "Charmander"
            Rivalstats = TemplateSaveData.CharmanderStats
            print(f"{RivalName}: Hey! {ChosenPokemon} is a cool pokemon, But since you picked that ill pick {Rivalpokemon}")
            time.sleep(0.5)

        Pointinggame = 4
        save()
    elif Pointinggame == 4:
        print(f"{RivalName}: Let's see how strong your {ChosenPokemon} is against my {Rivalpokemon}!")
        time.sleep(0.5)

        Battletype = "Rival"
        result = battlecode(Battletype, Potions, Balls, Coins, ChosenPokemon, Name, Level, Xp, XpToNextLevel, RivalName, Rivalpokemon, Pokemontype, Pokemonstats, Rivalstats, Moves, AvaliableAttacks)
        if result == 0:
            print(f"You won the battle against {RivalName}!")
            time.sleep(0.5)

            print(f"{RivalName}: Wow! You're really strong! I guess I'll let you go this time...")
            time.sleep(0.5)

            print(f"You gained {(5*(Level**3))//10} Xp! You Also Recieved {(4*(Level**3))//10} Coins!")
            time.sleep(0.5)

            Coins += (4*(Level**3))//10
            Xp += (5*(Level**3))//10
            Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks = level_up(ChosenPokemon, Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks)
            save()
            Pointinggame = 5
        else:
            print(f"You lost the battle against {RivalName}. Better luck next time!")
            time.sleep(0.5)

            print(f"{RivalName}: Haha! I win! Lets battle again! Here, I'll heal your {ChosenPokemon}.")
            Pokemonstats['HP'] = Pokemonstats['MaxHP']
            time.sleep(0.5)
    elif Pointinggame == 5:
        print(f"{RivalName}: I have to go now, but I'll see you around {Name}!")
        time.sleep(0.5)
        print(f"{RivalName}: Oh! and Before I forget, Heres a gift!")
        time.sleep(0.5)

        Potions += 3
        Balls += 3
        print("You received 3 Potions and 3 Pokeballs!")
        time.sleep(0.5)

        print(f"You now have {Potions} Potions and {Balls} Pokeballs!")
        time.sleep(0.5)

        Pointinggame = 6
        save()
    if Pointinggame == 6:
        print("Well Done!")
        time.sleep(0.5)
        print("Now, you can explore the world of Pokemon!")
        time.sleep(0.5)
        print("You can battle wild Pokemon, catch them, and train your Pokemon to become stronger!")
        time.sleep(0.5)
        print("You can also visit Pokemarts to buy items, and heal your Pokemon at Pokecenters!")
        time.sleep(0.5)
        print("You can also challenge other trainers to battles while on your journey!")
        time.sleep(0.5)
        print("Good luck on your journey to become a Pokemon Master!")
        time.sleep(0.5)
        Pointinggame = 7
        save()
    if Pointinggame == 7:
        Location = "Pallet Town"
        print(f"You are currently in {Location}")
        AccessableLocations = ["Route 1", "Route 21", "route 1", "route 21"]
        valid_walkchoices = [p.lower() for p in AccessableLocations]
        print("Accessable Locations:")
        half_length = len(AccessableLocations) // 2
        for i in range(half_length):
            print(f"  {AccessableLocations[i]}")
        Picking = True
        while Picking:
            WalkTo = input("Where do you want to go? ")
            if WalkTo in AccessableLocations:
                if AccessableLocations[valid_walkchoices.index(WalkTo.lower())] == "Route 21":
                    if Level >= 20:
                        Location = "Route 21"
                    else:
                        print("You Are Not High Enough Level To Access This Location")
                        continue
                Location = AccessableLocations[valid_walkchoices.index(WalkTo.lower())]
                print(f"While walking to {Location}, you encounter a Pokemon!")
                print(Location)
                Picking = False
            else:
                print("Invalid choice, try again")
        Playing = False
print("End of Demo, thank you for playing!")
Pokemonstats['HP'] = Pokemonstats['MaxHP']
save()
time.sleep(0.5)
