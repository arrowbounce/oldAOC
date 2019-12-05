import numpy
numpy.set_printoptions(threshold=numpy.inf)
lights = []
size = 100
a = numpy.zeros((size+2,size+2))
with open("Day18") as f:
    for line in f:
        lights.append(list(line.strip()))
for i in range(size):
    for j in range(size):
        if lights[i][j] == "#":
            a[i+1][j+1] = 1
        else:
            a[i+1][j+1] = 0

def conway(chart, size):
    out = numpy.zeros((size+2,size+2))
    chart[1,1] = 1
    chart[1,size] = 1
    chart[size,1] = 1
    chart[size,size] = 1
    for i in range(1, size+1):
        for j in range(1, size+1):
            sub = chart[i-1:i+2,j-1:j+2]
#            subs = [(x,y) for x in [i-1, i, i+1] for y in [j-1, j, j+1] if (i,j) != (x,y)]
#            sub = [chart[x,y] for x,y in subs]
            neighbors = numpy.count_nonzero(sub)
            if chart[i][j] == 1:
                if neighbors == 3 or neighbors == 4:
                    out[i][j] = 1
            else:
                if neighbors == 3:
                    out[i][j] = 1
    out[1,1] = 1
    out[1,size] = 1
    out[size,1] = 1
    out[size,size] = 1
    return out
def conwayprint(chart,size):
    for i in range(1,size+1):
        output = ""
        for j in range(1, size+1):
            if chart[i][j] == 1:
                output += "#"
            else:
                output += "."
        print output
    print ""

for _ in range(100):
#    conwayprint(a, size)
    a = conway(a, size)
conwayprint(a, size)
print numpy.count_nonzero(a)