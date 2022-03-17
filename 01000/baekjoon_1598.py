a, b = map(lambda x: int(x) - 1, input().split())
print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))
