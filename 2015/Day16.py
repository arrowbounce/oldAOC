base = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes":1
}

with open("Day16") as f:
    for line in f:
        sue = line.split()
        print sue
        issue = True
        for a in range(2, 7, 2):
            role = sue[a].replace(":", "")
            amount = int(sue[a+1].replace(",", ""))
            if role == "cats" or role == "trees":
                if base[role] >= amount:
                    issue = False
                    break
            elif role == "pomeranians" or role == "goldfish":
                if base[role] <= amount:
                    issue = False
                    break
            elif base[role] != amount:
                issue = False
                break
        if issue:
            print sue[1]
            break