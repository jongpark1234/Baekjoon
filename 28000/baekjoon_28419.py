n = int(input())
a = list(map(int, input().split()))
o, e = sum(a[0::2]), sum(a[1::2])
print(-1 if n == 3 and o > e else abs(o - e))
