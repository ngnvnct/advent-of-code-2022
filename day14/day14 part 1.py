import numpy as np
from collections import defaultdict

def build(cave_walls, matrix, min_x):
    for wall in cave_walls.values():    # building the cave in the numpy matrix
        for i in range(1, len(wall)):
            x_before, y_before = wall[i-1][0]-min_x, wall[i-1][1]
            curr_x, curr_y = wall[i][0]-min_x, wall[i][1]
            matrix[y_before][x_before] = -1
            while curr_x != x_before or curr_y != y_before:
                if curr_x > x_before:
                    x_before += 1
                elif curr_x < x_before:
                    x_before -= 1
                if curr_y > y_before:
                    y_before += 1
                elif curr_y < y_before:
                    y_before -= 1
                matrix[y_before][x_before] = -1
    return matrix    

def main():
    np.set_printoptions(threshold=np.inf)
    with open("day14\input.txt") as r:
        cave_walls = defaultdict(list)      # key = wall # ; value = coords that make up the wall in a list
        for i, wall in enumerate([l.split("->") for l in r.read().splitlines()]):   # Enumerates through a 2D array of the walls and the coords that make up the walls. coords[wall unit][coords]
            for xy in wall:
                (x, y) = xy.split(",")
                cave_walls[i].append((int(x),int(y)))

    min_x, max_x, max_y = 1e8, 0, 0
    for wall in cave_walls.values():
        for x,y in wall:
            min_x, max_x, max_y = min(min_x, x), max(max_x, x), max(max_y, y)
    print(min_x, max_x, max_y)

    source = (0, (0+(500-min_x)))

    matrix = np.full((max_y+1, (max_x-min_x)+1), 0)   # "empty" numpy array of the cave. Walls will be filled in as "#". 
    matrix = build(cave_walls, matrix, min_x)

    sand_y, sand_x = source
    while True:
        block = True
        for dir_y, dir_x in ((1,0), (1,-1), (1,1)):
            if matrix[sand_y+dir_y][sand_x+dir_x] == 0:
                sand_y += dir_y
                sand_x += dir_x
                block = False
                break
        if sand_y >= max_y or sand_x < 0 or sand_x > max_x:
            break
        if block:
            matrix[sand_y][sand_x] = 1
            if (sand_y, sand_x) == source:
                break
            sand_y, sand_x = source
    grains = np.sum(matrix, where=matrix == 1)
    print(grains)
    

if __name__ == "__main__":
    main()