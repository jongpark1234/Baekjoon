ret = 0
n, m = map(int, input().split())
for i in [sum(map(int, input().split())) for _ in range(n)]:
    ret ^= i
print('august14' if ret else 'ainta')
