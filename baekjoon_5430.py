from collections import deque
from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    r = errored = False
    p = stdin.readline().rstrip()
    n = int(stdin.readline())
    s = deque(stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        s = []
    for i in p:
        if i == 'R':
            r = not r
        elif i == 'D':
            if len(s) < 1:
                errored = True
                print('error')
                break
            else:
                if r == False:
                    s.popleft()
                else:
                    s.pop()
    if not errored:
        if r == True:
            s.reverse()
        print('[' + ','.join(s) + ']')
