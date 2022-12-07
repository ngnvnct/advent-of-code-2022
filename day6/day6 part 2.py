def check(window):
    unique = set()
    for c in window:
        if c in unique:
            return False
        unique.add(c)
    return True

def main():
    r = open("day6\input.txt")
    line = str(r.readline()).rstrip()

    for i in range(-1, len(line)-14):
        window = line[i+1:i+15]

        if not check(window):
            continue

        print(i+15)
        break

    r.close()

if __name__ == "__main__":
    main()