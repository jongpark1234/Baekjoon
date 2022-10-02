def calc(a, d, g):
    return a * (d + g) * ((a == d + g) + 1)
print(max([calc(*map(int, input().split())) for _ in range(int(input()))]))
