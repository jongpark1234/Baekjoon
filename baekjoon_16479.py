k = int(input())
d1, d2 = map(int, input().split())
m = (k ** 2) - ((d1 - d2) / 2) ** 2
print(int(m) if m.is_integer() else m)
