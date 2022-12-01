with open("f.txt") as f:
    s = f.read()

v = [sum([int(x) for x in elf.splitlines()]) for elf in s.split('\n\n')]
v.sort()

print(v[-1])
print(sum(v[-3:]))
