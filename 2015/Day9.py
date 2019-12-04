class Node:
	def __init__(self, n):
		self.loc = n
		self.path = {}

NList = {
	"Tristram": Node("Tristram"),
	"AlphaCentauri": Node("AlphaCentauri"),
	"Snowdin": Node("Snowdin"),
	"Tambi": Node("Tambi"),
	"Faerun": Node("Faerun"),
	"Norrath": Node("Norrath"),
	"Straylight": Node("Straylight"),
	"Arbre": Node("Arbre")
}

with open("Day9") as f:
	for line in f:
		a, _, b, _, dist = line.split(' ')
		NList[a].path[b] = int(dist)
		NList[b].path[a] = int(dist)

locs = NList.keys()

def helper(loc, remain, NList):
	if len(remain) == 0:
		return [0, 0]
	minl = 999999
	maxl = 0
	for n in remain:
		hold = helper(n, [x for x in remain if x != n], NList)
		if hold[0] + NList[loc].path[n] < minl:
			minl = hold[0] + NList[loc].path[n]
		if hold[1] + NList[loc].path[n] > maxl:
			maxl = hold[1] + NList[loc].path[n]
	return [minl, maxl]

mind = 999999
maxd = 0
for l in locs:
	hold = helper(l, [x for x in locs if x!= l], NList)
	if hold[0]< mind:
		mind = hold[0]
	if hold[1] > maxd:
		maxd = hold[1]
print maxd 
print mind