import re

with open("a.txt") as f:
    s = f.read()

def parse_stack(stacks, i):
    stk = []
    j = len(stacks)-1
    while j >= 0:
        if stacks[j][i] != '':
            stk.append(stacks[j][i][1:2])
        else:
            break
        j -= 1
    return stk

split = s.split('\n\n')
txt_stacks = [re.split("[\s]{1,4}", line) for line in split[0].splitlines()[:-1]]
stacks = []
for i in range(len(txt_stacks[0])):
    stacks.append(parse_stack(txt_stacks, i))

def exe_move(stacks, move):
    if move[0] == 0: return stacks
    stacks = exe_move(stacks, [move[0]-1] + move[1:])
    stacks[move[2]-1].append(stacks[move[1]-1].pop())
    return stacks

def exe_move_2(stacks, move):
    if move[0] == 0: return stacks
    top = stacks[move[1]-1].pop()
    stacks = exe_move_2(stacks, [move[0]-1] + move[1:])
    stacks[move[2]-1].append(top)
    return stacks

moves = [[int(x) for x in l.split( )[1:6:2]] for l in split[1].splitlines()]

stacks_1 = [s.copy() for s in stacks]
stacks_2 = [s.copy() for s in stacks]

for move in moves:
    stacks_1 = exe_move(stacks_1, move)
    stacks_2 = exe_move_2(stacks_2, move)

print(''.join([s[-1] for s in stacks_1]))
print(''.join([s[-1] for s in stacks_2]))
