x=0
y=0
visited = {(0,0)}
with open("day3") as f:
	for line in f:
		for ch in line:
			if ch =='^':
				y += 1
			elif ch =='v':
				y -= 1
			elif ch == '>':
				x += 1
			else:
				x -= 1
			visited.add((x,y))
print visited
print len(visited)