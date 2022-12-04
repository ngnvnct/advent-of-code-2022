"""
a-z = 1-26
A-Z = 27-52
"""
def main():
    total = 0
    lines = open("day3\input.txt").read().strip().split("\n")
    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i:i+3]
        [unique] = set(l1) & set(l2) & set(l3)
        group = ord(unique) - 96 if unique.islower() else ord(unique) - 38
        total += group
    print(total)

if __name__ == "__main__":
    main()