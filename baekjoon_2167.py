# pypy3
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(int(input())):
    temp = 0
    i, j, x, y = map(int, input().split())
    for xpos in range(i - 1, x):
        for ypos in range(j - 1, y):
            temp += arr[xpos][ypos]
    print(temp)
