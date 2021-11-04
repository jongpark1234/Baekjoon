from sys import stdin
input = lambda : stdin.readline().rstrip()
n, p = map(int, input().split())
stack = [[] for _ in range(7)]
moving = 0
for _ in range(n):
    line, fret = map(int, input().split())
    if len(stack[line]) == 0:
        stack[line].append(fret)
        moving += 1
    else:
        if stack[line][-1] < fret:
            stack[line].append(fret)
            moving += 1
        elif stack[line][-1] > fret:
            while stack[line]:
                if stack[line][-1] <= fret:
                    break
                stack[line].pop()
                moving += 1
            if len(stack[line]) and stack[line][-1] == fret:
                continue
            stack[line].append(fret)
            moving += 1
        else:
            continue
print(moving)
