def main():
    greatest = 0
    add = 0
    try:
        with open("day1\input.txt") as r:
            for line in r:
                if line == "\n":
                    if add > greatest:
                        greatest = add
                    add = 0
                else:
                    add += int(line)
    except FileNotFoundError:
        print("File not found")
    
    print(f"{greatest}")
    return greatest

if __name__ == "__main__":
    main()