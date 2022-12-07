def main():
    r = open("day6\input.txt")
    line = str(r.readline()).rstrip()

    for i in range(-1, len(line)-4):
        window = line[i+1:i+5]

        if not len(set(window)) == 4:
            continue

        print(i+5)
        break

    r.close()

if __name__ == "__main__":
    main()