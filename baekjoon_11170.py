from sys import stdin
for _ in range(int(stdin.readline())):
    count = 0
    n, m = map(int, stdin.readline().split())
    for i in range(n, m + 1):
        count += str(i).count('0')
    print(count)
