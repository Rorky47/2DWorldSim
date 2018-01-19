import pygame
from scripts.terrain import *

class Map_Render:
    def add_tile(tile, pos, addTo):
        addto.blit(tile,(pos[0]* Terrain.TSize, pos[1]* Terrain.TSize))


    def load_Map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        map_data = map_data.split("-")

        map_size = map_data[len(map_data) - 1]
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Terrain.TSize
        map_size[1] = int(map_size[1]) * Terrain.TSize

        tiles = []

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))

        for tile in tiles:
            tile[0] = tile[0].split(",")
            pos = tile[0]
            for p in pos:
                print(p)
                pos[pos.index(p)] = int(p)
            tiles[tiles.index(tiles)] = (pos, tile[1])

        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.Texture_Tags:
                Map_Engine.add_tile(Terrain.Terrain_tags(tile[1], tile[1], terrain))
        return terrain
