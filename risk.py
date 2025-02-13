import json
import math
from random import randrange

with open("map.json") as file:
    clear_map = json.load(file)
with open("entities.json") as file:
    entities =  json.load(file)

updated_map = []

#utils func
def calculate_best_positioning_for_remaining_resources(entity_tiles):
    for tiles in entity_tiles:
        temp_borders = entity_tiles
#




def start_game():
    map_tile_number = len(clear_map)
    tiles_per_entity = math.floor(map_tile_number / len(entities))
    unowned_tiles = clear_map

    for entity in entities:
        #print(entity["color"])
        entity['tiles'] = []
        x = 0
        while x < tiles_per_entity:
            tile = unowned_tiles[randrange(len(unowned_tiles))]
            tile['owner'] = entity["color"]
            unowned_tiles.remove(tile)
            tile['resources'] = 1
            entity['resources_total'] -= 1
            entity['owned_tiles'] += 1
            entity['tiles'].append(tile['id'])
            updated_map.append(tile)
            x += 1
        #print(entity)
    print("tiles distributed and minimum amount of resources assigned to owned tiles")
    initial_resources_distribution(tiles_per_entity)



def initial_resources_distribution(tiles_per_entity):
    for entity in entities:
        entity_tiles = entity['tiles']
        #print(entity['color'])
        for tile in entity['tiles']:
            distribution_per_tile = math.floor(entity['resources_total'] / len(entity['tiles']))
            remaining_resources =  entity['resources_total'] - (distribution_per_tile*len(entity['tiles']))
            updated_map[tile]['resources'] += distribution_per_tile
            print(entity_tiles)
            if tile == entity['tiles'][0]:
                calculate_best_positioning_for_remaining_resources(entity_tiles)
    return 0
start_game()


