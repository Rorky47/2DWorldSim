from ast import literal_eval
import pygame
from scripts.terrain import *


class Map_Render:
    

    def add_tile(tile, pos, add_to):
        
        add_to.blit(Terrain.tags[tile], (pos[0]* Terrain.TILE_SIZE, pos[1]* Terrain.TILE_SIZE))

    def load_Map(file):
        with open(file, "r") as mapfile:
            map_data = literal_eval(mapfile.read())
            map_size = [map_data[0]][0]
            map_tiles = map_data[1:]
        terrain = pygame.Surface([dim * Terrain.TILE_SIZE for dim in map_size], pygame.HWSURFACE)

        for tile in map_tiles:
            if tile[1] in Terrain.tags:
                Map_Render.add_tile(tile[1], tile[0], terrain)
        return terrain
