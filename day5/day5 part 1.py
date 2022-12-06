import re

def columns():
    file = open("day5\input.txt")
    line = str(file.readline())
    columns = (len(line)+1) // 4
    file.close()
    return columns

def build(col):
    stacks = [[] for i in range(col)]
    with open("day5\input.txt") as r:
        for line in r:
            if line == "\n":
                break
            for i, char in enumerate(line):
                if char.isalpha():
                    stacks[i//4].append(char)
    return stacks

def instructions():
    instructions = []
    build = False
    with open("day5\input.txt") as r:
        for line in r:
            if line == "\n":
                build = True
                continue
            if build:
                move = re.findall(r'\d+', line)
                instructions.append(list(map(int,move)))

    return instructions

def main():
    col = columns()

    boxes = build(col)
    for i in range(len(boxes)):
        boxes[i].reverse()

    moves = instructions()      # moves = [amount to move, start, end]
    
    for step in moves:
        for i in range(step[0]):
            boxes[step[2]-1].append(boxes[step[1]-1].pop())

    for i in range(len(boxes)):
        print(boxes[i].pop(), end="")

if __name__ == "__main__":
    main()