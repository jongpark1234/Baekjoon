from sys import stdin
n, k = map(int, stdin.readline().split())
numlist = []
for i in range(n):
    numlist.append(float(stdin.readline()))
numlist.sort()
print('{:.2f}'.format(sum(numlist[k:n-k]) / (n - 2 * k) + 1e-8))
print('{:.2f}'.format((sum([numlist[k]] * k) + sum([numlist[-(k + 1)]] * k) + sum(numlist[k:n-k])) / n + 1e-8))
