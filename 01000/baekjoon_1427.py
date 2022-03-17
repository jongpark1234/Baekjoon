n = list(map(int, input()))
n.sort(reverse=True)
for i in range(len(n)): print(n[i], end='')
