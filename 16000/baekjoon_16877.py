# pypy3
ret = 0
g = [0, 1, 2, 3] + [0] * 2999997
fibonacci = [0, 1]
for i in range(2, 35):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
n = int(input())
for i in range(4, 3000001):
    w = [0] * 16
    for j in range(2, 35):
        if fibonacci[j] <= i:
            w[g[i - fibonacci[j]]] = 1
        else:
            for k in range(16):
                if not w[k]:
                    g[i] = k
                    break
for i in map(int, input().split()):
    ret ^= g[i]
print('koosaga' if ret else 'cubelover')
