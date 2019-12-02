import hashlib
input = "bgvyzdsv"
i = 0
while True:
	hold = hashlib.md5(input + str(i)).hexdigest()
	if hold.startswith('000000'):
		print i
		print hold
		break
	i+= 1