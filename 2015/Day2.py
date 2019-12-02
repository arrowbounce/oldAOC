total = 0
with open("Day2") as f:
    for line in f:
        row = line.split('x')
        row = [int(i) for i in row]
        row.sort()
        total += 3*row[0]*row[1] + 2*row[2]*(row[0]+row[1])
print total