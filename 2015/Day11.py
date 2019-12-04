
def increment(s):
	if s[-1] == 'z':
		return increment(s[:-1]) + 'a'
	if s[-1] == 'h':
		return s[:-1] + 'j'
	if s[-1] == 'n':
		return s[:-1] + 'p'
	if s[-1] == 'k':
		return s[:-1] + 'm'
	return s[:-1] + chr(ord(s[-1])+1)

def legal(s):
	p1 = None
	p2 = None
	rule1 = 0
	rule3 = 0
	for ch in s:
		if ch == 'i' or ch == 'o' or ch == 'l':
			return False
		if p1 is None:
			p1 = ch
		elif p2 is None:
			if p1 == ch:
				rule3 += 1
			p2 = p1
			p1 = ch
		else:
			if ord(p2)+2 == ord(p1)+1 == ord(ch):
				rule1 += 1
			if p1 == ch and p1 != p2:
				rule3 +=0
			p2 = p1
			p1 = ch
	return (rule1 > 0) and (rule3 >=2) 

password = "hepxcrrq"
for x in range(len(password)):
	if password[x] == 'i':
		password = password[:x] + 'j' + 'a'*(8-x-1)
	if password[x] == 'o':
		password = password[:x] + 'p' + 'a'*(8-x-1)
	if password[x] == 'l':
		password = password[:x] + 'm' + 'a'*(8-x-1)
password = increment(password)

while not legal(password):
	password = increment(password)
print password