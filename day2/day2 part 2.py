"""
A = +1 = Rock
B = +2 = Paper
C = +3 = Scissors

X = Lose = +0
Y = Draw = +3
Z = Win = +6
"""
def main():
    points = 0
    
    result = {"X": 0, "Y": 3, "Z": 6}
    win = {"A": 2, "B": 3, "C": 1}
    draw = {"A":1, "B": 2, "C": 3}
    lose = {"A": 3, "B": 1, "C": 2}

    with open("day2\input.txt") as r:
        for line in r:
            p1, p2 = line.split(" ")[0], (line.split(" ")[1]).strip("\n")

            points += result[p2]

            if p2 == "Y":
                points += draw[p1]
            elif p2 == "Z":
                points += win[p1]
            else:
                points += lose[p1]

    print(points)

if __name__ == "__main__":
    main()