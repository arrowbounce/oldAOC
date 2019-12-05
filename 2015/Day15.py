sugar = [3, 0, 0, -3]
sprinkles = [-3, 3, 0, 0]
candy = [-1, 0, 4, 0]
chocolate = [0, 0, -2, 2]
cookie = 0
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            temp = max(0, (3*a - 3*b - c)) * max(0, 3*b) * max(0, (4*c - 2 *(100-a-b-c))) * max(0,(2*(100-a-b-c)-3*a))
            if cookie < temp and (2*a + 9*b + c + 8*(100-a-b-c)) ==500:
                cookie = temp
                s = a
                t = b
                ca = c
                ch = 100-a-b-c
print s, t, ca, ch
print cookie