import TemplateSaveData
import time
def level_up(ChosenPokemon, Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks):
    while Xp >= XpToNextLevel:
        Level += 1
        Xp -= XpToNextLevel
        XpToNextLevel = int((5*(Level**3))//4)
  # Increase XP needed for next level
        # Increase stats on level up
        Pokemonstats["MaxHP"] += 5
        Pokemonstats["Attack"] += 3
        Pokemonstats["Defense"] += 3
        Pokemonstats["Speed"] += 2
        Pokemonstats["HP"] = Pokemonstats["MaxHP"]  # Heal to full on level up
        time.sleep(0.5)
        print(f"{Pokemonstats['Name']} leveled up to Level {Level}!")
        time.sleep(0.5)
        print(f"New stats - HP: {Pokemonstats['HP']}, Attack: {Pokemonstats['Attack']}, Defense: {Pokemonstats['Defense']}, Speed: {Pokemonstats['Speed']}")
        time.sleep(0.5)
        if Level == 6:
            if ChosenPokemon == "Charmander":
                AvaliableAttacks.append(Moves["Ember"])
                
            elif ChosenPokemon == "Squirtle":
                AvaliableAttacks.append(Moves["WaterGun"])
                
            elif ChosenPokemon == "Bulbasaur":
                AvaliableAttacks.append(Moves["VineWhip"])
                print(f"{ChosenPokemon} learned Vine Whip!")
            time.sleep(0.5)
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in AvaliableAttacks))
            time.sleep(0.5)
        elif Level == 10:
            if ChosenPokemon == "Charmander":
                AvaliableAttacks.append(Moves["Flamethrower"])
                print(f"{ChosenPokemon} learned Flamethrower!")
            
            elif ChosenPokemon == "Squirtle":
                AvaliableAttacks.append(Moves["AquaTail"])
                print(f"{ChosenPokemon} learned Aqua Tail!")
                
            elif ChosenPokemon == "Bulbasaur":
                AvaliableAttacks.append(Moves["LeafBlade"])
                print(f"{ChosenPokemon} learned Leaf Blade!")
            time.sleep(0.5)
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in AvaliableAttacks))
            time.sleep(0.5)
        elif Level == 18:
            if ChosenPokemon == "Charmander":
                print(f"{ChosenPokemon} is trying to evolve!")
                time.sleep(0.5)
                ChosenPokemon = "Charmeleon"
                Pokemonstats.update({"Name": "Charmeleon", "Type": "Fire"})

                print(f"Congratulations! Your Charmander evolved into Charmeleon!")
                time.sleep(0.5)
            elif ChosenPokemon == "Squirtle":
                print(f"{ChosenPokemon} is trying to evolve!")
                time.sleep(0.5)
                ChosenPokemon = "Wartortle"
                Pokemonstats.update({"Name": "Wartortle", "Type": "Water"})

                print(f"Congratulations! Your Squirtle evolved into Wartortle!")
                time.sleep(0.5)
            elif ChosenPokemon == "Bulbasaur":
                print(f"{ChosenPokemon} is trying to evolve!")
                time.sleep(0.5)
                ChosenPokemon = "Ivysaur"
                Pokemonstats.update({"Name": "Ivysaur", "Type": "Grass"})
                print(f"Congratulations! Your Bulbasaur evolved into Ivysaur!")
                time.sleep(0.5)
        elif Level == 30:
            if ChosenPokemon == "Charmeleon":
                AvaliableAttacks.append(Moves["FlareBlitz"])
                print(f"{ChosenPokemon} learned Flare Blitz!")
            elif ChosenPokemon == "Wartortle":
                AvaliableAttacks.append(Moves["HydroPump"])
                print(f"{ChosenPokemon} learned Hydro Pump!")
            elif ChosenPokemon == "Ivysaur":
                AvaliableAttacks.append(Moves["SolarBeam"])
                print(f"{ChosenPokemon} learned Solar Beam!")
            time.sleep(0.5)
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in AvaliableAttacks))
            time.sleep(0.5)
        elif Level == 36:
            if ChosenPokemon == "Charmeleon":
                print(f"{ChosenPokemon} is trying to evolve!")
                time.sleep(0.5)
                ChosenPokemon = "Charizard"
                Pokemonstats.update({"Name": "Charizard", "Type": "Fire"})
                print(f"Congratulations! Your Charmeleon evolved into Charizard!")
                time.sleep(0.5)
            elif ChosenPokemon == "Wartortle":
                print(f"{ChosenPokemon} is trying to evolve!")
                time.sleep(0.5)
                ChosenPokemon = "Blastoise"
                Pokemonstats.update({"Name": "Blastoise", "Type": "Water"})
                print(f"Congratulations! Your Wartortle evolved into Blastoise!")
                time.sleep(0.5)
            elif ChosenPokemon == "Ivysaur":
                print(f"{ChosenPokemon} is trying to evolve!")
                time.sleep(0.5)
                ChosenPokemon = "Venusaur"
                Pokemonstats.update({"Name": "Venusaur", "Type": "Grass"})
                print(f"Congratulations! Your Ivysaur evolved into Venusaur!")
                time.sleep(0.5)
    # Always return updated values
    return Level, Xp, XpToNextLevel, Pokemonstats, ChosenPokemon, AvaliableAttacks