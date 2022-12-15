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

    print(sum(ans))   

if __name__ == "__main__":
    main()