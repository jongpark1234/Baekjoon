from sys import stdin
MAX = 10000001
sieve = [False, False] + [True for _ in range(MAX)]
for i in range(2, int(MAX ** 0.5) + 1):
    if sieve[i]:
        for j in range(i + i, MAX, i):
            sieve[j] = False
while True:
    try:
        a, b = map(int, stdin.readline().split())
        print(sum(sieve[a:b + 1]))
        print(input())
    except EOFError:
        break
