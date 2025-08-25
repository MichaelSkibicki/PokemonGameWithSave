import TemplateSaveData

def level_up(ChosenPokemon, Level, Xp, XpToNextLevel, Pokemonstats, Moves, AvaliableAttacks):
    while Xp >= XpToNextLevel:
        Level += 1
        Xp -= XpToNextLevel
        XpToNextLevel = int(XpToNextLevel * 1.5)  # Increase XP needed for next level
        # Increase stats on level up
        Pokemonstats["MaxHP"] += 5
        Pokemonstats["Attack"] += 3
        Pokemonstats["Defense"] += 3
        Pokemonstats["Speed"] += 2
        Pokemonstats["HP"] = Pokemonstats["MaxHP"]  # Heal to full on level up
        print(f"{Pokemonstats['Name']} leveled up to Level {Level}!")
        print(f"New stats - HP: {Pokemonstats['HP']}, Attack: {Pokemonstats['Attack']}, Defense: {Pokemonstats['Defense']}, Speed: {Pokemonstats['Speed']}")
        if Level == 6:
            if ChosenPokemon == "Charmander":
                AvaliableAttacks.append(Moves["Ember"])
                print(f"{ChosenPokemon} learned Ember!")
            elif ChosenPokemon == "Squirtle":
                AvaliableAttacks.append(Moves["WaterGun"])
                print(f"{ChosenPokemon} learned Water Gun!")
            elif ChosenPokemon == "Bulbasaur":
                AvaliableAttacks.append(Moves["VineWhip"])
                print(f"{ChosenPokemon} learned Vine Whip!")
            print("Avaliable Attacks:", ", ".join(move["Name"] for move in AvaliableAttacks))
    # Always return updated values
    return Level, Xp, XpToNextLevel, Pokemonstats