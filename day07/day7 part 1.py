def main():
    with open("day7\input.txt") as r:
        path, hsh = [], {}
        for line in r:
            parts = line.split()
            if parts[0] == "$" and parts[1] == "cd":
                if parts[2] == "..":      # checks if we are going down or up the path
                    curr = "/".join(path)
                    path.pop()
                    hsh["/".join(path)] += hsh[curr]
                    continue
                path.append(parts[2])
                if "/".join(path) not in hsh:
                    hsh["/".join(path)] = 0
            elif parts[1] == "ls" or parts[0] == "dir":
                continue
            else:
                hsh["/".join(path)] += int(parts[0])
    total = 0
    for values in hsh.values():
        if values <= 100000:
            total += values
    print(total)

if __name__ == "__main__":
    main()