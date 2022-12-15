from ast import literal_eval

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for num in map(compare, left, right):
            if num:
                return num
        return compare(len(left), len(right))

def main():
    with open("day13\input.txt") as r:
        packets = [[*map(literal_eval, p.split())] for p in r.read().split("\n\n")]     # list of packet pairs
        ans = [i for i, p in enumerate(packets, 1) if compare(*p) == 1]     # counts the correct indices where order is correct 
 
    distress = [val for p in list(packets) for val in p] + [[[2]], [[6]]]
    p1 = [1 for p in distress if compare(p, [[2]]) == 1]
    p2 = [1 for p in distress if compare(p, [[6]]) == 1]
    print((1+sum(p1)) * (1+sum(p2)))


if __name__ == "__main__":
    main()

