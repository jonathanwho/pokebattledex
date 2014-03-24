import json
from pprint import pprint

json_data = open('json/damagetaken.json')
pokemon_damage = open("../gae/pokedex/pokemon_damage.py", 'w')
pokemon_damage.write("""pokemon_types = ["normal", "fire", "water", "electric", 
  "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", 
  "rock", "ghost", "dragon", "dark", "steel", "fairy"] \n
  pokemon_damage_dict = dict()\n""")

pokemon_types = ["normal", "fire", "water", "electric", "grass", "ice", 
  "fighting", "poison", "ground", "flying", "psychic", "bug", "rock",
  "ghost", "dragon", "dark", "steel", "fairy"]

damageTaken = json.load(json_data)
for x, typer in enumerate(pokemon_types):
  pokemon_damage.write("pokemon_damage_dict[\"%s\"] = dict()\n" % typer)
  damages = damageTaken[x][typer]
  for subtype in pokemon_types:
    pokemon_damage.write("pokemon_damage_dict[\"%s\"][\"%s\"] = %.1f\n" % (
      typer, subtype, damages[subtype]))
  pokemon_damage.write("\n")