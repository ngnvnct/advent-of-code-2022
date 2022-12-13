def main():
    with open("day11\input.txt") as r:
        file = r.read().splitlines()        # each element is the separate line
    
    items = [[int(n) for n in file[x][18:].split(", ")] for x in range(1, len(file), 7)]     # 2D array of each monkey and what worry level each item is => items[monkey #][item's worry level]
    operations = [[c for c in file[x][23:].split(" ")] for x in range(2, len(file), 7)]             # 2D array of each monkey's operation to an item's worry level. 0th element is operator and 1st element is amount
    test = [int(file[x][21:]) for x in range(3, len(file), 7)]                                      # Array of each monkey's test check. Every test is a divisible check. Worry levels are checked to see if they are divisible by test[monkey #]
    toss = [[int(file[x+1][30:]), int(file[x][29:])] for x in range(4, len(file), 7)]               # 2D array of which monkey the current monkey will pass their item to. 0th index is if False, 1st index is if True => toss[monkey #][False 0/True 1]
    amount = [0 for _ in range(len(items))]

    for _ in range(20):
        for i, monkey in enumerate(items):
            if not items[i]: continue
            for item in list(monkey):
                operator = operations[i][0]
                curr = (((item*item if operations[i][1] == "old" else item*int(operations[i][1])) if operator == "*" else item+int(operations[i][1])) // 3) # lol
                items[toss[i][not bool(curr % test[i])]].append(curr)     
                amount[i] += 1
            items[i] = []
    print(sorted(amount)[-1]*sorted(amount)[-2])
               
if __name__ == "__main__":
    main()
"""
Monkey takes first item in list
Worry level has the operation performed
Worry level is divided by 3
Worry level is checked
Item is passed to the next monkey depending on if check passes or fails
    Item is appended onto next monkey's list (at the end)
In a turn, the monkeys inspect and pass all of their items until it has nothing left
    Record how many items each monkey inspects over the course of 20 rounds
If a monkey starts a turn with nothing, their turn is over
A ROUND is when every monkey is done with their turn
"""