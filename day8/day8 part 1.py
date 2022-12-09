def main():
    grid = []
    with open("day8\input.txt") as r:       # build the grid/matrix
        for i, line in enumerate(r):
            grid.append([])
            for n in line.rstrip():
                grid[i].append(int(n))

    rows, cols = len(grid), len(grid[0])
    visible = set()

    for row in range(rows):     # checking left to right
        curr_tallest = 0
        for col in range(cols):
            if col == 0:
                curr_tallest = grid[row][col]
                visible.add((row, col))
                continue

            if grid[row][col] > curr_tallest:
                curr_tallest = grid[row][col]
                visible.add((row, col))

    for row in range(rows):     # checking right to left
        curr_tallest = 0
        for col in range(cols-1, -1, -1):
            if col == cols -1:
                curr_tallest = grid[row][col]
                visible.add((row, col))
                continue
            
            if grid[row][col] > curr_tallest:
                curr_tallest = grid[row][col]
                visible.add((row, col))

    for col in range(cols):     # checking top to bottom
        curr_tallest = 0
        for row in range(rows):
            if row == 0:
                curr_tallest = grid[row][col]
                visible.add((row, col))
                continue

            if grid[row][col] > curr_tallest:
                curr_tallest = grid[row][col]
                visible.add((row, col))

    for col in range(cols):     # checking bottom to top
        curr_tallest = 0
        for row in range(rows-1, -1, -1):
            if row == rows-1:
                curr_tallest = grid[row][col]
                visible.add((row, col))
                continue

            if grid[row][col] > curr_tallest:
                curr_tallest = grid[row][col]
                visible.add((row, col))
    
    print(len(visible))

if __name__ == "__main__":
    main()