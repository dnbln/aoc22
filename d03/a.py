with open("a.txt") as f:
    s = f.read()

v = [[l[:len(l)//2], l[len(l)//2:]] for l in s.splitlines()]

def pr(x):
    if x.isupper():
        return ord(x) - ord('A') + 27
    else:
        return ord(x) - ord('a') + 1

print(sum([pr(next(iter(set(a) & set(b)))) for [a, b] in v]))

cv = s.splitlines()
cvv = []
i = 0
while i < len(cv):
    cvv.append([cv[i], cv[i+1], cv[i+2]])
    i += 3

print(sum([pr(next(iter(set(a)&set(b)&set(c)))) for [a,b,c] in cvv]))
