x=0
y=0
x2=0
y2=0
mode = 0
visited = {(0,0)}
with open("day3") as f:
	for line in f:
		for ch in line:
			if mode == 0:
				if ch =='^':
					y += 1
				elif ch =='v':
					y -= 1
				elif ch == '>':
					x += 1
				else:
					x -= 1
				visited.add((x,y))
			else:
				if ch =='^':
					y2 += 1
				elif ch =='v':
					y2 -= 1
				elif ch == '>':
					x2 += 1
				else:
					x2 -= 1
				visited.add((x2,y2))
			mode = 1 - mode
print visited
print len(visited)