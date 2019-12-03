count = 0
with open("Day5") as f:
	for line in f:
		hold = set()
		hold1 = None
		hold2 = None
		cond1 = 0
		cond2 = 0
		for ch in line:
			if hold2 is None:
				hold2 = ch
			elif hold1 is None:
				hold1 = hold2
				hold2 = ch
			else:
				if hold1 == ch:
					cond2 += 1
				if hold2 + ch in hold:
					cond1 += 1
				hold.add(hold1+hold2)
				hold1 = hold2
				hold2 = ch
		if cond1 and cond2:
			count += 1

		# prev = None
		# v = 0
		# n2 = 0 #has double
		# n3 = 0 #doesn't have ab cd pq or xy
		# for ch in line:
		# 	if prev is not None:
		# 		if prev == ch:
		# 			n2 += 1
		# 		if (prev == "a" and ch == "b") or (prev == "c" and ch == "d") or (prev == "p" and ch == "q") or (prev == "x" and ch == "y"):
		# 			n3 = 1
		# 			break
		# 	if ch in ["a", "e", "i", "o", "u"]:
		# 		v += 1
		# 	prev = ch
		# if n3 != 1:
		# 	if n2 > 0 and v >=3:
		# 		count += 1
print count
