total = 0
with open("day1") as f:
	for line in f:
		up = line.count('(')
		down = line.count(')')
		total = up - down
print total