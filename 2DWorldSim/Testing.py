import numpy as np

MAP_SIZE = (500, 500)

class Noise:

    def lerp(a0: float, a1: float, w: float):
        return(((1.0 - w) * a0) + (w * a1))


    def polynomial(x: float):
        return(x * x * x * (x * (x * 6 - 15) + 10))

    def generate_grid(x: int, y: int):
        grid=[]
        for col in range(x):
            newcol=[]
            for cell in range(y):
                angle=np.random.random_sample() * 2
                newcell=(np.cos(angle * np.pi), np.sin(angle * np.pi))
                newcol.append(newcell)
            grid.append(newcol)
        return grid


    new_grid=generate_grid(MAP_SIZE[0] + 2, MAP_SIZE[1] + 2)


    def dot_grid_gradient(ix: int, iy: int, x: float, y: float, gradient_grid):

        # Compute the distance vector
        dx=(x - ix)
        dy=(y - iy)

        # Compute the dot-product
        return((dx * gradient_grid[iy][ix][0]) + (dy * gradient_grid[iy][ix][1]))


    def perlin(x: float, y: float, gradient_grid):
        x0=int(np.floor(x))
        y0=int(np.floor(y))
        x1=(x0 + 1)
        y1=(y0 + 1)

        sx = Noise.polynomial(x - x0)
        sy = Noise.polynomial(y - y0)

        # sx = x - x0
        # sy = y - y0

        n0=Noise.dot_grid_gradient(x0, y0, x, y, gradient_grid)
        n1=Noise.dot_grid_gradient(x1, y0, x, y, gradient_grid)
        ix0=Noise.lerp(n0, n1, sx)

        n0=Noise.dot_grid_gradient(x0, y1, x, y, gradient_grid)
        n1=Noise.dot_grid_gradient(x1, y1, x, y, gradient_grid)
        ix1=Noise.lerp(n0, n1, sx)

        return(Noise.lerp(ix0, ix1, sy))


base_grid = Noise.generate_grid(MAP_SIZE[0], MAP_SIZE[1])
med_grid = Noise.generate_grid(MAP_SIZE[0], MAP_SIZE[1])
fine_grid = Noise.generate_grid(MAP_SIZE[0], MAP_SIZE[1])


class Generator:

    def map_gen(map_size = MAP_SIZE):
        OFFSET=0
        BASE_SCALE=0.09
        MED_SCALE=0.2
        FINE_SCALE=0.009
        BASE_VARIATION=1.0
        MED_VARIATION=0.4
        FINE_VARIATION=0.1
        SEA_LEVEL=0
        MTN_HEIGHT=0.4
        MTN_PEAK=0.55
        BEACH_SIZE = 0.1
        SHORE_WIDTH = 0.1

        new_map = [map_size]
        for y in range(map_size[1]):
            for x in range(map_size[0]): 
                elev = ((Noise.perlin(y * BASE_SCALE + OFFSET, x * BASE_SCALE + OFFSET, base_grid) * BASE_VARIATION) + (Noise.perlin(y * MED_SCALE + OFFSET, x * MED_SCALE + OFFSET, med_grid) * MED_VARIATION) + (Noise.perlin(y * FINE_SCALE + OFFSET, x * FINE_SCALE + OFFSET, fine_grid) * FINE_VARIATION))
                if elev < SEA_LEVEL - SHORE_WIDTH:
                    new_map.append([(x, y), 0])
                elif elev < SEA_LEVEL:
                    new_map.append([(x, y), 1])
                elif elev < SEA_LEVEL + BEACH_SIZE:
                    new_map.append([(x, y), 2])
                elif elev < MTN_HEIGHT:
                    new_map.append([(x, y), 3])
                elif elev < MTN_HEIGHT + MTN_PEAK:
                    new_map.append([(x, y), 4])
                else:
                    new_map.append([(x, y), 5])

        return new_map
    
    def save_map(map, name = "world"):
        with open(name + ".map", "w") as world_map:
            world_map.write(str(map))
    
    def create_map(map_size = MAP_SIZE):
        Generator.save_map(Generator.map_gen(map_size))


Generator.create_map()