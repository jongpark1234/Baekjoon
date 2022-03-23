from sys import stdin
Sum = 0
Xor = 0
for _ in range(int(stdin.readline())):
    cmd = [*map(int, stdin.readline().split())]
    if cmd[0] == 1:
        Sum += cmd[1]
        Xor ^= cmd[1]
    elif cmd[0] == 2:
        Sum -= cmd[1]
        Xor ^= cmd[1]
    else:
        print(Sum if cmd[0] == 3 else Xor)
