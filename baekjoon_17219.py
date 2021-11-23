from sys import stdin
site = {}
n, m = map(int, stdin.readline().split())
for _ in range(n):
    address, pw = stdin.readline().rstrip().split()
    site[address] = pw
for _ in range(m):
    print(site[stdin.readline().rstrip()])
