bottles = []

with open("Day17") as f:
    for line in f:
        bottles.append(int(line))

def check(num, amount, bottles, count):
    if num == len(bottles):
        if amount == 150:
            return [1, count]
        return [0, 999999]
    withb = check(num + 1, amount + bottles[num], bottles, count + 1) 
    without = check(num+1, amount, bottles, count)
    if withb[1] == without[1]:
        return [withb[0] + without[0], withb[1]]
    if withb[1] < without[1]:
        return withb
    return without
    #return check(num + 1, amount + bottles[num], bottles, count + 1) + check(num+1, amount, bottles, count)
print check(0, 0, bottles, 0)