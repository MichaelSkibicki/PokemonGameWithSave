import TemplateSaveData
import json
import sys
import pickle
from TemplateSaveData import PokemonChoices
from Battlecode import battlecode
import Battlecode
from LevelUpCode import level_up
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
        print(f"Welcome Back! You last saved with {ChosenPokemon} at level {Level}.")
        print(f"{ChosenPokemon}'s stats are:")
        for stat, value in Pokemonstats.items():
            if stat != "MaxHP":
                print(f"  {stat}: {value}")
        print("Available Attacks:")
        for move in AvaliableAttacks:
            print(f"  {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")
        print("Returning to most recent save point...")
        
except EOFError:
    print(f"Error: The pickle file is outd,ated or corrupted. Initializing {savefile} to a default value.")
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
Playing = True
while Playing:       
    if Pointinggame == 1:
        Name = input("What is your name? ")
        print(f"Hello {Name}, Welcome to the world of Pokemon!")
        picking = True          
        while picking:  
            PickedPokemon = input("Choose a pokemon: Charmander, Squirtle or Bulbasaur ")
            valid_choices = [p.lower() for p in PokemonChoices]
            if PickedPokemon.lower() in valid_choices:
                ChosenPokemon = PokemonChoices[valid_choices.index(PickedPokemon.lower())]
                print(f"You chose {ChosenPokemon}!")
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
                for stat, value in Pokemonstats.items():
                    print(f"  {stat}: {value}")
                AvaliableAttacks.append(Moves["Tackle"])
                print("Available Attacks:")
                for move in AvaliableAttacks:
                    print(f"  {move['Name']} - Type: {move['Type']}, Power: {move['Power']}")

                Pointinggame = 2
                save()
                picking = False
                
            else:
                print("Ivalid Choice, please pick 'Charmander', 'Squirtle', or 'Bulbasaur'")
                continue
    elif Pointinggame == 2:

        RivalName = input("What is your rival's name? ")
        print(f"Your rival's name is {RivalName}")
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
        Pointinggame = 4
        save()
    elif Pointinggame == 4:
        print(f"{RivalName}: Let's see how strong your {ChosenPokemon} is against my {Rivalpokemon}!")
        result = battlecode()
        if result == 0:
            print(f"You won the battle against {RivalName}!")
            print(f"{RivalName}: Wow! You're really strong! I guess I'll let you go this time...")
            print(f"You gained {(5*(Level**3))//10} Xp!")
            Xp += (5*(Level**3))//10
            Level, Xp, XpToNextLevel, Pokemonstats = level_up(ChosenPokemon, Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks)
            save()
            Pointinggame = 5
        else:
            print(f"You lost the battle against {RivalName}. Better luck next time!")
            print(f"{RivalName}: Haha! I win! Lets battle again! Here, I'll heal your {ChosenPokemon}.")
    elif Pointinggame == 5:
        Playing = False
print("End of Demo, thank you for playing!")
save()

