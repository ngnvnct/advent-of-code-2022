from collections import deque

def main():
    with open("day18\\test.txt") as r:
        coords = [p.split(",") for p in [line for line in r.read().splitlines()]]
        for coord in coords:
            for i,n in enumerate(coord):
                coord[i] = int(n)

    cubes = set(tuple(coord) for coord in coords)

    min_x, max_x, min_y, max_y, min_z, max_z = 0,0,0,0,0,0
    for (x, y, z) in cubes:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    surface_area = 0
    neighbors = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
    
    queue = deque()
    queue.append((min_x, min_y, min_z))
    water_contact = set()
    while queue:
        dx, dy, dz = queue.popleft()
        if (dx, dy, dz) in water_contact:
            continue
        water_contact.add((dx, dy, dz))
        for (nx, ny, nz) in neighbors:
            if min_x <= dx+nx <= max_x and min_y <= dy+ny <= max_y and min_z <= dz+nz <= max_z:
                if (dx+nx, dy+ny, dz+nz) not in cubes:
                    queue.append((dx+nx, dy+ny, dz+nz))
    
    lava_contact = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                if (x,y,z) not in water_contact:
                    lava_contact.add((x,y,z))

    for x, y, z in cubes:
        for (dx, dy, dz) in neighbors:
            if (x+dx, y+dy, z+dz) not in lava_contact:
                surface_area += 1
    
    print(surface_area)

if __name__ == "__main__":
    main()