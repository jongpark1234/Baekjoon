from sys import stdin
s = set()
for _ in range(int(input())):
    command = stdin.readline().rstrip().split()
    if len(command) == 1:
        if command[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    command, temp = command[0], int(command[1])
    if command == 'add':
        s.add(temp)
    elif command == 'remove':
        s.discard(temp)
    elif command == 'check':
        print(1 if temp in s else 0)
    elif command == 'toggle':
        if temp in s:
            s.discard(temp)
        else:
            s.add(temp)
