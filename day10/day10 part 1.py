def main():
    with open("day10\input.txt") as r:
        cycles = [1]
        value = 1
        for line in r:
            operation = line.split()
            if len(operation) == 1:
                cycles.append(value)
                continue
            cycles.append(value)
            cycles.append(value)
            value += int(operation[1])

        strength = []
        for i in range(20, 221, 40):
            strength.append((i)*cycles[i])

        print(sum(strength))

if __name__ == "__main__":
    main()