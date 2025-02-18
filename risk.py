import json
import math
from random import randrange


with open("map.json") as file:
    clear_map = json.load(file)
with open("entities.json") as file:
    entities =  json.load(file)

updated_map = []


def start_game():
    map_tile_number = len(clear_map)
    tiles_per_entity = math.floor(map_tile_number / len(entities))
    unowned_tiles = clear_map

    for entity in entities:
        print(entity["color"])
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
        print(entity)
    print("tiles distributed and minimum amount of resources assigned to owned tiles")
    initial_resources_distribution(tiles_per_entity)
    print("entity resources distributed throughout all tiles")
    print(updated_map)


def initial_resources_distribution(tiles_per_entity):
    for entity in entities:
        entity_tiles = entity['tiles']
        distribution_per_tile = math.floor(entity['resources_total'] / len(entity['tiles']))
        remaining_resources =  entity['resources_total'] - (distribution_per_tile*len(entity['tiles']))
        print(entity['color'], 'owns the tiles:', entity_tiles)
        for tile in entity['tiles']:
            updated_map[tile]['resources'] += distribution_per_tile
            #currently the remaining resources are assigned to the first cylced tile 
            if entity_tiles[0] == tile:
                updated_map[tile]['resources'] += remaining_resources
            print(updated_map[tile]['resources'])
    return 0
start_game()



#mathplot.lib

