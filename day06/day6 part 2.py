def main():
    r = open("day6\input.txt")
    line = r.readline().rstrip()

    for i in range(-1, len(line)-14):
        window = line[i+1:i+15]

        if not len(set(window)) == 14:
            continue

        print(i+15)
        break

    r.close()

if __name__ == "__main__":
    main()