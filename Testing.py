import numpy as np

MAP_SIZE = (30, 30)


class Generator:


    def map_gen(map_size = MAP_SIZE):
        new_map = [map_size]
        for y in range(map_size[1]):
            for x in range(map_size[0]):
                new_map.append([(x, y), np.random.randint(0, 1 + 1)])
        return new_map
    
    def save_map(map, name = 'world'):
        with open(name + ".map", "w") as world_map:
            world_map.write(str(map))
    
    def create_map(map_size = MAP_SIZE):
        Generator.save_map(Generator.map_gen(map_size))

    def perlin_noise(map_size = MAP_SIZE, scale, (x, y)):
        

Generator.create_map()