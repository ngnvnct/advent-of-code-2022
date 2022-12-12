import numpy as np

def main():
    with open("day10\input.txt") as r:
        cycles = []
        value = 1
        for line in r:
            operation = line.split()
            if len(operation) == 1:
                cycles.append(value)
                continue
            cycles.append(value)
            cycles.append(value)
            value += int(operation[1])
        # Cycles shows the position of the sprite at that cycle
        # sprite is 3 characters wide "###"
        crt = ["." for i in range(240)]

        for cycle, num in enumerate(cycles):
            if num-1 <= cycle%40 <= num+1:
                crt[cycle] = "#"
        
        for i, pixel in enumerate(crt):
            if i%40 == 0:
                print("")
            print(pixel, end=" ")
    
if __name__ == "__main__":
    main()