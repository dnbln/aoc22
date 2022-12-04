with open("a.txt") as f:
    s = f.read()

def remap(x):
    return [int(a) for a in x.split('-')]

v = [[remap(a) for a in x.split(',')] for x in s.splitlines()]

def cont(a, b):
    return a[0] <= b[0] and a[1] >= b[1] or a[0] >= b[0] and a[1] <= b[1]

print(sum([1 if cont(a,b) else 0 for [a,b] in v]))

def ovl(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]

print(sum([1 if ovl(a,b) else 0 for [a,b] in v]))
