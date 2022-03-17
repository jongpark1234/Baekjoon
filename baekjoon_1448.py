from sys import stdin
input = stdin.readline
side = sorted([int(input()) for _ in range(int(input()))], reverse=True)
for i in range(len(side) - 2):
    if side[i] < side[i + 1] + side[i + 2]:
        print(side[i] + side[i + 1] + side[i + 2])
        exit(0)
print(-1)
