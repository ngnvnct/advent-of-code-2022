"""
a-z = 1-26
A-Z = 27-52
"""

def main():
    ans = []
    total = 0
    with open("day3\input.txt") as r:
        for line in r:
            half = len(line) // 2
            comp1, comp2 = set(), set()
            
            for i in range(half):
                comp1.add(line[i])
                comp2.add(line[half+i])

            ans.extend([letter for letter in comp1 if letter in comp2])
            print(ans)          

    for letter in ans:
        if letter.islower():
            total += (ord(letter) - 96)
        else:
            total += (ord(letter) - 38)

    print(total)

if __name__ == "__main__":
    main()