
import requests, json
poke_list = requests.get("https://pokeapi.co/api/v2/pokemon/")

def get_info(*nums):
    pokemon_info = []
    
    for num in nums:
        single_poke = {}
        poke = requests.get(poke_list.json()['results'][num-1]['url']).json()
        sprite_page = requests.get(poke['forms'][0]['url']).json()
        
        single_poke['Name'] = poke['forms'][0]['name']
        single_poke['Ability 1'] = poke['abilities'][0]['ability']['name']
        single_poke['Ability 2'] = poke['abilities'][1]['ability']['name']
        single_poke['Base Experiance'] = poke['base_experience']
        single_poke['Sprite URL'] = sprite_page['sprites']['front_shiny']
        
        pokemon_info.append(single_poke)
        
    return pokemon_info

#get_info(1,2,3,4,5)