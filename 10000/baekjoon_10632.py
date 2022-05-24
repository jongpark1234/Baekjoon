n, a, b = map(int, input().split())
stones = [int(input()) for _ in range(n)]
Min = min(a, b)
grundy = 0
heaps = 0
for i in range(n):
    grundy ^= stones[i] % (Min + 1)
    if stones[i] > Min:
        heaps += 1
if heaps == 0 or a == b:
    print(['Jiro', 'Hanako'][grundy > 0])
elif a > b:
    print('Hanako')
else:
    num = a + 1
    Max = max(stones)
    grundy = grundy ^ (Max % num)
    r = (((Max - grundy) % num) + num) % num
    print(['Hanako', 'Jiro'][(r == 0 or r > a or r < Max - a) or (grundy != (Max - r) % num)])
