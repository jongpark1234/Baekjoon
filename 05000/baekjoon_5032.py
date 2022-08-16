e, f, c = map(int, input().split())
bottle = e + f
result = 0
while bottle >= c:
    bottle -= c - 1
    result += 1
print(result)
