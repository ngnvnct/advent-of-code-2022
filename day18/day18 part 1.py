def main():
    with open("day18\input.txt") as r:
        coords = [p.split(",") for p in [line for line in r.read().splitlines()]]
        for coord in coords:
            for i,n in enumerate(coord):
                coord[i] = int(n)

    cubes = set(tuple(coord) for coord in coords)

    surface_area = 0
    neighbors = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

    for x, y, z in coords:
        for dx, dy, dz in neighbors:
            if (x+dx, y+dy, z+dz) not in cubes:
                surface_area += 1
    
    print(surface_area)

if __name__ == "__main__":
    main()