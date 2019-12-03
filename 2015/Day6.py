import numpy
array = numpy.zeros((1000,1000), dtype = numpy.int)
with open("Day6") as f:
	for line in f:
		h = line.split()
		if h[0] == "toggle":
			xy1 = h[1].split(",")
			xy2 = h[3].split(",")
			x = slice(int(xy1[0]), int(xy2[0])+1)
			y = slice(int(xy1[1]), int(xy2[1])+1)
			array[x,y] += 2
		elif h[1] == "on":
			xy1 = h[2].split(",")
			xy2 = h[4].split(",")
			x = slice(int(xy1[0]), int(xy2[0])+1)
			y = slice(int(xy1[1]), int(xy2[1])+1)
			array[x,y] += 1
		else:
			xy1 = h[2].split(",")
			xy2 = h[4].split(",")
			x = slice(int(xy1[0]), int(xy2[0])+1)
			y = slice(int(xy1[1]), int(xy2[1])+1)
			array[x,y] -= 1
		array[array<0] = 0
print sum(sum(array))
