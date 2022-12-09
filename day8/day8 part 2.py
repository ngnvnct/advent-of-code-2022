def check(y, x, grid, height, max_rows, max_cols):
    dist = 0

    row = y
    y += 1
    while y < max_rows-1 and grid[y][x] < height:
        dist += 1
        y += 1
    score, dist = dist+1, 0

    y = row
    y -= 1
    while y > 0 and grid[y][x] < height:
        dist += 1
        y -= 1
    score *= (dist + 1)
    
    dist, y = 0, row

    col = x
    x += 1
    while x < max_cols-1 and grid[y][x] < height:
        dist += 1
        x += 1
    score *= (dist + 1)
    
    dist, x = 0, col

    x -= 1
    while x > 0 and grid[y][x] < height:
        dist += 1
        x -= 1
    score *= (dist + 1)
    return score

def main():
    grid = []
    with open("day8\input.txt") as r:       # build the grid/matrix
        for line in r:
            grid.append([int(n) for n in line.strip()])

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

    best = 0
    for row, col in visible:
        height = grid[row][col]
        best = max(best, check(row, col, grid, height, rows, cols))
    print(best)

if __name__ == "__main__":
    main()