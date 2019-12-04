import json

def sumdict(d):
    t= 0
    if "red" in d.values() or "red" in d.keys():
        return 0
    for l in d.values():
        if isinstance(l, dict):
            t += sumdict(l)
        elif isinstance(l, list):
            t += sumlist(l)
        elif isinstance(l, int):
            t+= l
    return t
def sumlist(c):
    t = 0
    for l in c:
        if isinstance(l, dict):
            t += sumdict(l)
        elif isinstance(l, list):
            t += sumlist(l)
        elif isinstance(l, int):
            t+= l
    return t
with open("Day12") as f:
    for l in f:
        x = json.loads(l)
        s = sumdict(x)
print s