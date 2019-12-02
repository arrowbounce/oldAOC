count = 0
with open("Day5") as f:
	for line in f:
		prev = None
		v = 0
		n2 = 0 #has double
		n3 = 0 #doesn't have ab cd pq or xy
		for ch in line:
			if prev is not None:
				if prev == ch:
					n2 += 1
				if (prev == "a" and ch == "b") or (prev == "c" and ch == "d") or (prev == "p" and ch == "q") or (prev == "x" and ch == "y"):
					n3 = 1
					break
			if ch in ["a", "e", "i", "o", "u"]:
				v += 1
			prev = ch
		if n3 != 1:
			if n2 > 0 and v >=3:
				count += 1
print count
