
def reccount(string, left):
	curchar = None
	count = 0
	output = ""
	for ch in string:
		if curchar is None:
			curchar = ch
		elif curchar != ch:
			output += str(count) + str(curchar)
			curchar = ch
			count = 0
		count += 1
	output += str(count) + str(curchar)
	return [output, left-1]

val = "1113222113"
for _ in range(40):
	val = reccount(val, _)[0]
print len(val)