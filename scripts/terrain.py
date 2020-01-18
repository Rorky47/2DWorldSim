import pygame
pygame.init()
class Terrain:


    TSize =  20

    def Load_Texture(file, TSize):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(TSize, TSize))
        surface = pygame.Surface((TSize, TSize), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    grass = Load_Texture("textures\\grass.png", TSize)
    water = Load_Texture("textures\\water.png", TSize)

    tags = {0: grass, 1: water}
