diff = 0
with open("Day8") as f:
	for line in f:
		i = 0
		while i< len(line):
			if line[i] == "\"":
				diff += 1
			elif line[i] == "\\":
				i += 1
				if line[i] == "x":
					diff += 3
					i += 2
				else:
					diff += 1
			i += 1
print diff