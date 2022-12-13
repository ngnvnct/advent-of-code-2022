import math
import numpy as np  # read some vector shit

def main():
    with open("day9\input.txt") as r:
        hsh = {"L": [-1,0], "R": [1,0], "D": [0,-1], "U": [0,1]}
        rope = np.zeros((10,2)) # 10 elements of [0 0]
        visited = set()        # Keeps track of the coords that tail travels over
        for line in r:
            direction, dist = line.split()
            dist = int(dist)
            for i in range(dist):
                rope[0] += hsh[direction]
                for knot in range(1, len(rope)):
                    diff = rope[knot-1] - rope[knot]
                    if np.linalg.norm(diff) > 2:
                        rope[knot] += np.sign(diff)     # adds +/- 1 to both elements
                    elif np.linalg.norm(diff) == 2:
                        rope[knot] += diff / np.linalg.norm(diff)   # adds 1 to the non 0 element
                visited.add(tuple(rope[-1]))
        print(len(visited))

if __name__ == "__main__":
    main()