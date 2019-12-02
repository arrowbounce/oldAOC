total = 0
pos = 1
with open("day1") as f:
	for line in f:
		for ch in line:
			if ch =='(':
				total += 1
			else:
				total -= 1
			if total == -1:
				print pos
				break
			pos += 1
		# up = line.count('(')
		# down = line.count(')')
		# total = up - down
print total