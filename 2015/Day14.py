class deer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = int(speed)
        self.time = int(time)
        self.rest = int(rest)
        self.clock = 0
        self.timer = 0
        self.mode = 0
        self.dists = 0
    def dist(self, time):
        full = time//(self.time + self.rest)
        extra = time % (self.time + self.rest)
        if extra < self.time:
            return (full * self.time + extra)*self.speed
        return (full+1) * self.time * self.speed
    def tick(self):
        self.clock += 1
        self.timer += 1
        if self.mode == 0:
            self.dists += self.speed
            if self.timer == self.time:
                self.mode = 1
                self.timer = 0
        else:
            if self.timer == self.rest:
                self.mode = 0
                self.timer = 0
        return self.dists
maxd = 0
reindeer = {}
times = {}
with open("Day14") as f:
    for line in f:
        x = line.split()
        a = deer(x[0], x[3], x[6], x[13])
        reindeer[a.name] = a
        times[a.name] = 0
        d = a.dist(2503)
        if d > maxd:
            maxd = d
for a in range(2503):
    curmax = 0
    maxdeer = []
    for r in reindeer.keys():
        dist = reindeer[r].tick()
        if dist > curmax:
            curmax = dist
            maxdeer = [r]
        elif dist == curmax:
            maxdeer.append(r)
    for r in maxdeer:
        times[r] += 1
print maxd
print times
print [(d.name, d.dists) for d in reindeer.values()] 

