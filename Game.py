import TemplateSaveData
import json
import sys
import pickle
from TemplateSaveData import PokemonChoices
from Battlecode import battlecode
import Battlecode
savefile = input("What was your save file name? ")

try:
    with open(savefile, 'rb') as f:
        print(f"File {savefile} Found")
        ChosenPokemon = pickle.load(f)
        Pointinggame = pickle.load(f)
        RivalName = pickle.load(f)
        Rivalpokemon = pickle.load(f)
        Pokemontype = pickle.load(f)
        print("Returning to most recent save point...")
        
except EOFError:
    print(f"Error: The pickle file is empty or corrupted. Initializing {savefile} to a default value.")
    ChosenPokemon = TemplateSaveData.Stats[0]
    Pointinggame = TemplateSaveData.Stats[1]
    RivalName = TemplateSaveData.Stats[2]
    Rivalpokemon = TemplateSaveData.Stats[3]
    Pokemontype = TemplateSaveData.Stats[4]
except FileNotFoundError:
    
    print("No File Found")
    # Define your template data
    Stats = TemplateSaveData.Stats
    ChosenPokemon = TemplateSaveData.Stats[0]
    Pointinggame = TemplateSaveData.Stats[1]
    RivalName = TemplateSaveData.Stats[2]
    Rivalpokemon = TemplateSaveData.Stats[3]
    Pokemontype = TemplateSaveData.Stats[4]
    with open(savefile, 'wb') as f:
        pickle.dump(ChosenPokemon, f)
        pickle.dump(Pointinggame, f)
        pickle.dump(RivalName, f)
        pickle.dump(Rivalpokemon, f)
        Pokemontype = TemplateSaveData.Stats[4]
   # Assign the template data to 'data' for immediate use
    print(f"New file created with name {savefile}") # Handle case where file doesn't exist yet
def save():
    with open(savefile, 'wb') as f:
        pickle.dump(ChosenPokemon, f)
        pickle.dump(Pointinggame, f)
        pickle.dump(RivalName, f)
        pickle.dump(Rivalpokemon, f)   
        Pokemontype = TemplateSaveData.Stats[4]
Playing = True
while Playing:       
    if Pointinggame == 1:
        picking = True          
        while picking:  
            PickedPokemon = input("Choose a pokemon: Charmander, Squirtle or Bulbasaur ")
            valid_choices = [p.lower() for p in PokemonChoices]
            if PickedPokemon.lower() in valid_choices:
                ChosenPokemon = PokemonChoices[valid_choices.index(PickedPokemon.lower())]
                print(f"You chose {ChosenPokemon}!")
                if ChosenPokemon == "Charmander":
                    Pokemontype = "Fire"
                elif ChosenPokemon == "Bulbasaur":
                    Pokemontype = "Grass"
                else:
                    Pokemontype = "Water"
                print(f"{ChosenPokemon} is a {Pokemontype} type pokemon.")
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
        elif ChosenPokemon == "Bulbasaur":
            Rivalpokemon = "Squirtle"
        else:
            Rivalpokemon = "Charmander"
            print(f"{RivalName}: Hey! {ChosenPokemon} is a cool pokemon, But since you picked that ill pick {Rivalpokemon}")
        Pointinggame = 4
        save()
    elif Pointinggame == 4:
        print(f"{RivalName}: Let's see how strong your {ChosenPokemon} is against my {Rivalpokemon}!")
        battlecode()
        result = battlecode()
        if result == 0:
            print(f"You won the battle against {RivalName}!")
            print(f"{RivalName}: Wow! You're really strong! I guess I'll let you go this time...")
            Pointinggame = 5
        else:
            print(f"You lost the battle against {RivalName}. Better luck next time!")
            print(f"{RivalName}: Haha! I win! Lets battle again!")
    elif Pointinggame == 5:
        Playing = False
print("End of Demo, thank you for playing!")
save()

