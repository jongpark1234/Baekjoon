n, t = map(int, input().split())
t -= 1
p = n * 2 - 1; q = t // p
print(n * 2 - t % p if q & 1 else t % p + 1)
