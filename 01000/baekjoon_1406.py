from sys import stdin
front = list(stdin.readline().rstrip())
back = []
for _ in range(int(stdin.readline())):
    cmd = stdin.readline().rstrip().split()
    if cmd[0] == 'L' and front:
        back.append(front.pop())
    elif cmd[0] == 'D' and back:
            front.append(back.pop())
    elif cmd[0] == 'B' and front:
            front.pop()
    elif cmd[0] == 'P':
        front.append(cmd[1])
print(''.join(front + back[::-1]))
