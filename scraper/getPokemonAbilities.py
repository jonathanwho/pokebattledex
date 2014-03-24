import json
from pprint import pprint

json_data = open('json/abilities.json')
pokemon_abilities = open("../gae/pokedex/pokemon_abilities.py", 'w')
pokemon_abilities.write("""# -*- coding: utf-8 -*-\npokemon_abilities_list = [] 
  \npokemon_abilities_dict = dict()\n""")


abilities = json.load(json_data)
for ability in abilities:
  pokemon_abilities.write("""pokemon_abilities_list.append(\"%s\")\n
    pokemon_abilities_dict[\"%s\"] = \"%s\"\n""" % (
    ability["name"].encode("utf-8"), ability["name"].encode("utf-8"), 
    ability["description"].encode("utf-8")))