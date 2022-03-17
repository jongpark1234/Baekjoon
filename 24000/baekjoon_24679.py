from sys import stdin
for _ in range(int(input())):
    stones = sorted(list(map(int, stdin.readline().split())))
    w = min(stones[2], stones[0] + stones[1] - 2)
    print('B' if (stones[0] == 0 and stones[1] % 2) or (stones[0] == 1 and stones[1] == stones[2] and stones[1] % 2) or (stones[0] > 1 and stones[0] % 2 == 0 and stones[1] % 2 == 0 and w % 2 == 0) or (stones[0] > 1 and (stones[0] + stones[1] + w) % 4 == 3) else 'R')
