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

# import os.path
# from bs4 import BeautifulSoup
# import urllib2

# filename = 'pokemonDataTemplate.txt'
# if os.path.isfile(filename) is False:
#   url = "http://www.smogon.com/bw/pokemon/" 
#   soup = BeautifulSoup(urllib2.urlopen(url).read())
#   with open(filename, 'w') as the_file:
#     the_file.write(soup.prettify().encode("utf8"))
# else:
#   with open(filename, 'r') as content_file:
#     soup = BeautifulSoup(content_file.read())

#   json_file = open("pokemon.json", 'w')
  # pokemon_dict = open("pokemon_dict.py", 'w')
  # pokemon_dict.write('pokemon_list = []\npokemon = dict()\n')

# filename = 'pokemonDataTemplate.txt'
# if os.path.isfile(filename) is False:
#   url = "http://www.smogon.com/bw/pokemon/" 
#   soup = BeautifulSoup(urllib2.urlopen(url).read())
#   with open(filename, 'w') as the_file:
#     the_file.write(soup.prettify().encode("utf8"))
# else:
#   with open(filename, 'r') as content_file:
#     soup = BeautifulSoup(content_file.read())

#   json_file = open("pokemon.json", 'w')
#   pokemon_dict = open("pokemon_dict.py", 'w')
#   pokemon_dict.write('pokemon_list = []\npokemon = dict()\n')

  # TODO: Scrape http://pokedream.com/pokedex/
  # for tr in soup.find_all('tr')[1:]:
  #   tds = tr.find_all('td') 
  #   json_file.write('{"name": "%s", "types": "%s", "abilities": "%s", "hp": %s, "atk": %s, "def": %s, "spa": %s, "spd": %s, "spe": %s, "bst": %s}\n' % (
  #     str(tds[0].text).strip(), # Name
  #     ", ".join([pokemonType.text.strip() for pokemonType in tds[1].find_all('a')]), # Type 
  #     # str(tds[2].text).strip(), # Tier
  #     ", ".join([pokemonType.text.strip() for pokemonType in tds[3].find_all('a')]), # Abilities
  #     str(tds[4].text).strip(), # HP
  #     str(tds[5].text).strip(), # Atk
  #     str(tds[6].text).strip(), # Def
  #     str(tds[7].text).strip(), # SpA
  #     str(tds[8].text).strip(), # SpD
  #     str(tds[9].text).strip(), # Spe
  #     str(tds[10].text).strip()) # BST
  #   )
    
  #   # write pokemon_dict.py
  #   pokemon_dict.write('pokemon_list.append("%s")\npokemon["%s"] = dict()\npokemon["%s"]["name"] = "%s"\npokemon["%s"]["types"] = "%s"\npokemon["%s"]["abilities"] = "%s"\npokemon["%s"]["hp"] = %s\npokemon["%s"]["atk"] = %s\npokemon["%s"]["def"] = %s\npokemon["%s"]["spa"] = %s\npokemon["%s"]["spd"] = %s\npokemon["%s"]["spe"] = %s\npokemon["%s"]["bst"] = %s\n\n' % (
  #     str(tds[0].text).strip(),
  #     str(tds[0].text).strip(),
  #     str(tds[0].text).strip(), str(tds[0].text).strip(), # Name
  #     str(tds[0].text).strip(), ", ".join([pokemonType.text.strip() for pokemonType in tds[1].find_all('a')]), # Type 
  #     # str(tds[2].text).strip(), # Tier
  #     str(tds[0].text).strip(), ", ".join([pokemonType.text.strip() for pokemonType in tds[3].find_all('a')]), # Abilities
  #     str(tds[0].text).strip(), str(tds[4].text).strip(), # HP
  #     str(tds[0].text).strip(), str(tds[5].text).strip(), # Atk
  #     str(tds[0].text).strip(), str(tds[6].text).strip(), # Def
  #     str(tds[0].text).strip(), str(tds[7].text).strip(), # SpA
  #     str(tds[0].text).strip(), str(tds[8].text).strip(), # SpD
  #     str(tds[0].text).strip(), str(tds[9].text).strip(), # Spe
  #     str(tds[0].text).strip(), str(tds[10].text).strip()) # BST
  #   )


# Below is for serebii
# # rooturl = "http://www.serebii.net"
# # url = "http://www.serebii.net/pokedex-xy/001.shtml"
# # soup = BeautifulSoup(urllib2.urlopen(url).read())
# # with open(filename, 'w') as the_file:
# #   the_file.write(soup.prettify().encode("utf8"))

# with open(filename, 'r') as content_file:
#   soup = BeautifulSoup(content_file.read())

# dextable = soup.find('table', {'class': 'dextable'})

# images = dextable.find_all('img')
# pokemon = {}
# pokemon['spriteSrc'] = rooturl + str(images[0].get('src'))
# pokemon['shinySpriteSrc'] = rooturl + str(images[1].get('src'))
# pokemon['types'] = []
# pokemon['types'].append(str(images[2].get('src')[len("/pokedex-bw/type/"):][:-4]))
# if len(images) is 4:
#   pokemon['types'].append(str(images[3].get('src')[len("/pokedex-bw/type/"):][:-4]))
# print pokemon