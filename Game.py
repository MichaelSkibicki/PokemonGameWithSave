import TemplateSaveData
import json
import sys
import pickle
from TemplateSaveData import PokemonChoices
savefile = input("What was your save file name? ")

try:
    with open(savefile, 'rb') as f:
        print(f"File {savefile} Found")
        ChosenPokemon = pickle.load(f)
        
except EOFError:
    print("Error: The pickle file is empty or corrupted. Initializing Gamemaxhealth to a default value.")
    ChosenPokemon = TemplateSaveData.Stats[0]

except FileNotFoundError:
    
    print("No File Found")
    # Define your template data
    Stats = TemplateSaveData.Stats
    ChosenPokemon = TemplateSaveData.Stats[0]
    

    with open(savefile, 'wb') as f:
        pickle.dump(ChosenPokemon, f)
        
   # Assign the template data to 'data' for immediate use
    print(f"New file created with name {savefile}") # Handle case where file doesn't exist yet
def save():
    with open(savefile, 'wb') as f:
        pickle.dump(ChosenPokemon, f)
        
if ChosenPokemon == "None":
    print("You havent chosen a pokemon, starting pokemon selection")
else:
    picking = True
    while picking:
        Newpokemon = input(f"You have chosen {ChosenPokemon}, would you like to switch? Y/N ")
        if Newpokemon.upper() == "N":
            print("Okay, continuing with current pokemon")
            print("End of Demo, thank you for playing!")
            save()
            picking = False
            sys.exit()
        elif Newpokemon.upper() == "Y":
            picking = False
            break
        else:
            print("Invalid Choice, pick 'Y' or 'N'")
            continue
picking = True          
while picking:  
    PickedPokemon = input("Choose a pokemon: Charmander, Squirtle or Bulbasaur ")
    valid_choices = [p.lower() for p in PokemonChoices]
    if PickedPokemon.lower() in valid_choices:
        ChosenPokemon = PokemonChoices[valid_choices.index(PickedPokemon.lower())]
        print(f"You chose {ChosenPokemon}!")
        picking = False
    else:
        print("Ivalid Choice, please pick 'Charmander', 'Squirtle', or 'Bulbasaur'")
        continue
print("End of Demo, thank you for playing!")
save()

