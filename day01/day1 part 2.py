def main():
    add = 0
    ans = []
    try:
        with open("day1\input.txt") as r:
            for line in r:
                if line == "\n":
                    ans.append(add)
                    add = 0
                else:
                    add += int(line)
    except FileNotFoundError:
        print("File not found")
    
    ans.sort()
    print(f"{ans[-1]}, {ans[-2]}, {ans[-3]}")
    total = ans[-1] + ans[-2] + ans[-3]
    print(f"{total}")

if __name__ == "__main__":
    main()