from sys import stdin
while True:
    n = int(stdin.readline())
    if not n:
        break
    print(sorted([stdin.readline().rstrip() for _ in range(n)], key = lambda x: x.lower())[0])
