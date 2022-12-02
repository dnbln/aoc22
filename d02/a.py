with open("a.txt") as f:
    s = f.read()

v = [[ord(x.split(' ')[0]) - ord('A'), ord(x.split(' ')[1]) - ord('X')] for x in s.splitlines()]
def t(a, b):
    s = b + 1
    outcome = 0
    if a == b:
        outcome = 3
    elif (b == (a + 1) % 3):
        outcome = 6
    return s + outcome

total = sum([t(a, b) for [a, b] in v])
print(total)

def remap(a, b):
    if b == 1:
        return [a, a]
    elif b == 0:
        return [a, (a + 2) % 3]
    elif b == 2:
        return [a, (a + 1) % 3]

cv = [remap(a, b) for [a, b] in v]
total2 = sum([t(a, b) for [a, b] in cv])
print(total2)
