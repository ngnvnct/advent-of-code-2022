def main():
    grid = []
    with open("day8\input.txt") as r:       # build the grid/matrix
        for line in r:
            grid.append([int(n) for n in line.strip()])

    rows, cols = len(grid), len(grid[0])
    visible = set()

    for r in range(1, rows-1):
        for c in range(1, cols-1):
            for up_down, left_right in ((1,0), (-1,0), (0,1), (0,-1)):      # For each cell, check the lateral neighbors in the while loop
                y, x = r, c
                neighbors = []
                while 0 <= y + up_down < rows and 0 <= x + left_right < cols:
                    y += up_down
                    x += left_right
                    neighbors.append(grid[y][x])    # We will be comparing the current cell grid[r][c] to all values in the same row/col to see if there is a taller tree in the way
                if grid[r][c] > max(neighbors):     # Yes => visible to that edge/able to see the edge from that tree; No => not visible since there is a taller tree in the LOS
                    visible.add((r, c))
    print(len(visible) + (rows-1)*2 + (cols-1)*2)

if __name__ == "__main__":
    main()