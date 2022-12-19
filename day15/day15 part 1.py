def build_sensors(sensors):
    for i, sensor in enumerate(sensors):
            sensors[i] = sensor[10:].strip("xy= ").replace(" y=", "").split(",")
            for j in range(len(sensors[i])):
                sensors[i][j] = int(sensors[i][j])
            sensors[i] = tuple(sensors[i])
    return sensors

def build_beacons(beacons):
    for i, beacon in enumerate(beacons):
        beacons[i] = beacon[22:].strip("xy= ").replace(" y=", "").split(",")
        for j in range(len(beacons[i])):
            beacons[i][j] = int(beacons[i][j])
        beacons[i] = tuple(beacons[i])
    return beacons

def main():
    with open("day15\input.txt") as r:
        sensors, beacons = [], []
        for comp in r.read().splitlines():
            sensors.append(comp.split(":")[0])
            beacons.append(comp.split(":")[1])

    sensors, beacons = build_sensors(sensors), build_beacons(beacons)
    
    manh_dist = []
    for i, sensor in enumerate(sensors):
        (a,b),(x,y) = sensor, beacons[i]
        manh_dist.append((abs(x-a) + abs(y-b)))
    
    coverage = set()
    for i, sensor in enumerate(sensors):
        x,y = sensor
        radius = manh_dist[i]
        for vert in range(radius+1):   
            if (y+vert==2_000_000):
                coverage.add((x, y+vert))
                for horiz in range(radius-vert+1):
                    left_stop, right_stop = x-horiz, x+horiz
                    coverage.add((left_stop, y+vert))
                    coverage.add((right_stop, y+vert))
                    if (left_stop, y+vert) in beacons or (right_stop, y+vert) in beacons:
                        break
            if (y-vert==2_000_000):
                coverage.add((x, y-vert))
                for horiz in range(1, radius-vert+1):
                    left_stop, right_stop = x-horiz, x+horiz
                    coverage.add((left_stop, y-vert))
                    coverage.add((right_stop, y-vert))
                    if (left_stop, y-vert) in beacons or (right_stop, y-vert) in beacons:
                        break
    for beacon in beacons:
        if beacon in coverage:
            coverage.remove(beacon)
    
    print(len(coverage))
    
if __name__ == "__main__":
    main()