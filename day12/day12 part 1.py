from collections import deque, defaultdict

def neighbors(matrix, curr):
    x_start, y_start = curr
    valid_neighbor = [(x_start-1, y_start), (x_start+1, y_start), (x_start, y_start-1), (x_start, y_start+1)]
    return [neighbor for neighbor in valid_neighbor if neighbor in matrix] 

def main(): 
    info = defaultdict(list)
    with open("day12\input.txt") as r:
        matrix = {(x,y): ord(val) for y, line in enumerate(r.read().splitlines()) for x, val in enumerate(line)}   # matrix in the form of a dict. Pos lookup is via (x,y) coords. Val is the ord of the letter

    start = [key for key in matrix.keys() if matrix[key] == 83][0]
    matrix[start] = ord("a")
    end = [key for key in matrix.keys() if matrix[key] == 69][0]
    matrix[end] = ord("z")
    info[start], info[end] = [None, 0], [None, 1e8]

    visited, queue = set(), deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        if curr in visited: continue
        if curr != end:
            visited.add(curr)

        for neighbor in neighbors(matrix, curr):
            if matrix[neighbor] - matrix[curr] <= 1:
                queue.append(neighbor)
                if neighbor == end and info[neighbor][1] > info[curr][1]+1:
                    info[neighbor] = [curr, info[curr][1]+1]
                    continue
                info[neighbor] = [curr, info[curr][1]+1]
    print(info[end])

if __name__ == "__main__":
    main()
"""
ord("S") == 83
ord("E") == 69
ord(a-z) == 97-122
"""