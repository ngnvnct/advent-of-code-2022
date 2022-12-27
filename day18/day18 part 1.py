from collections import Counter

def main():
    with open("day18\input.txt") as r:
        coords = [p.split(",") for p in [line for line in r.read().splitlines()]]
        for coord in coords:
            for i,n in enumerate(coord):
                coord[i] = int(n)

    cubes = set(tuple(coord) for coord in coords)

    exposed = Counter()
    neighbors = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

    for x, y, z in coords:
        for dx, dy, dz in neighbors:
            if (x+dx, y+dy, z+dz) not in cubes:
                exposed[(x, y, z)] += 1
    
    area = sum(exposed.values())
    print(area)

if __name__ == "__main__":
    main()