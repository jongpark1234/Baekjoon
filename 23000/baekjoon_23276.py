result = float('inf')
for _ in range(int(input())):
    y, c1, c2 = map(int, input().split())
    year = y + 1
    while (year - y) % c1 or (year - y) % c2:
        year += 1
    result = min(result, year)
print(result)
