"""
A and X = rock = +1 point
B and Y = paper = +2 points
C and Z = scissors = +3 points

Lose = +0 points
Draw = +3 points
Win = +6 points
"""
def main():
    points = 0
    score = {"X": 1, "Y": 2, "Z": 3}

    draw = {"X": "A", "Y": "B", "Z": "C"}
    win = {"X": "C", "Y": "A", "Z": "B"}
    lose = {"X": "B", "Y": "C", "Z": "A"}

    with open("day2\input.txt") as r:
        for line in r:
            p1, p2 = line.split(" ")[0], (line.split(" ")[1]).strip("\n")

            points += score[p2]     # Adds points based on what is played

            if draw[p2] == p1:      # Draw
                points += 3
            elif win[p2] == p1:     # Win
                points += 6
            elif lose[p2] == p1:    # Loss
                continue

    print(points)

if __name__ == "__main__":
    main()