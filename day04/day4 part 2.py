def main():
    amount = 0
    with open("day4\input.txt") as r:
        for line in r:
            first, second = list(map(int, (line.split(",")[0]).split("-"))), list(map(int, (line.split(",")[1].strip()).split("-")))    # Returns list of string-to-int elements
            if first[0] <= second[1] and first[1] >= second[0]:
                amount += 1
            # if not (first[1] < second[0] or first[0] > second[1]):
            #   amount += 1
    print(amount)

if __name__ == "__main__":
    main()