from sys import stdin
for _ in range(int(stdin.readline())):
    a, b, c = map(int, stdin.readline().split())
    print(min(a, b, c))
