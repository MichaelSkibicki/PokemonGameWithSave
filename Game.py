import TemplateSaveData
import json
import pickle
print(TemplateSaveData.Health)
savefile = input("What was your save file name? ")

try:
    with open(savefile, 'rb') as f:
        print(f"File {savefile} Found")
        Gamehealth = pickle.load(f)
        Gamemaxhealth = pickle.load(f)
        Gamelevel = pickle.load(f)
        Gamexp = pickle.load(f)
        Gamexpneeded = pickle.load(f)
        Gamegold = pickle.load(f)
except EOFError:
    print("Error: The pickle file is empty or corrupted. Initializing Gamemaxhealth to a default value.")
    Gamehealth = TemplateSaveData.Stats[0]
    Gamemaxhealth = TemplateSaveData.Stats[1]
    Gamelevel = TemplateSaveData.Stats[2]
    Gamexp = TemplateSaveData.Stats[3]
    Gamexpneeded = TemplateSaveData.Stats[4]
    Gamegold = TemplateSaveData.Stats[5]
except FileNotFoundError:
    
    print("No File Found")
    # Define your template data
    Stats = TemplateSaveData.Stats
    Gamehealth = TemplateSaveData.Stats[0]
    Gamemaxhealth = TemplateSaveData.Stats[1]
    Gamelevel = TemplateSaveData.Stats[2]
    Gamexp = TemplateSaveData.Stats[3]
    Gamexpneeded = TemplateSaveData.Stats[4]
    Gamegold = TemplateSaveData.Stats[5]
    with open(savefile, 'wb') as f:
        pickle.dump(Gamehealth, f)
        pickle.dump(Gamemaxhealth, f)
        pickle.dump(Gamelevel, f)
        pickle.dump(Gamexp, f)
        pickle.dump(Gamexpneeded, f)
        pickle.dump(Gamegold, f)  # Assign the template data to 'data' for immediate use
    print(f"New file created with name {savefile}") # Handle case where file doesn't exist yet



with open(savefile, 'wb') as f:
    pickle.dump(Gamehealth, f)
    pickle.dump(Gamemaxhealth, f)
    pickle.dump(Gamelevel, f)
    pickle.dump(Gamexp, f)
    pickle.dump(Gamexpneeded, f)
    pickle.dump(Gamegold, f)
print(f"You Have {Gamehealth} Health, You are Level {Gamelevel}, You have {Gamexp} Xp, You need {Gamexpneeded} Xp to level up, You have {Gamegold} Gold")