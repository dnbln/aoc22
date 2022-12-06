with open("a.txt") as f:
    s = f.read()

s = s.splitlines()[0] # if it has a newline character at the end, ignore it

def fp(s, x):
    i = x
    while i < len(s):
        b = s[i-x:i]
        if len(set(b)) == x:
            break
        i += 1
    return i

print(fp(s, 4))
print(fp(s, 14))
