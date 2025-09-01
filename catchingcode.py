import random
import TemplateSaveData
def catchPokemon(SecondPokemonStats, SecondPokemon, PokemonOnTeam, BattlePokemon, SecondPokemonMoves, Balls):
    SecondPokemonStats
    print("Catching Pokemon is not coded yet!")
    print("Adding random Pokemon to your team...")
    print("You will not be able to use the pokemon to battle, but the ability will be added.")
    PokemonCaught = random.choice(BattlePokemon)
    
    if SecondPokemon != "None":
        print("You have caught maximum pokemon!")
        return 0, SecondPokemonStats, SecondPokemon, PokemonOnTeam, BattlePokemon, SecondPokemonMoves, Balls
    else:
        if Balls >= 0:
            SecondPokemon = PokemonCaught
            if PokemonCaught == "Pidgey":
                SecondPokemonStats = TemplateSaveData.PidgeyStats
                SecondPokemonMoves.append(TemplateSaveData.Moves["Gust"])
            elif PokemonCaught == "Rattata":
                SecondPokemonStats = TemplateSaveData.RattataStats
                SecondPokemonMoves.append(TemplateSaveData.Moves["Pound"])
            elif PokemonCaught == "Caterpie":
                SecondPokemonStats = TemplateSaveData.CaterpieStats
                SecondPokemonMoves.append(TemplateSaveData.Moves["FuryCutter"])
            elif PokemonCaught == "Weedle":
                SecondPokemonStats = TemplateSaveData.WeedleStats
                SecondPokemonMoves.append(TemplateSaveData.Moves["FuryCutter"])
            else:
                SecondPokemonStats = TemplateSaveData.SpearowStats
                SecondPokemonMoves.append(TemplateSaveData.Moves["Gust"])
            PokemonOnTeam.append(SecondPokemon)
            Balls -= 1
            return 1, SecondPokemonStats, SecondPokemon, PokemonOnTeam, BattlePokemon, SecondPokemonMoves, Balls
        else:
            print("You dont have any pokeballs left!")
            return 2, SecondPokemonStats, SecondPokemon, PokemonOnTeam, BattlePokemon, SecondPokemonMoves, Balls
