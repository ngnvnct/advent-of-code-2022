from collections import defaultdict

def main():
    rate, path = defaultdict(lambda: 0), defaultdict(list)
    with open("day16\\test.txt") as r:
        line = [l.rstrip().split("; ") for l in r]
        print(line)
        for valve in line:
            rate[str(valve[0][6:8])] = int(valve[0][23:])
            path[str(valve[0][6:8])] = valve[1].replace("tunnels lead to valves ", "").replace("tunnel leads to valve ", "").replace(" ", "").split(",")
        print(f"{rate}\n{path}")

if __name__ == "__main__":
    main()