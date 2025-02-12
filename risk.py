import json
import math
from random import randrange

with open("map.json") as file:
    clear_map = json.load(file)
with open("entities.json") as file:
    entities =  json.load(file)


def start_game():
    map_tile_number = len(clear_map)
    tiles_per_entity = math.floor(map_tile_number / len(entities))
    for entity in entities:
        print(entity["color"])
        x = 0
        while x < tiles_per_entity:
            rng_number = randrange(map_tile_number)
            taken_tile = clear_map[rng_number]
            if taken_tile['owner'] == None:
                print(1)
                taken_tile['owner'] = entity['color']
                print(taken_tile)
                x += 1
            else:
                print(taken_tile,'tile already owned')
                
                
        return 0

start_game()