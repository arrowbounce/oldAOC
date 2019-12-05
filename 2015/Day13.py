class person:
    def __init__(self, name):
        self.n = name
        self.diff = {}

people = {
    "Alice": person("Alice"),
    "Bob": person("Bob"),
    "Carol": person("Carol"),
    "David": person("David"),
    "Eric": person("Eric"),
    "Frank": person("Frank"),
    "George": person("George"),
    "Mallory": person("Mallory")
}
def getsum(s, people):
    tot = 0
    for a in range(8):
        if a == 7:
            pass
            #tot += people[s[7]].diff[s[0]]
        else:
            tot += people[s[a]].diff[s[a+1]]
        if a==0:
            pass
        else:
            tot += people[s[a]].diff[s[a-1]]
    return tot

def getperms(s):
    if len(s) == 1:
        return [s]
    out = []
    for p in s:
        q = getperms([x for x in s if x != p])
        for a in q:
            a.append(p)
        out.extend(q)
    return out
with open("Day13") as f:
    for line in f:
        x = line.split()
        if x[2] == 'gain':
            opponent = x[-1]
            opponent = opponent[:-1]
            people[x[0]].diff[opponent] = int(x[3])
        else:
            opponent = x[-1]
            opponent = opponent[:-1]
            people[x[0]].diff[opponent] = int(x[3]) * -1

x = list(people.keys())
x.sort()
a = getperms(x)
mins = 999999
maxs = 0
holdmax = ""
holdmin = ""
for x in a:
    val = getsum(x, people)
    if val < mins:
        holdmin = x
        mins = val
    if val > maxs:
        holdmax = x
        maxs = val
print mins
print maxs
print holdmax