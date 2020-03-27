import pygame

pygame.init()
class Terrain:


    TILE_SIZE =  20

    def Load_Texture(file, TILE_SIZE):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(TILE_SIZE, TILE_SIZE))
        surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    ground = Load_Texture("textures\\grass.png", TILE_SIZE)
    ocean = Load_Texture("textures\\ocean.png", TILE_SIZE)
    coast = Load_Texture("textures\\water.png", TILE_SIZE)
    beach = Load_Texture("textures\\beach.png", TILE_SIZE)
    mtn = Load_Texture("textures\\mtn.png", TILE_SIZE)
    peak = Load_Texture("textures\\mtntop.png", TILE_SIZE)

    tags = {0: ocean, 1: coast, 2: beach, 3: ground, 4: mtn, 5: peak}
