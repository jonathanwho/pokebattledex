#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os, sys, webapp2, jinja2, json, operator, logging, difflib
from pokemon_data import pokemon_dict
from pokemon_data import pokemon_list
from pokemon_damage import pokemon_types
from pokemon_damage import pokemon_damage_dict
from pokemon_abilities import pokemon_abilities_list
from pokemon_abilities import pokemon_abilities_dict
from random import randint

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                 autoescape = True, extensions=['jinja2.ext.loopcontrols'])

"""
  Helper method to render templates. 
"""
def render_str(self, template, **params):
  t = jinja_env.get_template(template)
  return self.response.write(t.render(params))

"""
  Sanitizes a term for pokemon_damage_dict. 
"""
def dictionary_sanitize(term):
  return term.strip().lower()

"""
  Returns the closest matching pokemon name.
"""
def get_closest_pokemon(pokemon):
  # TODO: Kyurem returns Kyogre 
  pokemon = pokemon[0].upper() + pokemon[1:] 
  results = difflib.get_close_matches(pokemon[:-1] + pokemon[-1].upper(),
    pokemon_list)
  return results[0] if len(results) else None

"""
  Calculates the damage taken for a pokemon with types |input_types|
  
  param
    input_types The types of the pokemon.
  return
    a dictionary of all the pokemon types and the corresponding damage it will
    do to a pokemon with these |input_types|

  TODO: Take abilities into consideration.
"""
def get_damage_taken(input_types):
  damages = dict()
  for x in pokemon_types:
    damages[x] = 1

  for pokemon_type in input_types:
    for x in pokemon_types:
      damages[x] *= pokemon_damage_dict[dictionary_sanitize(pokemon_type)][x]

  weakness = dict()
  resistance = dict()
  for x in pokemon_types:
    if damages[x] > 1:
      weakness[x] = damages[x]
    elif damages[x] < 1:
      resistance[x] = damages[x]

  damages = dict()
  damages['weakness'] = weakness
  damages['resistance'] = resistance 
  return damages

def get_img_src(pokemon):
  pokemon = get_closest_pokemon(pokemon).lower()
  pokemon = pokemon.replace(' ', '-')
  if "mega-" in pokemon:
    pokemon = pokemon[5:] + "-mega"
  if "cloak)" in pokemon:
    pokemon = pokemon.replace('cloak', '')
  if "form)" in pokemon:
    pokemon = pokemon.replace('form', '')
  if "mode)" in pokemon:
    pokemon = pokemon.replace('mode', '')

  pokemon = str(pokemon).translate(None, '()')

  if pokemon[-1] == '-':
    pokemon = pokemon [:len(pokemon) - 1]
  if "-normal" in pokemon:
    pokemon = pokemon.replace('-normal', '')
  if "-standard" in pokemon:
    pokemon = pokemon.replace('-standard', '')
  return pokemon

def get_stats(stats):
  stat = dict()
  stat["hp"] = stats[0]
  stat["atk"] = stats[1]
  stat["def"] = stats[2]
  stat["spatk"] = stats[3]
  stat["spdef"] = stats[4]
  stat["spd"] = stats[5]
  return stat

bg_images = [
  "bg.jpg",  
  "bg-beachshore.png", 
  "bg-beach.png",
  "bg-volcanocave.png", 
  "bg-thunderplains.png", 
  "bg-route.png", 
  "bg-river.png", 
  "bg-mountain.png", 
  "bg-meadow.png",  
  "bg-icecave.png", 
  "bg-forest.png", 
  "bg-earthycave.png", 
  "bg-desert.png", 
  "bg-deepsea.png", 
  "bg-dampcave.png", 
  "bg-city.png"]

def get_background_image():
  index = randint(0, len(bg_images) - 1)
  return bg_images[index]

class MainHandler(webapp2.RequestHandler):
  def get(self, pokemon=None):
    if pokemon:
      pokemon = get_pokemon_stats(pokemon)
    render_str(self, "index.html", pokemon_list = pokemon_list, 
      pokemon = pokemon)

def get_pokemon_stats(pokemon):
  try:
    pokemon_data = pokemon_dict[get_closest_pokemon(pokemon)]
    pokemon = dict()
    pokemon['name'] = pokemon_data["name"].decode("utf-8") 
    pokemon['stats'] = get_stats(pokemon_data["stats"])
    pokemon['types'] = pokemon_data["types"]
    pokemon['abilities'] = []
    for ability in pokemon_data["abilities"].split(','):
      pokemon['abilities'].append((ability.decode("utf-8"), 
       pokemon_abilities_dict[ability.strip()].decode("utf-8")))
    pokemon['damage_taken'] = get_damage_taken(pokemon['types'].split(",")) 
    pokemon['img_src'] = get_img_src(pokemon['name'])
    pokemon['background_img'] = get_background_image()
    return pokemon
  except KeyError:
    return None 

class PokemonStatHandler(webapp2.RequestHandler):
  def get(self, pokemon): 
    pokemon = get_pokemon_stats(pokemon)
    render_str(self, "stats.html", pokemon = pokemon)


app = webapp2.WSGIApplication([
  ('/', MainHandler), 
  webapp2.Route(r'/stats/<pokemon:(.*)>', handler=PokemonStatHandler),
  webapp2.Route(r'/<pokemon:(.*)>', handler=MainHandler),
], debug=True)
