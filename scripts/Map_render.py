from ast import literal_eval
import pygame
from scripts.terrain import *

SCALE_FACTOR == 50

class Map_Render:
    

    def add_tile(tile, pos, add_to):
        add_to.blit(Terrain.tags[tile], (pos[0]* Terrain.TSize, pos[1]* Terrain.TSize))


    def load_Map(file):
        with open(file, "r") as mapfile:
            map_data = literal_eval(mapfile.read())
            map_size = [map_data[0]][0]
            map_tiles = map_data[1:]
        terrain = pygame.Surface([dim * SCALE_FACTOR for dim in map_size], pygame.HWSURFACE)

        for tile in map_tiles:
            if tile[1] in Terrain.tags:
                Map_Render.add_tile(tile[1], tile[0], terrain)
        return terrain
