import numpy as np
from itertools import cycle

def main():
    directions = {"<": np.array([-1,0]), ">": np.array([1,0])}
    rocks = [
        np.array([[0,0], [1,0], [2,0], [3,0]]), # horizontal line
        np.array([[1,0], [0,1], [1,1], [2,1], [1,2]]), # plus
        np.array([[0,0], [1,0], [2,0], [2,1], [2,2]]), # backwards L
        np.array([[0,0], [0,1], [0,2], [0,3]]), # vertical line
        np.array([[0,0], [1,0], [0,1], [1,1]]) # box
        ]   # coords are [x, y] built from bottom up
    with open("day17\input.txt") as r:
        arrows = [char for char in r.read()]

    rocks_cycle, arrows_cycle = cycle(rocks), cycle(arrows)
    cave = np.zeros((9, (4*2022)+1), dtype=int)
    cave[:, 0], cave[0, :], cave[-1, :] = 1, 1, 1
    highest = 0     # will be the highest point of the rock formation

    for _ in range(2022):
        rock = next(rocks_cycle)
        spawn = np.array([3, highest+4])  # 2 away from left wall, 3 above the highest point
        pos = rock + spawn  
        while True:
            direction = next(arrows_cycle)
            move = pos + directions[direction]
            if not any([cave[tuple(coord)] for coord in move]) != 0: # makes a list of the values at the cave coordinates after moving left or right. 
                pos = move
            down = np.array([0,-1])
            move = pos + down
            if any([cave[tuple(coord)] for coord in move]): # if any of the coords != 0 after the down move, do not update position. break loop, rock as reached rest
                break
            pos = move
        for p in pos:
            cave[tuple(p)] = 1
            highest = max(highest, p[1])

    print(highest)

if __name__ == "__main__":
    main()

"""
####

 #
###
 #

  #
  #
###

#
#
#
#

##
##

Each rock's left edge spawns 2 units away from left wall and 3 units above highest rock/the floor(if there is no rock below)
"""