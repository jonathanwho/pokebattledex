import json
from pprint import pprint

json_data = open('json/pokemon.json')
pokemon_dict = open("../gae/pokedex/pokemon_data.py", 'w')
pokemon_dict.write('pokemon_list = []\npokemon_dict = dict()\n')

pokemons = json.load(json_data)
for pokemon in pokemons:
  print pokemon['name']
  pokemon_dict.write('pokemon_list.append("%s")\npokemon_dict["%s"] = dict()\npokemon_dict["%s"]["name"] = "%s"\npokemon_dict["%s"]["types"] = "%s"\npokemon_dict["%s"]["abilities"] = "%s"\npokemon_dict["%s"]["stats"] = %s\n\n' % (
    pokemon['name'], # name
    pokemon['name'], # name
    pokemon['name'], # name
    pokemon['name'], # name
    pokemon['name'], # name
    ", ".join(set([str(x) for x in pokemon['types']])), # types
    pokemon['name'], # name 
    ", ".join(set([str(x) for x in pokemon['abilities']])), # abilities
    pokemon['name'], # name
    pokemon['baseStats']
    )
  ) 