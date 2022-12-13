import math

def main():
    with open("day9\input.txt") as r:
        hsh = {"L": [-1,0], "R": [1,0], "D": [0,-1], "U": [0,1]}
        head, tail = [0,0], [0,0]
        visited = set()        # Keeps track of the coords that tail travels over
        for line in r:
            direction, dist = line.split()
            dist = int(dist)
            for i in range(dist):
                head[0] += hsh[direction][0]
                head[1] += hsh[direction][1]
                a = head[0] - tail[0]
                b = head[1] - tail[1]
                if math.sqrt((a**2) + (b**2)) > math.sqrt(2):   # pythagorean distance. i never took linear algebra so idk fancy vector shit
                    tail[0] = head[0] - hsh[direction][0]
                    tail[1] = head[1] - hsh[direction][1]                
                elif (abs(head[0] - tail[0]) == 2 and head[1] == tail[1]) or (abs(head[1] - tail[1]) == 2 and head[0] == tail[0]): # if H and T are 2 spaces apart and on the same line
                    tail[0] += hsh[direction][0]
                    tail[1] += hsh[direction][1]
                visited.add(tuple(tail))      
        print(len(visited))

if __name__ == "__main__":
    main()