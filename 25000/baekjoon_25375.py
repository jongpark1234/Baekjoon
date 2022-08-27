from sys import stdin
for _ in range(int(input())):
    a, b = map(int, stdin.readline().split())
    print(+(b % a == 0 and a != b))
