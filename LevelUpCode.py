import TemplateSaveData
import time
def level_up(ChosenPokemon, Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks, SecondPokemonXp, SecondPokemonLevel, SecondPokemonXpNeeded, SecondPokemon, SecondPokemonStats, SecondPokemonMoves):
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
    while SecondPokemonXp >= SecondPokemonXpNeeded:
        SecondPokemonLevel += 1
        SecondPokemonXp -= SecondPokemonXpNeeded
        SecondPokemonXpNeeded = int((5*(Level**3))//4)
  # Increase XP needed for next level
        # Increase stats on level up
        SecondPokemonStats["MaxHP"] += 5
        SecondPokemonStats["Attack"] += 3
        SecondPokemonStats["Defense"] += 3
        SecondPokemonStats["Speed"] += 2
        SecondPokemonStats["HP"] = SecondPokemonStats["MaxHP"]  # Heal to full on level up
        time.sleep(0.5)
        print(f"{SecondPokemonStats['Name']} leveled up to Level {SecondPokemonLevel}!")
        time.sleep(0.5)
        print(f"New stats - HP: {SecondPokemonStats['HP']}, Attack: {SecondPokemonStats['Attack']}, Defense: {SecondPokemonStats['Defense']}, Speed: {SecondPokemonStats['Speed']}")
        time.sleep(0.5)
        if Level == 6:
            if SecondPokemon == "Spearow":
                SecondPokemonMoves.append(Moves["AirCutter"])
                print(f"{SecondPokemon} learned Air Cutter!")
            elif SecondPokemon == "Pidgey":
                SecondPokemonMoves.append(Moves["AirCutter"])
                print(f"{SecondPokemon} learned Air Cutter!")
            elif SecondPokemon == "Caterpie":
                SecondPokemonMoves.append(Moves["BugBite"])
                print(f"{SecondPokemon} learned Bug Bite!")
            elif SecondPokemon == "Weedle":
                SecondPokemonMoves.append(Moves["BugBite"])
                print(f"{SecondPokemon} learned Bug Bite!")
            elif SecondPokemon == "Rattata":
                SecondPokemonMoves.append(Moves["Swift"])
                print(f"{SecondPokemon} learned Swift!")
            time.sleep(0.5)
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in SecondPokemonMoves))
            time.sleep(0.5)
        elif Level == 10:
            if SecondPokemon == "Spearow":
                SecondPokemonMoves.append(Moves["Aeroblast"])
                print(f"{SecondPokemon} learned Aeroblast!")
            elif SecondPokemon == "Pidgey":
                SecondPokemonMoves.append(Moves["Aeroblast"])
                print(f"{SecondPokemon} learned Aeroblast!")
            elif SecondPokemon == "Caterpie":
                SecondPokemonMoves.append(Moves["BugBuzz"])
                print(f"{SecondPokemon} learned Bug Buzz!")
            elif SecondPokemon == "Weedle":
                SecondPokemonMoves.append(Moves["BugBuzz"])
                print(f"{SecondPokemon} learned Bug Buzz!")
            elif SecondPokemon == "Rattata":
                SecondPokemonMoves.append(Moves["MegaKick"])
                print(f"{SecondPokemon} learned Mega Kick!")
            time.sleep(0.5)
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in SecondPokemonMoves))
            time.sleep(0.5)
        elif Level == 18:
            if SecondPokemon == "Spearow":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Fearow"
                SecondPokemonStats.update({"Name": "Fearow", "Type": "Flying"})

                print(f"Congratulations! Your Spearow evolved into Fearow!")
                time.sleep(0.5)
            elif SecondPokemon == "Pidgey":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Pidgeotto"
                SecondPokemonStats.update({"Name": "Pidgeotto", "Type": "Flying"})

                print(f"Congratulations! Your Pidgey evolved into Pidgeotto!")
                time.sleep(0.5)
            elif SecondPokemon == "Weedle":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Kakuna"
                SecondPokemonStats.update({"Name": "Kakuna", "Type": "Bug"})
                print(f"Congratulations! Your Weedle evolved into Kakuna!")
                time.sleep(0.5)
            elif SecondPokemon == "Caterpie":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Metapod"
                SecondPokemonStats.update({"Name": "Metapod", "Type": "Bug"})
                print(f"Congratulations! Your Caterpie evolved into Metapod!")
                time.sleep(0.5)
            elif SecondPokemon == "Rattata":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Raticate"
                SecondPokemonStats.update({"Name": "Raticate", "Type": "Normal"})
                print(f"Congratulations! Your Caterpie evolved into Metapod!")
        elif Level == 30:
            if SecondPokemon == "Fearow":
                SecondPokemonMoves.append(Moves["SkyAttack"])
                print(f"{SecondPokemon} learned Sky Attack!")
            elif SecondPokemon == "Pidgeotto":
                SecondPokemonMoves.append(Moves["SkyAttack"])
                print(f"{SecondPokemon} learned Sky Attack!")
            elif SecondPokemon == "Metapod":
                SecondPokemonMoves.append(Moves["MegaHorn"])
                print(f"{SecondPokemon} learned Mega Horn!")
            elif SecondPokemon == "Kakuna":
                SecondPokemonMoves.append(Moves["MegaHorn"])
                print(f"{SecondPokemon} learned Mega Horn!")
            elif SecondPokemon == "Raticate":
                SecondPokemonMoves.append(Moves["HyperBeam"])
                print(f"{SecondPokemon} learned HyperBeam!")
            time.sleep(0.5)
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in SecondPokemonMoves))
            time.sleep(0.5)
        elif Level == 36:

            if SecondPokemon == "Pidgeotto":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Pidgeot"
                SecondPokemonStats.update({"Name": "Pidgeot", "Type": "Flying"})

                print(f"Congratulations! Your Pidgeotto evolved into Pidgeot!")
                time.sleep(0.5)
            elif SecondPokemon == "Kakuna":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Beedrill"
                SecondPokemonStats.update({"Name": "Bedrill", "Type": "Bug"})
                print(f"Congratulations! Your Kakuna evolved into Beedrill!")
                time.sleep(0.5)
            elif SecondPokemon == "Metapod":
                print(f"{SecondPokemon} is trying to evolve!")
                time.sleep(0.5)
                SecondPokemon = "Butterfree"
                SecondPokemonStats.update({"Name": "Butterfree", "Type": "Bug"})
                print(f"Congratulations! Your Metapod evolved into Butterfree!")
                time.sleep(0.5)

    # Always return updated values

    return ChosenPokemon, Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks, SecondPokemonXp, SecondPokemonLevel, SecondPokemonXpNeeded, SecondPokemon, SecondPokemonStats, SecondPokemonMoves